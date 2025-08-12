# Ops Kits Engine (Starter)

A zero-cost, autopilot-friendly system that sells plug-and-play operating kits for solo service businesses.

## What this repo includes
- Static site generator (CSV → hundreds of SEO pages) via **GitHub Actions**.
- **Embeddable calculators** (HTML/JS) with a soft CTA.
- **Products database** (`/data/products.csv`) and **Industries list** (`/data/industries.csv`).
- Ready-to-upload **Sheets templates** (Excel files) and **Notion-ready Markdown templates** for the core kits.
- RSS feed for **IFTTT → Pinterest** autopinning.
- Affiliate & remix license pages.

## One-time setup (≈30–60 min)
1) Create a new GitHub repo and upload all files from this folder's ZIP.
2) Go to **Settings → Pages**: set source to `docs/` on `main` branch.
3) Enable Actions (they're on by default). The nightly workflow will publish the site to `/docs`.
4) Edit `/data/products.csv` and set your **real Gumroad URLs** (replace placeholders).
5) (Optional) In `scripts/build.py`, set `SITE_BASE` to your `https://<username>.github.io/<repo>`.
6) Connect **IFTTT**: RSS (https://<username>.github.io/<repo>/feed.xml) → Pinterest “Create Pin”.
7) Turn on **Gumroad Affiliates** at 30–40% and paste `AFFILIATES.md` copy into your listings and delivery email.

## Local build (optional)
- Requires Python 3.11+: `pip install jinja2 pandas pyyaml` then `python scripts/build.py`.
- Outputs to `/docs`.

## Files
- `/data/products.csv` — products meta with token placeholders (e.g., `{industry}`).
- `/data/industries.csv` — 120+ industries for programmatic pages.
- `/embed/calculators/*.html` — copy-to-embed widgets.
- `/scripts/build.py` — CSV → pages, index, RSS.
- `/template.html` — page layout.
- `/docs/` — site output (GitHub Pages source).

## License
Remix license included. See `REMIX_LICENSE.md`.
