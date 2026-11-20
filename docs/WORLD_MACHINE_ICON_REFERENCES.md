# World Machine Icon References

> **Legal notice:** All icons in this collection are **original recreations** drawn from scratch,
> inspired by the visual language of *OneShot: World Machine Edition* (Future Cat / Nightmargin).
> They are **not** official assets, extracts, or derivatives of the game's binary resources.
> OneShot and The World Machine are trademarks of their respective owners.

---

## Sources consulted

| Source | URL | Purpose |
|--------|-----|---------|
| OneShot WME Steam page | https://store.steampowered.com/app/2915460/ | Official screenshots, UI screenshots |
| OneShot Wiki – WME article | https://oneshot.wiki.gg/wiki/OneShot_(World_Machine_Edition) | Lore, palette, interface description |
| pdn6606/TWM-xfce (reference only) | https://github.com/pdn6606/TWM-xfce | Third-party desktop recreation for style reference |
| pdn6606/OneShot-themes (reference only) | https://github.com/pdn6606/OneShot-themes | Color palette and theme reference |

---

## Color palette used

| Token | Hex | Usage |
|-------|-----|-------|
| Background | `#08050D` | Deepest background, transparency base |
| Desktop | `#0B0712` | Icon area background |
| Window | `#17101F` | Window interior fill |
| Dark body | `#1A1028` | Icon body fill |
| Medium purple | `#2A1A3E` | Shadow / secondary fill |
| Border dark | `#6940A7` | Outer borders, shadows |
| Purple main | `#8751D8` | Title bars, main accents |
| Purple bright | `#9B64F6` | Highlight borders |
| Lavender | `#BE91FF` | Active pixel highlights |
| Light lavender | `#E8DDF7` | Bright pixels, text |
| Pink-red | `#FF91B8` | Close button (contrast) |

---

## Desktop icons

### `documents.svg`
- **Source:** WME desktop screenshot analysis — doc/file icon visible in desktop
- **Observed:** Rectangular page with dog-ear fold top-right; thin purple border; 3–4 horizontal lines suggesting text content
- **Design decisions:** 32×32 px grid; 1-px outlines; text lines at 3 px intervals; lighter top line = title, dimmer = body text
- **File:** `assets/world-machine/icons/desktop/documents.svg`
- **Status:** Original recreation inspired by WME, not an official asset

---

### `oneshot.svg`
- **Source:** OneShot logo / lightbulb/sun motif (central game symbol)
- **Observed:** The lightbulb is the core symbol of the game — sun-shaped bulb with rays, narrow neck, rectangular base
- **Design decisions:** 32×32; 8 compass rays; bright inner core (#FFF) fades to lavender at rim; neck narrows to 8 px; base rect 10×2
- **File:** `assets/world-machine/icons/desktop/oneshot.svg`
- **Status:** Original recreation, not official

---

### `customize.svg`
- **Source:** WME customize/theme application description from wiki + TWM-xfce reference
- **Observed:** Slider-style control panel with draggable knobs on horizontal tracks; color swatches row
- **Design decisions:** 3 slider tracks; each knob is 3×3 px white+purple; 5 color swatches 4×4 px at bottom
- **File:** `assets/world-machine/icons/desktop/customize.svg`
- **Status:** Original recreation

---

### `help.svg`
- **Source:** WME help application icon (question mark in circle)
- **Observed:** Filled circle outline with thick question mark; gap between stem and dot
- **Design decisions:** Circle uses rect approximation; Q-mark uses 2-px stroke equivalent in pixel art
- **File:** `assets/world-machine/icons/desktop/help.svg`
- **Status:** Original recreation

---

### `wallpapers.svg`
- **Source:** WME wallpaper picker; landscape thumbnails visible in community screenshots
- **Observed:** Framed landscape with dark sky, mountain silhouettes, circuit lines on ground
- **Design decisions:** Frame with purple border; mountain layers use 3 depth values; star dots in sky; CRT circuit line on ground; monitor stand at bottom
- **File:** `assets/world-machine/icons/desktop/wallpapers.svg`
- **Status:** Original recreation

---

### `themes.svg`
- **Source:** WME theme/customize application; color palette visual reference
- **Observed:** Paint bucket with color drip/puddle; color swatch row
- **Design decisions:** Bucket outline 14×12 px; handle arc; pour drop right of bucket; interior puddle; row of 3 swatches along bucket rim
- **File:** `assets/world-machine/icons/desktop/themes.svg`
- **Status:** Original recreation

---

### `music-box.svg`
- **Source:** WME Jukebox application (desktop icon); audio player UI reference
- **Observed:** Box with two speaker grilles (dot grid), center display panel, control buttons, leg supports
- **Design decisions:** 22×20 px body; 6×8 grille areas; 3 control buttons; 2 legs; note symbol in center display
- **File:** `assets/world-machine/icons/desktop/music-box.svg`
- **Status:** Original recreation

---

### `gallery.svg`
- **Source:** WME Gallery/Photos application; 2×2 grid of images
- **Observed:** Photo gallery split into 4 quadrants; each showing a different miniature scene
- **Design decisions:** 4 quadrant split with 1-px separator; each quadrant ~12×12 px; scenes: mountain/sky, planet, circuit, star
- **File:** `assets/world-machine/icons/desktop/gallery.svg`
- **Status:** Original recreation

---

### `friends.svg`
- **Source:** WME Contacts/Friends application; character sprite style
- **Observed:** Two pixel art humanoid figures side by side; simple head+body+arms+legs structure at ~8×8 resolution
- **Design decisions:** Two figures 8×20 px each; different shades of purple/lavender to differentiate them; connection line between figures
- **File:** `assets/world-machine/icons/desktop/friends.svg`
- **Status:** Original recreation

---

### `badges.svg`
- **Source:** WME Achievements icon; medal/trophy shape
- **Observed:** Circular medal with ribbon at top; star shape inside medal
- **Design decisions:** Ribbon two-tone (6940A7 / 8751D8); medal circle outline BE91FF; star inside uses pixel-diamond approximation
- **File:** `assets/world-machine/icons/desktop/badges.svg`
- **Status:** Original recreation

---

### `controls.svg`
- **Source:** WME Controls application; gamepad/controller shape
- **Observed:** Rectangular controller body with grips; D-pad left side; 4 ABXY buttons right side; center select/start buttons
- **Design decisions:** 24×12 body; 4-px grips; D-pad uses cross of 3×3; buttons use 2×2 colored squares
- **File:** `assets/world-machine/icons/desktop/controls.svg`
- **Status:** Original recreation

---

### `exit.svg`
- **Source:** WME Exit/Power-off application
- **Observed:** Door frame with open door panel; arrow pointing outward
- **Design decisions:** 16×24 door; door panel slightly inset; knob 2×2; horizontal arrow right of door; floor line at bottom
- **File:** `assets/world-machine/icons/desktop/exit.svg`
- **Status:** Original recreation

---

## Window icons

### `minimize.svg`  `maximize.svg`  `close.svg`
- **Source:** WME window chrome buttons observed in community screenshots and TWM-xfce reference
- **Observed:** Small square buttons (~10–14 px) in title bar; minimize = horizontal bar; maximize = square outline; close = X shape; close button uses distinct reddish/pink color
- **Design decisions:** 16×16 button face with 1 px border; raised top-left, shadowed bottom-right; lavender icons on dark background; close uses #FF91B8 on #3E1A2A
- **Files:** `assets/world-machine/icons/window/minimize.svg`, `maximize.svg`, `close.svg`
- **Status:** Original recreation

---

### `folder.svg`
- **Source:** WME file explorer; folder icon standard shape adapted to WME palette
- **Observed:** Tab on top-left of body; body taller than wide; interior lines suggesting file contents
- **Design decisions:** Tab 10×3 px; body 26×16 px; interior content hinted with 1-px dimmed lines
- **File:** `assets/world-machine/icons/window/folder.svg`
- **Status:** Original recreation

---

### `document.svg`
- **Source:** WME doc viewer icon (window header variant of documents.svg)
- **Observed:** Same page-with-fold shape but adapted for 16-px window header use
- **Design decisions:** Identical structure to desktop/documents.svg but rendered in window/navbar context
- **File:** `assets/world-machine/icons/window/document.svg`
- **Status:** Original recreation

---

### `image.svg`
- **Source:** WME photo/image viewer window
- **Observed:** Frame with landscape scene inside; monitor-stand at bottom
- **Design decisions:** 26×18 inner image; sky + mountains + ground; stand 8×2 px; base 12×1 px
- **File:** `assets/world-machine/icons/window/image.svg`
- **Status:** Original recreation

---

### `settings.svg`
- **Source:** WME customize/settings window header
- **Observed:** Gear/cog shape with 8 teeth at compass directions and diagonals; center circle with dot
- **Design decisions:** Teeth 4×4 px at diagonals, 6×4 px at cardinal directions; body ring from rect cross; center hole 8×8; center highlight 2×2
- **File:** `assets/world-machine/icons/window/settings.svg`
- **Status:** Original recreation

---

## Validation

All 19 icons were rendered via `cairosvg` at 64×64 and verified:
- Zero render errors
- All files have non-transparent pixel content (900–3136 px range)
- Consistent `shape-rendering="crispEdges"` preserves pixel art appearance
- Transparent backgrounds confirmed

Preview sheet: `assets/world-machine/icons/previews/icon-sheet.png`
