# WhoBuilt — Project Context for Claude Code

## Project Configuration

- **Language**: TypeScript
- **Package Manager**: pnpm
- **Add-ons**: prettier, eslint, vitest, playwright, tailwindcss, sveltekit-adapter, devtools-json, drizzle, better-auth, paraglide, storybook, mcp

---

You are able to use the Svelte MCP server, where you have access to comprehensive Svelte 5 and SvelteKit documentation. Here's how to use the available tools effectively:

## Available MCP Tools:

### 1. list-sections

Use this FIRST to discover all available documentation sections. Returns a structured list with titles, use_cases, and paths.
When asked about Svelte or SvelteKit topics, ALWAYS use this tool at the start of the chat to find relevant sections.

### 2. get-documentation

Retrieves full documentation content for specific sections. Accepts single or multiple sections.
After calling the list-sections tool, you MUST analyze the returned documentation sections (especially the use_cases field) and then use the get-documentation tool to fetch ALL documentation sections that are relevant for the user's task.

### 3. svelte-autofixer

Analyzes Svelte code and returns issues and suggestions.
You MUST use this tool whenever writing Svelte code before sending it to the user. Keep calling it until no issues or suggestions are returned.

### 4. playground-link

Generates a Svelte Playground link with the provided code.
After completing the code, ask the user if they want a playground link. Only call this tool after user confirmation and NEVER if code was written to files in their project.

## What is WhoBuilt?

WhoBuilt (whobuilt.org) is the UK's first independent quality comparison service
for new build housebuilders. It helps buyers make informed decisions by combining
verified resident reviews, HBF satisfaction data, NHBC warranty records, and
build quality scores.

The founder bought a new build flat during COVID and experienced significant
problems — both within the flat and building-wide (snagging issues post 2-year
period, lift breakdowns, render falling off exterior walls). This is the personal
motivation behind the product.

---

## Brand & Design

**Colours:**
- Primary: Sage green `#3D7A52` (dark: `#2A5A3A`, light: `#EBF4EE`, mid: `#C4DFD0`)
- Accent: Red `#E03A2F` (dark: `#B02820`, light: `#FDEEED`)
- Ink: `#1E2D24`
- Muted: `#6B7A6F`
- Border: `#D8E8DE`
- Background: `#F5FAF6`
- Card: `#FFFFFF`

**Typography:**
- Display / headings: Lora (serif, italic for emphasis)
- Body / UI: Nunito (sans-serif, weight 600–900)

**Design principles:**
- Warm and approachable, not corporate watchdog
- Rounded cards (border-radius: 16px), soft shadows
- Sage green for primary actions, red for accents and alerts
- Score badges: green ≥95%, amber 90–95%, red <90%

---

## Tech Stack

- **Framework:** SvelteKit with adapter-static (deployed to GitHub Pages)
- **Styling:** Tailwind CSS + @tailwindcss/forms + @tailwindcss/typography
- **Maps:** Leaflet.js with OpenStreetMap tiles (no API key needed)
- **Postcode lookup:** postcodes.io (free, no key needed)
- **Charts:** Chart.js
- **Email capture:** Formspree (endpoint: https://formspree.io/f/mzdjypjg)
- **Hosting:** GitHub Pages with custom domain whobuilt.org
- **Redirect:** whobuilt.uk → whobuilt.org (DNS redirect via Namecheap)

---

## Site Structure

```
src/routes/
├── +page.svelte              ← Landing page / waitlist
├── +layout.svelte            ← Shared header, footer, nav
├── map/
│   └── +page.svelte          ← Postcode search + Leaflet map prototype
├── data/
│   └── +page.svelte          ← HBF satisfaction chart (Chart.js, 19 quarters)
├── builders/
│   ├── +page.svelte          ← All builders index
│   └── [slug]/
│       └── +page.svelte      ← Individual builder profile (SEO target)
├── methodology/
│   └── +page.svelte          ← How scores are calculated
└── about/
    └── +page.svelte          ← Founder story
```

---

## Data

### HBF Satisfaction Scores (Q1 2021 – Q3 2025)

Source: Home Builders Federation Customer Satisfaction Survey
Key question: "Would you recommend your builder to a friend?"
Note: Survey sent 8 weeks post-completion — scores are flattering (honeymoon effect).
NHBC 9-month scores run 5–10% lower.

| Builder | Avg Score | Trend |
|---|---|---|
| Bloor Homes | 96.4% | Stable |
| CALA Homes | 95.0% | Stable |
| Berkeley Group | 95.8% | Stable |
| Barratt Developments | 94.2% | Stable |
| Bellway Homes | 93.5% | Stable |
| Vistry Group | 93.1% | Improving |
| Miller Homes | 92.7% | Stable |
| Persimmon Homes | 92.8% | Recovering (dipped to 81.4% Q3 2022) |
| Taylor Wimpey | 92.6% | Improving |
| Keepmoat | 92.1% | Stable |
| Bovis Homes | 91.4% | Stable |
| Crest Nicholson | 90.9% | Improving (dipped to 86.5% mid-2022, recovered to 97% by 2024) |

### Planned Data Sources

- **EPC Register** (open data, gov.uk) — builder name + postcode for development locations
- **Land Registry price paid data** — new build density by area
- **NHBC warranty claims** — FOI request pending
- **Trustpilot / HomeViews** — review aggregation

---

## Pages Already Built (as standalone HTML files)

These exist as static HTML prototypes and need migrating into SvelteKit:

1. `index.html` — Landing page with waitlist form (Formspree integrated)
2. `hbf_chart.html` — Interactive HBF satisfaction chart with 3 views
   (trend over time, overall ranking, latest quarter)
3. `map.html` — Postcode search map with 50 seeded UK developments,
   colour-coded pins by score, sidebar builder cards

---

## Key Insights for Content / SEO

- "1 in 3 new build buyers report a major defect"
- "Housebuilders run their own satisfaction surveys — taken 8 weeks after completion"
- "There are zero independent comparison services for a £31bn market"
- Persimmon's Q3 2022 collapse to 81.4% is a key data story
- Crest Nicholson's recovery from 86.5% to 97% is biggest turnaround in dataset
- Bloor Homes is consistently highest rated but barely known

---

## Tone of Voice

- Honest and direct, never corporate
- Consumer advocate — firmly on the buyer's side
- Data-led but written for normal people, not analysts
- Warm, not alarmist

---

## What's Next

- [ ] Scaffold full SvelteKit app from this structure
- [ ] Migrate the three HTML prototypes into Svelte components
- [ ] Set up GitHub Actions for auto-deploy to GitHub Pages
- [ ] Build individual builder profile pages (slug routing)
- [ ] Integrate EPC register data for real development locations
- [ ] Write methodology page
- [ ] Write about page (founder story)
