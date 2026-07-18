"""Convert text strings to SVG path data using a (variable) TTF."""
import json, sys
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform


def load(path, axes):
    font = TTFont(path)
    if "fvar" in font:
        instantiateVariableFont(font, axes, inplace=True)
    return font


def text_path(font, text, size, tracking=0.0):
    """Return (path_d, width_px) for text rendered at `size` px em, baseline y=0."""
    upm = font["head"].unitsPerEm
    scale = size / upm
    glyph_set = font.getGlyphSet()
    cmap = font.getBestCmap()
    # kerning via GPOS is complex; use fontTools' otlLib? Simplest: harfbuzz not
    # available, so read 'kern' table if present (Manrope/Inter rely on GPOS).
    # Approximate: no kerning, then hand-adjust via tracking per pair if needed.
    x = 0.0
    d_parts = []
    track_units = tracking * upm / size  # tracking given in px at this size
    for ch in text:
        gname = cmap[ord(ch)]
        glyph = glyph_set[gname]
        spen = SVGPathPen(glyph_set)
        # flip y (font y-up -> svg y-down), scale, offset
        tpen = TransformPen(spen, Transform(scale, 0, 0, -scale, x * scale, 0))
        glyph.draw(tpen)
        d = spen.getCommands()
        if d:
            d_parts.append(d)
        x += glyph.width + track_units
    return " ".join(d_parts), x * scale


if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    out = {}
    for item in spec:
        font = load(item["font"], item.get("axes", {}))
        d, w = text_path(font, item["text"], item["size"], item.get("tracking", 0))
        out[item["id"]] = {"d": d, "width": round(w, 2)}
    json.dump(out, open(sys.argv[2], "w"), indent=1)
    for k, v in out.items():
        print(k, "width:", v["width"])
