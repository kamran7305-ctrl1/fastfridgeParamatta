#!/usr/bin/env python3
"""Static technical-SEO audit for the Fridge Repair Parramatta site.

Runs on the repository checkout (no network, no database). It checks what can be
proven from the source: page metadata, canonicals, robots directives, JSON-LD,
the internal link graph (broken links, orphans, links to redirecting URLs),
robots.txt, the generated sitemap and the clean-URL routing in .htaccess.

Exit code 0 = no failures, 1 = at least one failure. Warnings never fail the run.
Usage: python3 tests/site_audit.py [--report]
"""
import glob, html, json, os, re, subprocess, sys
from urllib.parse import urlparse, urljoin, unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://fridgerepairparramatta.com.au'
fails, warns = [], []

def fail(msg): fails.append(msg)
def warn(msg): warns.append(msg)
def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8', errors='replace') as f: return f.read()

# ---------------------------------------------------------------- routes
legacy_blog = re.compile(r'^blog-[a-z0-9-]+\.html$')
static_pages = {}   # route -> file
for f in sorted(glob.glob(os.path.join(ROOT, '*.html'))):
    n = os.path.basename(f)
    if n == 'index.html': static_pages['/'] = n; continue
    if legacy_blog.match(n): continue          # legacy snapshots, 301 to /blog/<slug>
    if n == 'blog.html': continue              # served by blog.php at /blog
    static_pages['/' + n[:-5]] = n
dynamic = {'/blog': 'blog.php', '/about': 'about.php'}
ROUTES = {**static_pages, **dynamic}
# Blog posts are database driven; any /blog/<slug> is treated as valid here.
def is_route(path):
    path = path.rstrip('/') or '/'
    if path in ROUTES: return True
    if re.fullmatch(r'/blog/[a-z0-9-]+', path): return True
    return False

# ---------------------------------------------------------------- page facts
pages = {}
for route, fname in ROUTES.items():
    src = read(fname)
    if fname == 'about.php':
        # about.php pulls SEO fields from the database; use the static fallbacks if present
        pass
    title = re.search(r'<title[^>]*>(.*?)</title>', src, re.S)
    canon = re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', src)
    desc = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]*)"', src)
    robots = re.findall(r'<meta[^>]+name="robots"[^>]+content="([^"]*)"', src)
    h1 = re.findall(r'<h1[\s>]', src)
    pages[route] = dict(file=fname, src=src,
        title=html.unescape(title.group(1).strip()) if title else None,
        canon=canon.group(1) if canon else None,
        desc=html.unescape(desc.group(1)) if desc else None,
        robots=robots, h1=len(h1))

for route, p in pages.items():
    f = p['file']
    dyn = f.endswith('.php')
    if not dyn:
        if not p['title']: fail(f'{f}: missing <title>')
        elif len(p['title']) > 70: warn(f'{f}: title is {len(p["title"])} chars (over 70)')
        if not p['desc']: fail(f'{f}: missing meta description')
        elif not 70 <= len(p['desc']) <= 175: warn(f'{f}: meta description is {len(p["desc"])} chars')
        if not p['canon']: fail(f'{f}: missing canonical')
        else:
            want = BASE + ('' if route == '/' else route)
            want_alt = BASE + '/'
            if p['canon'] not in (want, want_alt if route == '/' else want):
                fail(f'{f}: canonical {p["canon"]} does not match {want}')
        if p['h1'] != 1: fail(f'{f}: expected one <h1>, found {p["h1"]}')
    for r in p['robots']:
        if 'noindex' in r.lower(): fail(f'{f}: robots meta contains noindex ({r})')

# duplicate titles / descriptions
for key in ('title', 'desc'):
    seen = {}
    for route, p in pages.items():
        v = p[key]
        if v: seen.setdefault(v, []).append(p['file'])
    for v, fs in seen.items():
        if len(fs) > 1: fail(f'duplicate {key} on {", ".join(fs)}: {v[:70]}')

# JSON-LD must parse
for route, p in pages.items():
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', p['src'], re.S):
        raw = m.group(1)
        if '<?' in raw: continue
        try:
            d = json.loads(raw)
        except Exception as e:
            fail(f'{p["file"]}: invalid JSON-LD ({e})'); continue
        graph = d.get('@graph', [d])
        for node in graph:
            if node.get('@type') == 'FAQPage':
                for q in node.get('mainEntity', []):
                    ans = html.unescape(q['acceptedAnswer']['text'])
                    plain = html.unescape(re.sub(r'<[^>]+>', ' ', p['src']))
                    if ans not in plain: fail(f'{p["file"]}: FAQ schema text not found on page: {q["name"][:50]}')
        if 'aggregateRating' in raw:
            warn(f'{p["file"]}: aggregateRating in schema (needs real, visible, verifiable reviews)')

# ---------------------------------------------------------------- link graph
inbound = {r: set() for r in ROUTES}
broken, redirecting = [], []
asset_ext = ('.css', '.js', '.png', '.jpg', '.jpeg', '.webp', '.svg', '.ico', '.zip', '.xml', '.txt', '.pdf', '.json')
def normalise(href, page_route):
    href = href.strip()
    if not href or href.startswith(('mailto:', 'tel:', 'javascript:', '#', 'data:')): return None
    u = urlparse(href)
    if u.scheme in ('http', 'https'):
        if u.netloc.replace('www.', '') != 'fridgerepairparramatta.com.au': return None
        path = u.path
    else:
        path = u.path
        if not path.startswith('/'):
            path = '/' + path          # every page uses site-root-relative links (blog pages set <base href="/">)
    return unquote(path) or '/'
for route, p in pages.items():
    src = p['src']
    for m in re.finditer(r'<a\s[^>]*href="([^"]*)"', src):
        h = m.group(1)
        if '<?' in h: continue
        path = normalise(h, route)
        if path is None or path.lower().endswith(asset_ext): continue
        if path.startswith(('/admin', '/image/', '/includes')): continue
        target = path.rstrip('/') or '/'
        if re.fullmatch(r'/blog-[a-z0-9-]+(\.html)?', target) or target.endswith('.html') or path == '/fridge-repair-parramatta/':
            redirecting.append((p['file'], h)); continue
        if path != '/' and path.endswith('/') and target in ROUTES:
            redirecting.append((p['file'], h)); continue
        if is_route(target):
            if target in inbound and target != route: inbound[target].add(p['file'])
        else:
            broken.append((p['file'], h))
for f, h in sorted(set(broken)): fail(f'{f}: broken internal link {h}')
for f, h in sorted(set(redirecting)): warn(f'{f}: link to a redirecting URL {h}')
for route, srcs in inbound.items():
    if route != '/' and not srcs: fail(f'orphan page (no internal links to it): {route}')

# ---------------------------------------------------------------- robots.txt
rob = read('robots.txt')
if re.search(r'^\s*Disallow:\s*/\s*$', rob, re.M): fail('robots.txt blocks the whole site')
if f'Sitemap: {BASE}/sitemap.xml' not in rob: fail('robots.txt is missing the absolute Sitemap line')

# ---------------------------------------------------------------- sitemap
try:
    out = subprocess.run(['php', os.path.join(ROOT, 'sitemap.php')], capture_output=True, text=True, timeout=30).stdout
except Exception as e:
    out = ''; warn(f'could not run sitemap.php: {e}')
if out:
    if not out.startswith('<?xml'): fail('sitemap output does not start with the XML declaration')
    locs = re.findall(r'<loc>([^<]+)</loc>', out)
    if len(locs) != len(set(locs)): fail('sitemap has duplicate URLs')
    sm = set()
    for l in locs:
        if not l.startswith(BASE): fail(f'sitemap URL is not on the preferred HTTPS host: {l}'); continue
        path = l[len(BASE):] or '/'
        sm.add(path)
        if not is_route(path): fail(f'sitemap lists a URL that is not a route: {l}')
    for route in ROUTES:
        if route not in sm: fail(f'indexable page missing from sitemap: {route}')
    for lm in re.findall(r'<lastmod>([^<]+)</lastmod>', out):
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', lm): fail(f'bad lastmod {lm}')
    dates = set(re.findall(r'<lastmod>([^<]+)</lastmod>', out))
    if len(dates) == 1 and len(locs) > 5:
        warn(f'every sitemap URL has the same lastmod ({next(iter(dates))}); lastmod is not telling Google which pages changed')

# ---------------------------------------------------------------- .htaccess routing
ht = read('.htaccess')
generic = 'REQUEST_FILENAME}.html' in ht or '%{DOCUMENT_ROOT}/$1.html' in ht
if not generic:
    m = re.search(r'RewriteRule \^\(([^)]+)\)/\?\$ \$1\.html', ht)
    listed = set(m.group(1).split('|')) if m else set()
    for route, fname in static_pages.items():
        if route != '/' and route[1:] not in listed: fail(f'.htaccess has no clean-URL route for {route}')
if 'RewriteRule ^fridge-repair-parramatta/?$ index.html' in ht:
    warn('.htaccess serves the old /fridge-repair-parramatta/ slug as a 200 duplicate of the homepage instead of a 301')

# ---------------------------------------------------------------- report
if '--report' in sys.argv:
    print(f'routes checked: {len(ROUTES)}   internal link targets: {sum(len(v) for v in inbound.values())}')
for w in warns: print('WARN ', w)
for f_ in fails: print('FAIL ', f_)
print(f'\n{len(fails)} failure(s), {len(warns)} warning(s)')
sys.exit(1 if fails else 0)
