#!/usr/bin/env python3
"""Write site-manifest.json: the list of public pages tracked in git, each with the date
of the last commit that touched it. Run in CI before the FTP upload so sitemap.php can
(1) list only pages that really belong to the site, even if stale files linger on the
server, and (2) use real change dates for <lastmod> instead of file upload times."""
import json, os, subprocess, datetime
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
files = subprocess.run(['git', 'ls-files', '*.html', '*.php'], cwd=root, capture_output=True, text=True, check=True).stdout.split()
pages = {}
for f in sorted(files):
    if '/' in f: continue                      # root-level pages only
    out = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', f], cwd=root, capture_output=True, text=True).stdout.strip()
    pages[os.path.splitext(f)[0]] = out or datetime.date.today().isoformat()
with open(os.path.join(root, 'site-manifest.json'), 'w') as fh:
    json.dump({'generated': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'pages': pages}, fh, indent=1)
print(f'manifest: {len(pages)} pages')
