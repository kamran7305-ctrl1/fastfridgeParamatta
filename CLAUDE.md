# fridgerepairparramatta.com.au: project memory

Static HTML site plus a small PHP/MySQL blog admin, deployed to Hostinger by GitHub Actions (FTP). See HOSTINGER_DEPLOYMENT.md.

## Daily page routine (important)
The owner does not want to say each day which page to build.
1. Read `claude/page-progress.md`. Find the first page marked TO DO in its build order.
2. Tell the owner in one line: "Today's page: <name> (<URL>, primary keyword <kw>)", then build it.
3. Use `claude/keyword-strategy.md` for that page's title, meta, H1, keywords, notes and competitors.
4. Follow `claude/content-standard.md`, `claude/website-context.md` and `claude/seo-playbook.md` (Part B page rules; Part C keeps this site different from fridgerepairblacktown.com.au) (Australian English, no em dashes, no AI tells, no invented reviews, stats, phone or ARCtick numbers, no senior discount, prices must match /fridge-repair-cost).
5. When the page is done: update `claude/page-progress.md` (status plus log line), add links to it from related live pages, add it to the sitemap and `.htaccess`, commit and push to the branch you were given.

## Site rules
- Flat URLs only (`/fridge-regas`, `/lg-fridge-repair`). The keyword sheet's `/services/...`, `/commercial/...`, `/brands/...` URLs are not used; the flat mapping is in `claude/keyword-strategy.md`.
- Each page is a root `*.html` file. New page = copy the site's header/footer from an existing page, add the route to `.htaccess` (both lists), add its priority to `sitemap.php`.
- `tailwind-built.css` is precompiled. After adding new Tailwind classes run `cd .buildtools && npm ci && npx tailwindcss -i input.css -o ../tailwind-built.css --minify`.
- No phone number exists on the site, so never add a tel: link. No ARCtick number is known: use the owner's wording ("ARCtick licensed & verified" or "ARC-licensed") and no number. Lic #R38910 is on the site.
- Pages so far: regas, Samsung, LG. Everything else is tracked in `claude/page-progress.md`.
- Branches: PR #8 and #9 are merged. Start each new page on a fresh branch cut from `origin/main` (for example `claude/ice-machine-page`) and open a separate PR. Leave `claude/site-layout-review-knuu9t` (old PR #7) untouched.
- Never push to `main` unless asked. Pushing a `claude/**` branch also deploys to the live site.

## Playbook rules (claude/seo-playbook.md, 20 Oct 2026)
- Never target Blacktown, Seven Hills, Prospect, Glenwood or Quakers Hill on this site, and never link to or copy text from fridgerepairblacktown.com.au. Do not reuse its section order or FAQ wording (Part C).
- Titles up to 60 characters and metas 140 to 155 with a clear next step. FAQ questions should be H3 headings. No aggregateRating until real, visible reviews exist.
- Nav and body links must point to real pages. Use one price source of truth ($150 to $450 repair, call-out $60 to $200 residential, $100 to $250 commercial) and say plainly what is free (the quote) versus paid (the call-out).
- OWNER DECISION (20 Oct): do NOT touch the existing reviews, rating, testimonials or live-status banners on the site, and make no site changes because of the playbook. The playbook is saved as reference only. Do not add new review or rating markup to new pages.
- Open items for the owner (not code, do not do them unless asked): phone number and `tel:` links, `[confirm]` placeholders on the cost page, GBP and reviews.
