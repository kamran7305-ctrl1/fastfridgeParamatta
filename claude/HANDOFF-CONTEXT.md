# Handoff: fridgerepairparramatta.com.au (full context for another AI)

Written 26 Oct 2026. Paste this whole file into the new AI, then also give it `CLAUDE.md` and the files in `claude/`. Anything marked *unverified* could not be checked from the sandbox. Check live state (PR status, deploys) before relying on it.

## 1. The owner and how to talk to them
- Owner writes Roman Urdu/English. Keep replies short and simple, step by step.
- Merge instructions style: "green Merge pull request, then Confirm merge".
- End-of-day summaries: short formal English bullets, each page with each point.
- Daily routine: owner says "NEXT PAGE". First ask them to confirm the page returns 404 live (the sandbox cannot reach the live site), then build it.
- The owner merges PRs. Do not merge for them.

## 2. The project
- Static HTML site plus a small PHP/MySQL blog admin (`admin/`), hosted on Hostinger.
- Repo: `kamran7305-ctrl1/fastfridgeParamatta`. Deploy: GitHub Actions FTP (`.github/workflows/deploy.yml`, SamKirkland/FTP-Deploy-Action v4.3.5, `protocol: ftps`, `server-dir: ./`, `dangerous-clean-slate: false`).
- **Pushing to `main` or any `claude/**` branch deploys to the live site.** Branches with other names (for example `seo-technical-audit`) do not deploy. Merging a PR to `main` does.
- Secrets (FTP server, user, password) live in GitHub secrets. Never print or commit credentials.
- Pages are root `*.html` files with clean URLs through `.htaccess` (two hand-kept route lists). Dynamic: `blog.php`, `blog-post.php`, `about.php`, `sitemap.php`. Shared: `includes/site-header.php`, `site-footer.php`, `page-seo.php`.
- CSS is precompiled Tailwind. After adding new classes: `cd .buildtools && npm ci && npx tailwindcss -i input.css -o ../tailwind-built.css --minify`.

## 3. Rules (owner decisions, do not break)
- Read `CLAUDE.md`, `claude/content-standard.md`, `claude/website-context.md`, `claude/seo-playbook.md`, `claude/keyword-strategy.md`.
- Flat URLs for pages (`/fridge-regas`). Blog posts live at `/blog/<slug>`; old `/blog-<slug>` 301s to the new form; listing stays `/blog`.
- Do NOT touch existing reviews, ratings, testimonials or live-status banners. Add no new review or rating markup to new pages. The SEO playbook is reference only: make no site changes because of it.
- Never target Blacktown, Seven Hills, Prospect, Glenwood or Quakers Hill. Never link to or copy text from fridgerepairblacktown.com.au.
- No phone number and no `tel:` links. No ARCtick number: write "ARCtick licensed & verified" or "ARC-licensed". Lic #R38910 is on the site.
- Prices must match `/fridge-repair-cost`: repair $150 to $450, call-out $60 to $200 residential, $100 to $250 commercial. Say what is free (the quote) and what is paid (the call-out). No senior discount.
- Australian English, no em dashes, no AI-sounding phrases, no invented reviews, stats or numbers. New pages use no photos.
- Titles up to 60 characters, metas 140 to 155, FAQ questions as H3. FAQ schema text must match the on-page text. Unique content and FAQs per page (checked by 6-word shingle overlap; Samsung/LG overlap was cut from 55% to 16%).
- New page checklist: copy header/footer from an existing page, add the route to both `.htaccess` lists, add priority in `sitemap.php`, link it from related live pages, update `claude/page-progress.md`, save schema JSON to `claude/schemas/`.
- Each new page goes on a fresh branch cut from `origin/main` (for example `claude/ice-machine-page`) with its own PR. Never push to `main`. Leave branch `claude/site-layout-review-knuu9t` (old PR #7) untouched.

## 4. Page status
Built (all root `.html`): regas, samsung-fridge-repair-parramatta, lg-fridge-repair, commercial-refrigeration-repair, coolroom-repair, commercial-freezer-repair, ice-machine-repair, fridge-door-seal-replacement, freezer-repair, fridge-compressor-repair, areas, fridge-repairs-parramatta, fridge-repair-westmead, fridge-repair-granville, fridge-repair-north-parramatta, fridge-repair-harris-park.

TO DO (in order, see `claude/page-progress.md`): fridge-repair-merrylands, fridge-repair-hills-district, westinghouse-fridge-repair, fisher-paykel-fridge-repair, blogs `/blog/why-is-my-fridge-leaking-water`, `/blog/fridge-regas-cost-parramatta`, `/blog/freezer-not-freezing`, then lower-priority brands.

Later phase: optimise title/meta/H1 for older live pages (home, services, fridge-not-cooling-repair, fridge-regas, fridge-repair-cost, emergency-fridge-repair, brands, blog post fridge-not-cooling-causes).

Whether each page is live on the server depends on deploys. *Unverified*: ask the owner to open the URL. Earlier, one deploy race removed three pages from the server; it was fixed by re-running the deploy and adding a workflow `concurrency` group (PR #22, merged).

## 5. Technical SEO audit (22 Oct)
Done on branch `seo-technical-audit`, **PR #23** (https://github.com/kamran7305-ctrl1/fastfridgeParamatta/pull/23). Merge status *unverified*; check it.
- `robots.txt`: single `User-agent: *` group, `Disallow: /admin/`, Sitemap line.
- `.htaccess`: `/fridge-repair-parramatta/` 301s to `/`; deny `.ftp-deploy-sync-state.json` and `site-manifest.json`.
- `sitemap.php`: uses CI-built `site-manifest.json` (git-tracked pages and last-change dates), falls back to a directory scan.
- Blog 404: `noindex, follow`, no canonical.
- `deploy.yml`: new `checks` job (PHP lint and `tests/site_audit.py`), manifest build, post-deploy smoke test; `tests/**` and `.github/scripts/**` excluded from upload.
- Local audit result: 0 failures, 2 warnings (aggregateRating on the homepage, left by owner decision; uniform lastmod, probably a checkout artefact).
- After merge, owner should verify live: the 301, the 403 on the state file, `/sitemap.xml`, the smoke-test step green.
- Not verifiable from the sandbox: live status codes, Cloudflare/WAF, server logs, Search Console data. Do not claim Google crawled or indexed more without Search Console evidence. 54 crawl requests alone is not proof of a technical problem.
- Stale `privacy-policy.html` and `terms-of-service.html` were removed from the repo; whether they still exist on the server is *unverified*.

## 6. Current request: convert the site to WordPress
Owner wants: same design and sections, pages as WordPress pages with code inside, nothing broken, mobile and desktop responsive, custom theme, custom plugins only where needed, error free. Owner offered to connect a WordPress MCP.

Agreed plan (nothing built yet):
1. Staging WordPress on a Hostinger subdomain (never on the live domain first), noindex.
2. Custom theme `fridge-theme` in `wp-content/themes/` in the repo, reusing `tailwind-built.css` and `app.js`; shared `header.php`/`footer.php`; one custom page template per page (Option A) so the HTML stays in code.
3. Custom plugins: inquiry form (replaces `send-inquiry.php`), SEO fields (title, meta, canonical, schema), sitemap kept at `/sitemap.xml`; blog import script from the `blog_posts` table to WordPress posts at `/blog/%postname%/`.
4. Keep every URL, redirect, title, meta, H1 and schema identical. Compare old and new with a script, plus mobile and desktop screenshots.
5. Go live with a full backup and one-step rollback; resubmit the sitemap in Search Console.
6. Deploy: theme and plugins from the repo via the FTP workflow, but keep WordPress core, `wp-content/uploads` and `wp-config.php` out of deploys (otherwise the server files can be deleted).

Limits: the sandbox cannot reach wordpress.org (403) or the live site, and there is no MySQL, so WordPress cannot be run here. A WordPress MCP usually writes content, not theme or plugin files. The owner must create staging and upload the theme zip. The WordPress MCP was not connected as of this file. Suggested branch for this work: `wp-theme` (not `claude/**`, so it does not auto-deploy).

## 7. Open items for the owner (not code)
Phone number and `tel:` links, `[confirm]` placeholders on the cost page, Google Business Profile and reviews, Search Console checks listed in the audit, Hostinger staging for WordPress.

## 8. Tooling notes for the next AI
- GitHub access in this setup is via MCP tools (`mcp__github__*`), loaded with ToolSearch; there is no `gh`. Create PRs against `kamran7305-ctrl1/fastfridgeparamatta`, base `main`.
- Page generator scripts were in an old scratchpad (`gen/build_*.py`) and are not in the repo; pages and schemas are the source of truth.
- `tests/site_audit.py` is the static audit (routes, internal links, canonicals, robots, sitemap inputs). Run `python3 tests/site_audit.py` and `php -l` on changed PHP before any push.
- Commit messages end with the attribution lines the harness asks for.
