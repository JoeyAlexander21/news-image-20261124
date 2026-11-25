#!/usr/bin/env python3
"""Render the 24 Nov 2026 world-news front page (1024x1024 PNG).
Local build-time script only; the shipped entry is main.ts + entry.png."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 234)
INK = (17, 17, 17)
RED = (178, 34, 34)
NAVY = (16, 42, 67)
TEAL = (0, 110, 110)
GOLD = (176, 124, 0)
GREY = (90, 90, 86)
LIGHT = (255, 255, 255)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

def f(path, s):
    return ImageFont.truetype(path, s)

def wrap(d, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def para(d, x, y, text, font, color, max_w, lh):
    for ln in wrap(d, text, font, max_w):
        d.text((x, y), ln, font=font, fill=color)
        y += lh
    return y

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 36
# outer border
d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=3)
d.rectangle([20, 20, W - 21, H - 21], outline=INK, width=1)

# ---- Masthead ----
y = 34
d.text((M, y), "THE WORLD IN ONE DAY", font=f(SERIF, 58), fill=INK)
y += 66
d.rectangle([M, y, W - M, y + 5], fill=RED)
y += 14
d.text((M, y), "TUESDAY, 24 NOVEMBER 2026", font=f(SANS_B, 30), fill=RED)
d.text((W - M - d.textlength("6 STORIES  •  ONE DAY", font=f(SANS_B, 22)), y + 8),
       "6 STORIES  •  ONE DAY", font=f(SANS_B, 22), fill=INK)
y += 46
d.rectangle([M, y, W - M, y + 2], fill=INK)

# ---- Lead story (navy box) ----
y += 12
lead_h = 200
d.rectangle([M, y, W - M, y + lead_h], fill=NAVY)
lx, ly = M + 22, y + 14
d.text((lx, ly), "LEAD STORY  •  WAR AT SEA  •  BENGHAZI, LIBYA", font=f(SANS_B, 19), fill=(255, 205, 80))
ly += 30
ly = para(d, lx, ly, "Ukraine says it sank a Russian warship in Libya",
          f(SERIF, 38), LIGHT, W - 2 * M - 44, 46)
ly += 4
ly = para(d, lx, ly,
          "President Volodymyr Zelensky said seven Ukrainian sea drones sank the corvette Merkury "
          "in Benghazi port on 22 Nov. Kyiv also says a Ka-27 helicopter was destroyed and the "
          "cargo ship Angara was hit.",
          f(SANS, 20), (225, 232, 238), W - 2 * M - 44, 25)
d.text((lx, y + lead_h - 30), "7  SEA DRONES CLAIMED   •   SHIP COMMISSIONED 2023",
       font=f(SANS_B, 20), fill=(255, 205, 80))
y += lead_h + 14

# ---- Two-column stories ----
def card(x, y, w, h, accent, kicker, headline, body, stat):
    d.rectangle([x, y, x + w, y + h], outline=INK, width=2)
    d.rectangle([x, y, x + w, y + 8], fill=accent)
    cx, cy = x + 18, y + 20
    d.text((cx, cy), kicker, font=f(SANS_B, 17), fill=accent)
    cy += 26
    cy = para(d, cx, cy, headline, f(SERIF, 26), INK, w - 36, 30)
    cy += 6
    cy = para(d, cx, cy, body, f(SANS, 17), (40, 40, 40), w - 36, 21)
    d.text((cx, y + h - 28), stat, font=f(SANS_B, 20), fill=accent)
    return y + h

col_w = (W - 2 * M - 16) // 2
row_h = 208
card(M, y, col_w, row_h, RED, "GULF  •  RIYADH",
     "Houthi drone hits Riyadh's tallest tower",
     "Saudi Civil Defence said 11 people were hurt on Tuesday in a strike on the 385 m PIF Tower "
     "\u2014 the second hit in five days.",
     "11  INJURED")
card(M + col_w + 16, y, col_w, row_h, TEAL, "MARKETS  •  WALL STREET",
     "Nvidia brings back Jensen Huang — shares soar 31%",
     "The board unanimously reinstated Huang as CEO on Mon 23 Nov, 11 days after he resigned. "
     "Shares closed at $165.05.",
     "+31%  •  $165.05  •  ~$950 BN ADDED")
y += row_h + 14

card(M, y, col_w, row_h, GOLD, "SPORT  •  LAUSANNE",
     "Senegal get their Africa Cup title back",
     "The Court of Arbitration for Sport ruled unanimously on Tue 24 Nov that Senegal's 1\u20130 "
     "extra-time win over Morocco stands.",
     "1–0  •  UNANIMOUS RULING")
card(M + col_w + 16, y, col_w, row_h, RED, "GAZA  •  GAZA CITY",
     "Israeli strike kills Hamas security chief",
     "Naeem Abu Nahel, 50, director of Hamas's internal security, was killed in western Gaza City "
     "on Tue 24 Nov. Six others also died.",
     "7  KILLED IN TUESDAY'S STRIKES")
y += row_h + 14

# ---- Bottom strip: two mini stories ----
strip_h = 112
d.rectangle([M, y, W - M, y + strip_h], outline=INK, width=2)
d.rectangle([M, y, W - M, y + 8], fill=INK)
sy = y + 20
d.text((M + 18, sy), "ALSO ON 24 NOVEMBER", font=f(SANS_B, 17), fill=RED)
sy += 26
half = (W - 2 * M - 36) // 2
sy1 = para(d, M + 18, sy, "ZAPORIZHZHIA \u2014 Overnight Russian strike kills 2, wounds 40, "
          "including four children, the governor says.",
          f(SANS, 17), INK, half, 22)
para(d, M + 18 + half + 18, sy, "CLIMATE \u2014 After COP31 ended on 22 Nov with no deal, the EU says "
     "it will seek an overhaul of UN climate talks.",
     f(SANS, 17), INK, half, 22)
y += strip_h + 12

# ---- Footer ----
d.rectangle([M, y, W - M, y + 2], fill=INK)
y += 10
para(d, M, y,
     "Sources: Reuters, BBC, AP, Court of Arbitration for Sport, Nvidia, Saudi Civil Defence — reports of 24 Nov 2026. "
     "Casualty figures as reported; some tolls are disputed.",
     f(SANS, 15), GREY, W - 2 * M, 20)

img.save("/home/hatch/workspace/makefun/news-image-20261124/entry.png", optimize=True)
print("saved")
