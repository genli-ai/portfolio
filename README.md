# ligen-portfolio

Personal portfolio site — AI for finance, MENA.

Live URL: TBD (to be set after first GitHub Pages deploy).

## What's here

A single-page Astro + Tailwind site showcasing:

- **Case study**: Saudi Vision 2030 deep-dive — 15k words, 41 charts, end-to-end via my own AI-augmented workflow
- **Skill**: `analyst-research` — the open-source Claude skill (MIT, v0.6.0) behind the case study, with 3 user-selectable modes (light/medium/heavy)
- **Methodology**: the 8-step research skeleton, multi-LLM division of labor
- **About + Contact**

## Local dev

```bash
npm install
npm run dev      # http://localhost:4321
```

## Build

```bash
npm run build    # outputs to dist/
npm run preview  # serve dist/ locally
```

## Deploy

### Option A — GitHub Pages, project page (default)

Push to GitHub at `https://github.com/<user>/<repo>`. The workflow at `.github/workflows/deploy.yml` auto-builds with:

- `SITE=https://<user>.github.io`
- `BASE=/<repo>`

Settings → Pages → Source → "GitHub Actions". Site lives at `https://<user>.github.io/<repo>/`.

### Option B — GitHub Pages, user page (root URL)

Rename the repo to `<user>.github.io`. In `.github/workflows/deploy.yml`, remove the `BASE` env var (leave it unset) so the site builds at the root. URL becomes `https://<user>.github.io/`.

### Option C — Custom domain (e.g. ligen.dev)

1. Add a `public/CNAME` file containing your domain (e.g. `ligen.dev`).
2. In `.github/workflows/deploy.yml`, set `SITE=https://ligen.dev` and remove `BASE`.
3. Configure DNS at your registrar (ALIAS or A records — see GitHub Pages docs).

## Structure

```
src/
├── pages/index.astro          # Single-page route
├── layouts/Base.astro         # HTML scaffolding + head
├── components/                # Section components
│   ├── Nav.astro
│   ├── Hero.astro
│   ├── CaseStudy.astro        # 9 figures + 3 key findings + PDF link
│   ├── Skill.astro            # analyst-research mode-picker visualization
│   ├── Methodology.astro      # 8-step workflow + LLM division of labor
│   ├── About.astro
│   └── Contact.astro
└── styles/global.css          # Tailwind + custom palette
public/
├── figures/                   # 9 Vision 2030 chart JPGs
├── reports/                   # 7 MB PDF deliverable
└── favicon.svg, favicon.ico
```

## Color palette

Adapted from the report itself (`report_style_spec.md` McKinsey blue-grey palette):

| Token | Hex | Use |
|---|---|---|
| `--color-ink` | `#0a0e1a` | Body text, dark sections |
| `--color-paper` | `#fafaf7` | Page background |
| `--color-paper-warm` | `#f5f3ed` | Section alternates |
| `--color-brand` | `#1f3a5f` | Headlines, key numbers |
| `--color-accent` | `#c97b4c` | Highlights, links |
| `--color-muted` | `#6e7681` | Secondary text |

## Tech

- [Astro 6](https://astro.build/) — static site generator
- [Tailwind CSS v4](https://tailwindcss.com/) — utility CSS (Vite plugin, not the legacy PostCSS path)
- Static HTML output, no JS runtime needed for the site

## License

Site code: MIT. Report PDF and figures: © 2026 Ligen, all rights reserved.

---

Built with [Claude Code](https://claude.com/claude-code) and the open-source [analyst-research](https://github.com/reagan475614947/market-research-skills) workflow.
