#!/usr/bin/env python3
"""Build the WME icon sheet PNG from all SVG icons."""
import os, io
from PIL import Image, ImageDraw, ImageFont
import cairosvg

REPO      = "/home/pablo/Documents/GitHub/PabloTrujilloArtunduaga"
ICON_SIZE = 64
PADDING   = 12
LABEL_H   = 14
COLS      = 6
BG_COLOR  = (8, 5, 13, 255)
BORDER_COL= (155,100,246,255)
TEXT_COL  = (232,221,247,255)
SEP_COL   = (105, 64,167,120)

DESKTOP_ICONS = [
    ("documents",  "desktop/documents.svg"),
    ("oneshot",    "desktop/oneshot.svg"),
    ("customize",  "desktop/customize.svg"),
    ("help",       "desktop/help.svg"),
    ("wallpapers", "desktop/wallpapers.svg"),
    ("themes",     "desktop/themes.svg"),
    ("music-box",  "desktop/music-box.svg"),
    ("gallery",    "desktop/gallery.svg"),
    ("friends",    "desktop/friends.svg"),
    ("badges",     "desktop/badges.svg"),
    ("controls",   "desktop/controls.svg"),
    ("exit",       "desktop/exit.svg"),
]
WINDOW_ICONS = [
    ("minimize",  "window/minimize.svg"),
    ("maximize",  "window/maximize.svg"),
    ("close",     "window/close.svg"),
    ("folder",    "window/folder.svg"),
    ("document",  "window/document.svg"),
    ("image",     "window/image.svg"),
    ("settings",  "window/settings.svg"),
]

ICON_BASE = os.path.join(REPO, "assets/world-machine/icons")

def load_svg(path, size):
    png_data = cairosvg.svg2png(url=path, output_width=size, output_height=size)
    return Image.open(io.BytesIO(png_data)).convert("RGBA")

def build_sheet(icons, cols, label=""):
    rows   = (len(icons) + cols - 1) // cols
    cell_w = ICON_SIZE + PADDING * 2
    cell_h = ICON_SIZE + PADDING * 2 + LABEL_H
    sheet_w = cell_w * cols + 2
    sheet_h = cell_h * rows + 32
    sheet = Image.new("RGBA", (sheet_w, sheet_h), BG_COLOR)
    draw  = ImageDraw.Draw(sheet)
    try:
        font_lbl = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 11)
        font_sm  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 9)
    except:
        font_lbl = font_sm = ImageFont.load_default()
    draw.text((4, 6), label, fill=TEXT_COL, font=font_lbl)
    draw.line([(0,24),(sheet_w,24)], fill=BORDER_COL, width=1)
    for i, (name, rel_path) in enumerate(icons):
        col = i % cols; row = i // cols
        x = col * cell_w + 1; y = row * cell_h + 30
        draw.rectangle([x, y, x+cell_w-1, y+cell_h-1], fill=(11,7,18,255))
        draw.rectangle([x, y, x+cell_w-1, y+cell_h-1], outline=SEP_COL, width=1)
        svg_path = os.path.join(ICON_BASE, rel_path)
        if os.path.exists(svg_path):
            try:
                icon_img = load_svg(svg_path, ICON_SIZE)
                sheet.paste(icon_img, (x+PADDING, y+PADDING), icon_img)
            except Exception as e:
                print(f"  WARN {rel_path}: {e}")
        else:
            print(f"  MISSING: {svg_path}")
        draw.text((x+PADDING, y+PADDING+ICON_SIZE+2), name, fill=TEXT_COL, font=font_sm)
    return sheet

def main():
    out_dir = os.path.join(REPO, "assets/world-machine/icons/previews")
    os.makedirs(out_dir, exist_ok=True)
    print("Rendering desktop icons...")
    ds = build_sheet(DESKTOP_ICONS, COLS, "DESKTOP ICONS — WME Recreation (original works inspired by OneShot WME)")
    print("Rendering window icons...")
    ws = build_sheet(WINDOW_ICONS,  COLS, "WINDOW ICONS  — WME Recreation")
    cw = max(ds.width, ws.width)
    ch = ds.height + ws.height + 8
    combined = Image.new("RGBA", (cw, ch), BG_COLOR)
    combined.paste(ds, (0, 0)); combined.paste(ws, (0, ds.height+8))
    draw = ImageDraw.Draw(combined)
    draw.rectangle([0,0,cw-1,ch-1], outline=BORDER_COL, width=2)
    out = os.path.join(out_dir, "icon-sheet.png")
    combined.save(out, "PNG")
    print(f"Saved: {out}  ({combined.width}x{combined.height})")

if __name__ == "__main__":
    main()
