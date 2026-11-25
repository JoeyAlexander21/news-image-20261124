[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/JoeyAlexander21/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/JoeyAlexander21/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entry for the [make.fun bounty "Sum up 24 November 2026's world news in one image"](https://make.fun/bounty/news-image-20261124) — $100 shared by the top 50 entries.

# The World in One Day — Tuesday, 24 November 2026

Entry for make.fun bounty `news-image-20261124` — sum up 24 November 2026's
world news in one image. Prize $100 shared by the top 50 entries; deadline
26 Nov 2026 00:00 UTC (07:00 WIB). Built by Jawa (Muse) for Alexander
(@joey-alexander21). **Not submitted** — this folder is the local entry only.

## The image

`entry.png` — 1024×1024 PNG, ~153 KB (limit: 1 MiB, 1024×1024). A newspaper
front page: masthead with the date in large red type, a lead story, four
stories in a 2×2 grid, and an "Also on 24 November" strip — 6 stories in all,
each with a headline, 1–2 sentences, and a key number. It was drawn with
code (`build_image.py`, Pillow + Liberation fonts) rather than an image
generator, so every word and number is exactly as written and was checked
visually, twice.

## Stories chosen (all verified in news reports of 24 Nov 2026)

1. **Lead — Ukraine says it sank a Russian warship in Libya.** President
   Volodymyr Zelensky said seven Ukrainian sea drones sank the corvette
   *Merkury* in Benghazi port on 22 Nov; Kyiv also says a Ka-27 helicopter
   was destroyed and the cargo ship *Angara* was hit. The claim and its
   fallout (Libya seeking a probe, Italy raising concern) dominated 24 Nov
   coverage. Sources: Reuters via The Independent / Kyiv Independent;
   Strategic Lens Defence fact-check (24 Nov update).
   The attack itself was 22 Nov and the claim 23 Nov — the image says so
   ("on 22 Nov") and does not present it as happening on the 24th.
2. **Houthi drone hits Riyadh's tallest tower — 11 injured.** Saudi Civil
   Defence, 24 Nov: a strike on the 385 m PIF Tower (Public Investment Fund
   HQ), the second hit in five days (the 19 Nov strike injured no one).
   Source: Reuters, 24 Nov 2026.
3. **Nvidia brings back Jensen Huang — shares soar 31%.** The board
   unanimously reinstated Huang as CEO on Mon 23 Nov, 11 days after he
   resigned; shares closed at $165.05, adding about $950 bn in one day —
   the market reaction reported on Tue 24 Nov. Sources: Nvidia statement;
   Yahoo Finance / Reuters / Admiral Markets.
4. **Senegal get their Africa Cup title back.** The Court of Arbitration for
   Sport ruled unanimously on Tue 24 Nov that Senegal's 1–0 extra-time win
   over Morocco (Jan 2026 final) stands; Morocco plans to appeal.
   Sources: CAS statement via Reuters / BBC, 24 Nov 2026.
5. **Israeli strike kills Hamas security chief.** Naeem Abu Nahel, 50,
   director of Hamas's internal security, killed in western Gaza City on
   Tue 24 Nov; medics said six others died, including two police officers.
   Sources: Reuters / BBC, 24 Nov 2026.
6. **Also: Zaporizhzhia + COP31 fallout.** Overnight Russian strike on
   Zaporizhzhia kills 2, wounds 40 including four children (regional
   governor Mykhailo Semikin, via Reuters, 24 Nov). After COP31 ended on
   22 Nov with no deal, the EU said it will seek an overhaul of UN climate
   talks (OilPrice / Reuters, 24 Nov).

Deliberately left out: COP31's collapse itself (it ended Sun 22 Nov, not
24 Nov) and the Merkury death toll (reports conflicted on 24 Nov — Al
Jazeera reported deaths, Reuters/AP reported 10 injured — so the image
gives no death toll for that story).

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
# in the grader: node main.ts                          # writes /output/entry.png
```

`main.ts` (Node 22, standard library only) just copies `entry.png` to
`/output/entry.png`. No network at runtime; running it twice produces
byte-identical output (verified — same SHA-256 both runs).

To re-render the image from scratch: `python3 build_image.py` (build-time
only, needs Pillow and the Liberation/DejaVu fonts; not used at runtime).

## What is still missing to submit

- A public GitHub repo under Alexander's own account containing `main.ts`,
  `entry.png`, `LICENSE`, `README.md` (and `build_image.py`), created after
  the competition opened, pushed to a commit — then submit its URL + commit
  SHA on make.fun before 26 Nov 2026 00:00 UTC.
- The transcript bundle: `node cli/makefun.mjs bundle` from the kit
  (the kit was downloaded and read, then removed from this folder to keep
  the repo clean). The bundle must cover **this session and its parent
  session** (the orchestrator session that handed this task to the subagent),
  plus the system prompt / instruction files. This subagent session is the
  one that built the entry; whether the bundle can be made from it depends
  on the parent agent running the kit CLI, which can discover this session
  and its parent — the subagent itself cannot submit or bundle.
