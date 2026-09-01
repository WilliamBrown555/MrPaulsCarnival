# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

*(Primary medium today is print — menu cards and tri-folds produced by the in-vault PDF pipeline. `web` records the platform for any future digital surface; no website exists yet.)*

## Users

Primarily **regulars** — neighborhood guests who come back. The room splits roughly evenly between a **beer & shot bar crowd** and guests there for the **whimsical cocktails**; both are first-class audiences, and neither should be designed away. Secondary traffic: guests connected to the wider Mr. Paul's world (Supper Club, cocktail classes). *(User-confirmed 2026-08-18.)*

## Product Purpose

Carnival Bar is a neighborhood bar in Edina, MN with a carnival-spectacle streak: theatrical house cocktails (nitro pours, color-changing serves, cotton candy, popcorn buckets) and a NOLA-leaning kitchen (boudin, étouffée, po' boys), alongside honest cheap beer (Montucky, Highlife Pony, Coors Banquet). Success is regulars treating it as theirs — not a one-visit Instagram destination.

## Positioning

A **regulars' bar that happens to do spectacle**, not a spectacle bar chasing tourists. The signature contrast: playful carnival content (Giggle Water, Circus Peanut Fizz, balloon dog, waving elephants) presented with restrained French-bistro polish (Pinyon Script, Newsreader, aubergine ink, double-rule flourishes). **Shaved Ice Cocktails are the star of the show — and deliberately under-merchandised.** Regulars already know; the menu should not spotlight them. Word-of-mouth and the room carry the signature. *(User-confirmed 2026-08-18.)*

## Operating Context

- Location: 3917 Market St, Edina MN. Hours: Thursday–Saturday, 4pm–10pm. Instagram: @CarnivalBarMN.
- Soundtrack is part of the identity: **hip hop, 1988–2003**. A Spotify playlist QR is printed on the tri-fold (`open.spotify.com/playlist/3nm1hXH4bRCMHxpv64I1l6`).
- Menus are read in a dim bar room; legibility floors matter (established minimum ~9.3pt ingredients type on cards).
- Part of the Mr. Paul's family (Supper Club, Apothecary Bar, cocktail class series); shares an operator and service sensibility but keeps its own identity.
- Menu production is code-driven: `menu_engine.py` / `build_all.py` / `trifold2.py` / `backs.py` in the session outputs rebuild all six PDFs from structured menu data.

## Capabilities and Constraints

- **Fonts are ASCII-only embedded subsets** (Pinyon Script, Newsreader SemiBold/Italic). Accented characters (é, É, ñ), curly apostrophes, and italic en dashes are synthesized as composed glyphs by the pipeline; any new special character needs the same treatment.
- Card format: 4.25×11in two-up on letter; tri-folds in tabloid (100% scale) and legal/letter (77.3%). Roll fold, two-sided, short-edge flip.
- **Tri-fold roles (decided 2026-08-19):** tabloid is the only table version; legal/letter print below the dim-room legibility floor (~7.2pt effective ingredients) and are takeaway-only — filenames carry "Takeaway". Prices print #3d3d3d for the dim room.
- Compliance carried on menus: FDA raw/undercooked advisory (asterisk convention — `*` points to the advisory), 3% credit-card fee notice. Quail Flip contains raw quail egg; menu lists Cognac and Genepy while build sheets say Korbel and Izarra — **unresolved discrepancy, do not print new runs without confirming**.
- Menu items marked "(limited availability)": Bees Wax, Quail Flip.
- Undecided: no website, no confirmed digital surface, no balloon dog artwork in the vault.

## Brand Commitments

- **Mascots:** the elephant (three vector variants: martini, fork, bottle — traced and stored in the pipeline) and the **Balloon Dog** *(user-confirmed; no vault artwork exists yet — must be sourced or drawn, not fabricated as if canonical)*.
- **Type:** Pinyon Script for display, Newsreader SemiBold for items, Newsreader Italic for descriptions.
- **Color:** near-black `#1a1a1a` body, price gray `#5c5c5c`, brand aubergine `#392733`, pattern/accent mauve `#89696e` (sampled from the operator's own test prints).
- **Voice:** playful names, terse ingredient lists, house coinages ("Shrettuce") — carnival content, bistro delivery.
- Era cue: golden-age hip hop (1988–2003) is a binding part of the atmosphere, not decoration.

## Evidence on Hand

- Six production PDFs in `Efforts/Mr. Pauls/Carnival Bar/` (three cards with patterned backs, three tri-fold sizes).
- Build notes: `Carnival Bar Cocktail Builds.md`, `Carnival Bar V2 Cocktail Builds.md`, `Carnival Bar Cocktails.md` (source copy; contains unmenued builds: Voodoo Daiquiri, Bluest Hawaii, UnderTow, Smoked À La Louisiane, Grasshopper, Alamagoozlum, Shaved Ice #1 "Saturn").
- Brand artwork: elephant pattern test prints (red `#962c2a`, mauve `#89696e`), original logo bitmap in the wine menu PDF, traced vector variants in the pipeline.
- **Absent — do not fabricate:** balloon dog artwork, testimonials, press, photography of the room or drinks.

## Product Principles

1. **Regulars outrank tourists.** Design for the person on their fortieth visit; the spectacle should still work for them.
2. **Both crowds are real.** The beer-and-shot guest and the cotton-candy guest read the same menu; neither is an afterthought.
3. **Carnival content, bistro restraint.** The tension is the brand — never resolve it by making the design louder or the drinks plainer.
4. **The star doesn't shout.** Shaved ice is the signature precisely because the menu doesn't sell it — regulars pass it on. Future surfaces keep that restraint.
5. **Print truth is code truth.** The PDFs are built from structured data; changes go through the pipeline so spacing, accents, and compliance never drift.
