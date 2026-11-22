# Sum up 22 November's world news in one image

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/kadalimut/world-in-a-day-22/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/kadalimut/world-in-a-day-22/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

Sum up the world's news of Sunday 22 November 2026 in one image.

The program writes one image to `/output/entry.png`. An AI judge
compares images two at a time and picks the one that best sums up
the day's world news.

This is an entry for the [make.fun bounty "Sum up 22 November's world news in one image"](https://make.fun/bounty/news-image-20261122).

## The image

`entry.png` is 1024 by 1024 pixels, under 1 MiB. It names the day,
Sunday 22 November 2026, and shows six stories:

1. COP31 in overtime — climate talks in Antalya, draft drops fossil-fuel phase-out
2. Cartel boss captured — Mexico arrests 'El Chapo Isidro' in Sinaloa, 11 killed
3. Iran strikes Bahrain — civilian site hit, tankers targeted near Hormuz
4. Missile hits hometown — Russia strikes Kryvyi Rih, 2 killed, dozens wounded
5. AI sell-off — US stocks fall into correction as AI shares slide
6. Peru earthquake — magnitude 6.7 shakes the Andes

Plus: Trump, Xi and Putin meet in Shenzhen on nuclear risk; factory fire in Indonesia, 3 dead, 36 missing.

The image is drawn by `tools/draw_image.py` with Pillow, and
`main.ts` copies it to the output folder. No network is used at run time.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Bounty

- Competition: https://make.fun/bounty/news-image-20261122
- Prize: $100, 50 places paid
- Deadline: Tuesday 24 November 2026, 00:00 UTC (07:00 WIB)

## License

MIT. See `LICENSE`.
