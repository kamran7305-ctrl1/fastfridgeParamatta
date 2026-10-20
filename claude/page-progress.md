# Page progress

**Update this file after every page. At the start of each session: read this file, find the first TO DO page in the build order below, tell the user "Today's page: X (URL, primary keyword)" in 1 line, and build it.** The user must not have to say which page is next.

Standing rules: `claude/content-standard.md`, `claude/website-context.md` and `claude/seo-playbook.md` (20 Oct playbook, Part B rules and Part C anti-duplication vs the Blacktown site). Keyword data: `claude/keyword-strategy.md`. Flat URLs only. Never invent reviews, stats, phone or ARCtick numbers.

## Build order (new pages only, from the sheet's priority list)

1. COMM-FRIDGE: Commercial Fridge & Refrigeration Repair (hub) -> `/commercial-refrigeration-repair` (Wk 1-2 P1) [DONE 16 Oct]
2. COOLROOM: Coolroom & Cold Room Repair -> `/coolroom-repair` (Wk 1-2 P1) [DONE 16 Oct]
3. COMM-FREEZER: Commercial Freezer Repair -> `/commercial-freezer-repair` (Wk 3-4 P1) [DONE 16 Oct]
4. ICE: Ice Machine Repair -> `/ice-machine-repair` (Wk 3-4 P2) [DONE 19 Oct]
5. SEAL: Fridge Door Seal Replacement -> `/fridge-door-seal-replacement` (Wk 3-4 P1) [DONE 19 Oct]
6. FREEZER: Freezer Repair -> `/freezer-repair` (Wk 1-2 P1) [DONE 20 Oct]
7. COMPRESSOR: Fridge Compressor Repair & Replacement -> `/fridge-compressor-repair` [DONE 20 Oct]
8. AREAS: Areas We Service (hub) -> `/areas` [DONE 20 Oct]
9. LOC-CBD: Fridge Repairs Parramatta (own suburb page) -> `/fridge-repairs-parramatta` [DONE 20 Oct]
10. LOC-WESTMEAD: Fridge Repairs Westmead -> `/fridge-repair-westmead` [TO DO]
11. LOC-GRANVILLE: Fridge Repairs Granville -> `/fridge-repair-granville` [TO DO]
12. LOC-NPARRAMATTA: Fridge Repairs North Parramatta -> `/fridge-repair-north-parramatta` [TO DO]
13. LOC-HARRISPARK: Fridge Repairs Harris Park -> `/fridge-repair-harris-park` [TO DO]
14. LOC-MERRYLANDS: Fridge Repairs Merrylands -> `/fridge-repair-merrylands` [TO DO]
15. LOC-HILLS: Fridge Repair Hills District / Castle Hill -> `/fridge-repair-hills-district` [TO DO]
16. BR-WESTINGHOUSE: Westinghouse Fridge Repair -> `/westinghouse-fridge-repair` [TO DO]
17. BR-FP: Fisher & Paykel Fridge Repair -> `/fisher-paykel-fridge-repair` [TO DO]
18. B-LEAK: Blog: Why Is My Fridge Leaking Water? -> `/blog/why-is-my-fridge-leaking-water` [TO DO]
19. B-REGAS-COST: Blog: Fridge Regas Cost in Parramatta -> `/blog/fridge-regas-cost-parramatta` [TO DO]
20. B-FREEZER: Blog: Freezer Not Freezing -> `/blog/freezer-not-freezing` [TO DO]
21. BR-ELECTROLUX / BR-HAIER / BR-HISENSE / BAR-WINE / BR-MIELE / B-NOISE: lower priority, only after the above are indexing [TO DO]
(Dropped: LOC-BLACKTOWN, because fridgerepairblacktown.com.au is the owner's other site. EXP-WSYD is conditional on the real service area.)

## Already built (do not redo)

- REGAS: `/fridge-regas` [LIVE (built 14 Oct; optimise per sheet later)]
- BR-SAMSUNG: `/samsung-fridge-repair-parramatta` [DONE (live)]
- BR-LG: `/lg-fridge-repair` [DONE (live)]
- COMM-FRIDGE: `/commercial-refrigeration-repair` [DONE 16 Oct; schema in claude/schemas/]
- COOLROOM: `/coolroom-repair` [DONE 16 Oct; schema in claude/schemas/]
- COMM-FREEZER: `/commercial-freezer-repair` [DONE 16 Oct; schema in claude/schemas/]
- ICE: `/ice-machine-repair` [DONE 19 Oct; schema in claude/schemas/]
- SEAL: `/fridge-door-seal-replacement` [DONE 19 Oct; schema in claude/schemas/]
- FREEZER: `/freezer-repair` [DONE 20 Oct; schema in claude/schemas/]
- COMPRESSOR: `/fridge-compressor-repair` [DONE 20 Oct; schema in claude/schemas/]
- AREAS: `/areas` [DONE 20 Oct; schema in claude/schemas/]
- LOC-CBD: `/fridge-repairs-parramatta` [DONE 20 Oct; schema in claude/schemas/]

## Live pages that still need the sheet's title/meta/H1 optimisation (later phase)

- HOME: `/`
- SERV-HUB: `/services`
- NOTCOOL: `/fridge-not-cooling-repair`
- REGAS: `/fridge-regas`
- COST: `/fridge-repair-cost`
- EMERG: `/emergency-fridge-repair`
- BRANDS: `/brands`
- B-NOTCOOL: `/blog/fridge-not-cooling-causes`
- B-SUMMER: `/blog/summer-fridge-maintenance-tips`

## Log
- 14 Oct 2026: /fridge-regas built.
- 15 Oct 2026: /samsung-fridge-repair-parramatta and /lg-fridge-repair built from user-supplied HTML.
- 16 Oct 2026: keyword sheet saved to claude/. Built COMM-FRIDGE (/commercial-refrigeration-repair). Competitor sites could not be fetched (network block), used sheet benchmarks only. Linked from header/footer "Commercial Fridge Repair", services, cost, emergency pages. Spoke links (coolroom, freezer, ice) are plain text until those pages exist: when each spoke is built, link it from COMM-FRIDGE (equipment cards, FAQ 8) and the footer.
- 16 Oct 2026: Built COOLROOM (/coolroom-repair). Owner confirmed the page did not exist on the live site. Coolroom installation NOT claimed (unconfirmed). Linked from header/footer, services, cost, emergency, and the COMM-FRIDGE hub.
- RULE: before building any page, check the live site if the network allows (sandbox could not reach fridgerepairparramatta.com.au on 16 Oct); otherwise ask the owner to confirm the page does not already exist.
- 16 Oct 2026: Built COMM-FREEZER (/commercial-freezer-repair). Owner confirmed it did not exist live. Linked from COMM-FRIDGE hub (upright card) and COOLROOM related list.
- BRANCHES: all new work goes on `claude/new-pages-seo-oct16` (PR #8 to main). Do NOT push to `claude/site-layout-review-knuu9t` (PR #7, owner wants it left alone).
- 19 Oct 2026: Built ICE (/ice-machine-repair) on branch `claude/ice-machine-page` (owner confirmed 404 on live site). Linked from COMM-FRIDGE hub, footer/header "Ice Machine Repair" and services card. PR #8 and #9 are merged; `claude/new-pages-seo-oct16` is finished, use a fresh branch from `main` per page.
- 19 Oct 2026: Built SEAL (/fridge-door-seal-replacement) on branch `claude/door-seal-page` (owner confirmed 404 live). Prices follow the cost page ($120-$300 seal, $60-$200 call-out). Linked from services, cost, fridge-not-cooling pages.
- 20 Oct 2026: Built FREEZER (/freezer-repair) on branch `claude/freezer-repair-page`, stacked on `claude/door-seal-page` because PR #11 was not merged yet (merge #11 first). Owner confirmed 404 live. Header/footer "Freezer Repair" links now point to it.
- Next: BR-WESTINGHOUSE (/westinghouse-fridge-repair).
- 20 Oct 2026: Saved claude/seo-playbook.md. Build order changed to follow its B11/A9 priorities (compressor, areas hub and nearby suburb pages, then brands and blogs). LOC-BLACKTOWN dropped.
- 20 Oct 2026 (owner decision): the playbook is reference only. Do not change reviews, ratings or banners on existing pages and make no other site changes because of it. Only the build order and CLAUDE.md notes were updated.
- 20 Oct 2026: Built COMPRESSOR (/fridge-compressor-repair) on branch `claude/compressor-page` (owner confirmed 404 live). PR #11 and #12 are merged. Next: AREAS (/areas).
- 20 Oct 2026: Built AREAS (/areas) on branch `claude/areas-hub-page` (owner confirmed 404 live). Lists 28 suburbs as plain text (Blacktown and Seven Hills left out on purpose). When each suburb page is built, turn that suburb chip on /areas into a link and add it to the footer. Footer "Areas We Serve" heading and a homepage line now link to /areas. Next: LOC-CBD (/fridge-repairs-parramatta).
- 20 Oct 2026: Built LOC-CBD (/fridge-repairs-parramatta) on branch `claude/parramatta-suburb-page` (owner confirmed 404 live). Uses only local facts already on the homepage (Church St, Parramatta Square, Westfield Parramatta, Harris Park, CBD apartments). The Parramatta chip on /areas and the first footer suburb now link to it. Suburb page recipe: hero with form, short answer, services grid, homes/apartments cards, businesses cards, fault table with price, price table, booking steps, brands, nearby suburbs, FAQs. Next: LOC-WESTMEAD (/fridge-repair-westmead): write fresh, do not copy-swap the Parramatta text; link its chip on /areas and the footer.
- 20 Oct 2026: Rewrote the Samsung and LG pages (owner asked) to remove duplicate copy: overlap between them fell from 55% to 16%. Different section order, new FAQ sets (schema updated to match), brand-specific extra sections (Samsung ice maker table, LG door and seal table). Title, meta, H1 and URL unchanged. For future brand pages (Westinghouse, Fisher & Paykel): write from scratch with their own structure, never copy-swap; run a 6-word overlap check against the other brand pages before publishing.
- 21 Oct 2026: Blog URLs changed from /blog-slug to /blog/slug (owner request). .htaccess redirects old URLs, blog-post.php/blog.php/sitemap/admin/canonical updated, shared header has `<base href="/">`, internal links updated. Future blog posts: /blog/<slug>.
