"""Assemble ShopClass SVG brand assets from generated text paths."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(HERE, "paths.json")))
OUT = os.path.join(HERE, "..", "brand")
os.makedirs(os.path.join(OUT, "favicon"), exist_ok=True)

NAVY = "#0F2742"
TEAL = "#12A6A0"
OFFWHITE = "#F7F5F1"
SLATE = "#435466"
LABEL = "#8A94A0"
CORAL = "#FF6B4A"
HAIR = "#DFDAD2"


def mark(color_awning_bar, c_scallops, c_outline, c_tag, c_pin, c_bubble, uid):
    """The ShopClass mark in a 96x96 box. c_scallops is a 3-tuple."""
    s1, s2, s3 = c_scallops
    return f'''<mask id="cut-{uid}">
  <rect width="96" height="96" fill="#fff"/>
  <circle cx="71" cy="63" r="15" fill="#000"/>
  <rect x="2" y="35.5" width="36" height="21" rx="8" transform="rotate(-33 20 46)" fill="#000"/>
</mask>
<g mask="url(#cut-{uid})" fill="none" stroke="{c_outline}" stroke-width="8" stroke-linecap="round">
  <path d="M14 40 L14 74 Q14 84 24 84 L56 84"/>
  <path d="M82 32 L82 46"/>
</g>
<rect x="8" y="6" width="80" height="12" rx="4" fill="{color_awning_bar}"/>
<path d="M8 17.5 A13.33 13.33 0 0 0 34.67 17.5 Z" fill="{s1}"/>
<path d="M34.67 17.5 A13.33 13.33 0 0 0 61.33 17.5 Z" fill="{s2}"/>
<path d="M61.33 17.5 A13.33 13.33 0 0 0 88 17.5 Z" fill="{s3}"/>
<path fill-rule="evenodd" transform="rotate(-33 20 46)" fill="{c_tag}"
      d="M11.5 38.5 H28.5 Q34 38.5 34 44 V48 Q34 53.5 28.5 53.5 H11.5 Q6 53.5 6 48 V44 Q6 38.5 11.5 38.5 Z
         M13.5 46 A2.5 2.5 0 1 1 8.5 46 A2.5 2.5 0 1 1 13.5 46 Z"/>
<path fill-rule="evenodd" fill="{c_pin}"
      d="M47 40.3 C41.9 40.3 37.8 44.4 37.8 49.5 C37.8 56.5 47 66 47 66 C47 66 56.2 56.5 56.2 49.5 C56.2 44.4 52.1 40.3 47 40.3 Z
         M51 49.5 A4 4 0 1 1 43 49.5 A4 4 0 1 1 51 49.5 Z"/>
<path d="M64 71 L57.5 78.5 L68 74.5 Z" fill="{c_bubble}"/>
<path fill-rule="evenodd" fill="{c_bubble}"
      d="M82.5 63 A11.5 11.5 0 1 1 59.5 63 A11.5 11.5 0 1 1 82.5 63 Z
         M67.5 63 A2 2 0 1 1 63.5 63 A2 2 0 1 1 67.5 63 Z
         M73 63 A2 2 0 1 1 69 63 A2 2 0 1 1 73 63 Z
         M78.5 63 A2 2 0 1 1 74.5 63 A2 2 0 1 1 78.5 63 Z"/>'''


def color_mark(uid):
    return mark(NAVY, (NAVY, TEAL, TEAL), NAVY, NAVY, TEAL, TEAL, uid)


def mono_mark(uid, color=TEAL):
    return mark(color, (color, color, color), color, color, color, color, uid)


def svg(name, viewbox, body):
    w, h = viewbox.split()[2:4]
    doc = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" '
           f'width="{w}" height="{h}" role="img" aria-label="ShopClass">\n{body}\n</svg>\n')
    open(os.path.join(OUT, name), "w").write(doc)
    print(name, len(doc), "bytes")


def text(pid, x, y, size, fill):
    s = size / 100.0
    return (f'<path transform="translate({x} {y}) scale({s})" fill="{fill}" '
            f'd="{P[pid]["d"]}"/>')


def tw(pid, size):
    return P[pid]["width"] * size / 100.0


# ---------------------------------------------------------------- icon
svg("shopclass-icon.svg", "0 0 96 96", color_mark("i"))

# ---------------------------------------------------------------- favicon
fav = f'''<rect width="96" height="96" rx="21" fill="{NAVY}"/>
<g transform="translate(14.4 14.4) scale(0.7)">
{mono_mark("f")}
</g>'''
svg(os.path.join("favicon", "shopclass-favicon.svg"), "0 0 96 96", fav)

# ---------------------------------------------------------------- primary logo
ts = 92  # text size
shop_w = tw("shop", ts)
gap = 28
x0 = 96 + gap
baseline = 93
total = x0 + shop_w + tw("class", ts)
body = f'''<g transform="translate(0 12)">
{color_mark("l")}
</g>
{text("shop", x0, baseline, ts, NAVY)}
{text("class", x0 + shop_w, baseline, ts, TEAL)}'''
svg("shopclass-logo.svg", f"0 0 {round(total + 4)} 120", body)

# ---------------------------------------------------------------- compact logo
ts2 = 64
shop_w2 = tw("shop", ts2)
x2 = 72 + 21
base2 = 67
total2 = x2 + shop_w2 + tw("class", ts2)
body = f'''<g transform="translate(0 8) scale(0.75)">
{color_mark("c")}
</g>
{text("shop", x2, base2, ts2, NAVY)}
{text("class", x2 + shop_w2, base2, ts2, TEAL)}'''
svg("shopclass-logo-compact.svg", f"0 0 {round(total2 + 3)} 88", body)

# ---------------------------------------------------------------- monochrome (all-navy) variants
svg("shopclass-icon-mono.svg", "0 0 96 96", mono_mark("im", NAVY))

body = f'''<g transform="translate(0 12)">
{mono_mark("lm", NAVY)}
</g>
{text("shop", x0, baseline, ts, NAVY)}
{text("class", x0 + shop_w, baseline, ts, NAVY)}'''
svg("shopclass-logo-mono.svg", f"0 0 {round(total + 4)} 120", body)

body = f'''<g transform="translate(0 8) scale(0.75)">
{mono_mark("cm", NAVY)}
</g>
{text("shop", x2, base2, ts2, NAVY)}
{text("class", x2 + shop_w2, base2, ts2, NAVY)}'''
svg("shopclass-logo-compact-mono.svg", f"0 0 {round(total2 + 3)} 88", body)

# ---------------------------------------------------------------- board 1920x1080
E = []
E.append(f'<rect width="1920" height="1080" fill="{OFFWHITE}"/>')
E.append(f'<line x1="1005" y1="60" x2="1005" y2="1020" stroke="{HAIR}" stroke-width="2"/>')
E.append(f'<line x1="70" y1="556" x2="940" y2="556" stroke="{HAIR}" stroke-width="2"/>')
E.append(f'<line x1="1070" y1="556" x2="1850" y2="556" stroke="{HAIR}" stroke-width="2"/>')

# top-left: primary logo, scaled to ~740 wide, centered in 0..1005
scale = 740.0 / total
lw, lh = total * scale, 120 * scale
lx, ly = (1005 - lw) / 2, 190
E.append(f'<g transform="translate({lx:.1f} {ly}) scale({scale:.4f})">')
E.append(f'<g transform="translate(0 12)">{color_mark("b1")}</g>')
E.append(text("shop", x0, baseline, ts, NAVY))
E.append(text("class", x0 + shop_w, baseline, ts, TEAL))
E.append('</g>')
lab = 19
E.append(text("lbl_primary", 502.5 - tw("lbl_primary", lab) / 2, 505, lab, LABEL))

# top-right: compact logo scaled to ~560 wide, centered in 1005..1920
scale2 = 560.0 / total2
cw = total2 * scale2
cx0, cy0 = 1005 + (915 - cw) / 2, 230
E.append(f'<g transform="translate({cx0:.1f} {cy0}) scale({scale2:.4f})">')
E.append(f'<g transform="translate(0 8) scale(0.75)">{color_mark("b2")}</g>')
E.append(text("shop", x2, base2, ts2, NAVY))
E.append(text("class", x2 + shop_w2, base2, ts2, TEAL))
E.append('</g>')
E.append(text("lbl_short", 1462.5 - tw("lbl_short", lab) / 2, 505, lab, LABEL))

# bottom-left: favicon 300px centered, size labels, section label
fs = 300.0 / 96
fx, fy = 502.5 - 150, 630
E.append(f'<g transform="translate({fx:.1f} {fy}) scale({fs:.4f})">')
E.append(f'<rect width="96" height="96" rx="21" fill="{NAVY}"/>')
E.append(f'<g transform="translate(14.4 14.4) scale(0.7)">{mono_mark("b3")}</g>')
E.append('</g>')
pxs = 24
px_gap = 60
px_total = tw("px16", pxs) + tw("px32", pxs) + tw("px48", pxs) + 2 * px_gap
pxx = 502.5 - px_total / 2
E.append(text("px16", pxx, 992, pxs, NAVY))
pxx += tw("px16", pxs) + px_gap
E.append(text("px32", pxx, 992, pxs, NAVY))
pxx += tw("px32", pxs) + px_gap
E.append(text("px48", pxx, 992, pxs, NAVY))
E.append(text("lbl_favicon", 502.5 - tw("lbl_favicon", lab) / 2, 1048, lab, LABEL))

# bottom-right: typography specimen
tx = 1090
E.append(text("spec_h_label", tx, 668, 30, LABEL))
E.append(text("spec_heading", tx, 748, 62, NAVY))
E.append(text("spec_chars", tx, 820, 52, NAVY))
E.append(text("spec_b_label", tx, 912, 30, LABEL))
E.append(text("spec_body", tx, 972, 39, SLATE))
E.append(text("lbl_typo", tx, 1048, lab, LABEL))
E.append(f'<circle cx="1866" cy="1040" r="11" fill="{CORAL}"/>')

svg("shopclass-board.svg", "0 0 1920 1080", "\n".join(E))
print("done ->", OUT)
