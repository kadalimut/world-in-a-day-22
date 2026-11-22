#!/usr/bin/env python3
"""Draw the news-image-20261122 entry: a newspaper front page for
Sunday 22 November 2026, 1024x1024 PNG, deterministic (no network,
no timestamps, fixed colours and text). Run: python3 tools/draw_image.py
Writes entry.png next to the repository root.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 232)
INK = (20, 20, 28)
NAVY = (20, 33, 61)
RED = (178, 34, 34)
TEAL = (0, 110, 110)
GOLD = (176, 141, 45)
GREY = (90, 90, 96)
WHITE = (255, 255, 255)
CARD = (255, 255, 255)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap by measured pixel width."""
    lines = []
    for word in text.split(" "):
        if lines and draw.textlength(lines[-1] + " " + word, font=fnt) <= max_width:
            lines[-1] += " " + word
        elif draw.textlength(word, font=fnt) <= max_width:
            lines.append(word)
        else:
            lines.append(word)
    return lines


STORIES = [
    ("CLIMATE", "COP31 IN OVERTIME", RED,
     "Climate talks in Antalya run into a second day of overtime. The draft deal drops any call to phase out fossil fuels.",
     "ANTALYA, TURKEY"),
    ("MEXICO", "CARTEL BOSS CAPTURED", NAVY,
     "Mexican forces capture Fausto Isidro Meza Flores, 'El Chapo Isidro', in Sinaloa. Eleven people are killed in the raid.",
     "SINALOA, MEXICO"),
    ("MIDDLE EAST", "IRAN STRIKES BAHRAIN", RED,
     "Bahrain says Iran hit a civilian industrial site. Two tankers are targeted near the Strait of Hormuz.",
     "BAHRAIN / HORMUZ"),
    ("UKRAINE", "MISSILE HITS HOMETOWN", NAVY,
     "A Russian missile strikes Kryvyi Rih, President Zelenskyy's hometown, killing two people and wounding dozens.",
     "KRYVYI RIH, UKRAINE"),
    ("MARKETS", "AI SELL-OFF", TEAL,
     "US stocks fall into correction as artificial-intelligence shares slide sharply, dragging world markets down.",
     "NEW YORK, USA"),
    ("DISASTER", "PERU EARTHQUAKE", TEAL,
     "A magnitude 6.7 earthquake shakes Peru's Andes, rattling towns across the mountain region.",
     "PERU"),
]


def draw_icon(draw, kind, x, y, s, colour):
    """Simple pictogram in a coloured square."""
    draw.rounded_rectangle([x, y, x + s, y + s], radius=8, fill=colour)
    cx, cy = x + s // 2, y + s // 2
    if kind == "CLIMATE":
        draw.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], outline=WHITE, width=5)
        draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=WHITE)
    elif kind == "MEXICO":
        draw.polygon([(cx, cy - 24), (cx + 20, cy + 14), (cx - 20, cy + 14)], outline=WHITE, width=5)
        draw.line([cx - 14, cy + 18, cx + 14, cy + 18], fill=WHITE, width=5)
    elif kind == "MIDDLE EAST":
        draw.polygon([(cx - 20, cy - 6), (cx, cy - 24), (cx + 20, cy - 6), (cx, cy + 6)], outline=WHITE, width=4)
        draw.line([cx, cy + 6, cx, cy + 24], fill=WHITE, width=5)
    elif kind == "UKRAINE":
        draw.rectangle([cx - 20, cy - 20, cx + 20, cy + 20], outline=WHITE, width=5)
        draw.line([cx - 20, cy, cx + 20, cy], fill=WHITE, width=5)
        draw.line([cx, cy - 20, cx, cy + 20], fill=WHITE, width=5)
    elif kind == "MARKETS":
        pts = [(cx - 22, cy + 14), (cx - 8, cy - 2), (cx + 4, cy + 8), (cx + 22, cy - 16)]
        draw.line(pts, fill=WHITE, width=6, joint="curve")
        draw.polygon([(cx + 22, cy - 16), (cx + 10, cy - 16), (cx + 22, cy - 4)], fill=WHITE)
    else:
        draw.arc([cx - 20, cy - 14, cx + 20, cy + 14], 180, 360, fill=WHITE, width=5)
        draw.line([cx - 24, cy + 14, cx + 24, cy + 14], fill=WHITE, width=5)
        draw.line([cx - 12, cy + 14, cx - 12, cy + 24], fill=WHITE, width=4)
        draw.line([cx + 12, cy + 14, cx + 12, cy + 24], fill=WHITE, width=4)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # Masthead
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.text((512, 28), "THE WORLD IN ONE DAY", font=font(SERIF, 58),
           fill=WHITE, anchor="ma")
    d.text((512, 96), "Sunday, 22 November 2026  •  Six stories from around the world",
           font=font(SANS, 24), fill=(220, 220, 220), anchor="ma")
    d.rectangle([0, 148, W, 154], fill=GOLD)
    # Six story cards: 2 columns x 3 rows
    margin, gap = 28, 20
    cw = (W - 2 * margin - gap) // 2
    ch = 236
    top = 172
    for i, (tag, head, colour, body, place) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = margin + col * (cw + gap)
        y = top + row * (ch + gap)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=10, fill=CARD,
                            outline=(200, 195, 180), width=2)
        draw_icon(d, tag, x + 18, y + 18, 64, colour)
        d.text((x + 96, y + 20), tag, font=font(SANS, 20), fill=colour)
        d.text((x + 96, y + 46), place, font=font(SANS_R, 17), fill=GREY)
        lines = wrap(d, head, font(SANS, 28), cw - 36)
        yy = y + 96
        for line in lines[:2]:
            d.text((x + 18, yy), line, font=font(SANS, 28), fill=INK)
            yy += 34
        blines = wrap(d, body, font(SANS_R, 20), cw - 36)
        yy += 4
        for line in blines[:3]:
            d.text((x + 18, yy), line, font=font(SANS_R, 20), fill=(50, 50, 58))
            yy += 26
    # Footer strip: two briefs
    fy = top + 3 * ch + 2 * gap + 6
    d.rectangle([margin, fy, W - margin, fy + 62], fill=NAVY)
    d.text((margin + 16, fy + 8), "ALSO TODAY",
           font=font(SANS, 19), fill=GOLD)
    d.text((margin + 16, fy + 32),
           "Trump, Xi and Putin meet in Shenzhen on nuclear risk  •  Factory fire in Indonesia: 3 dead, 36 missing",
           font=font(SANS_R, 18), fill=WHITE)
    d.text((512, 1008), "All stories reported on 22 November 2026  •  make.fun news-image-20261122",
           font=font(SANS_R, 16), fill=GREY, anchor="ma")
    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
