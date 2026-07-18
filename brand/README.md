# ShopClass brand assets (SVG)

All assets are pure vector, self-contained (no font dependencies — wordmarks and
labels are converted to outlines), and safe to scale to any size.

| File | Use |
|---|---|
| `shopclass-logo.svg` | Primary large logo (icon + wordmark) |
| `shopclass-logo-compact.svg` | Short logo for nav headers / GitHub readme |
| `shopclass-icon.svg` | Mark only, transparent background |
| `shopclass-logo-mono.svg` | Primary logo, monochrome all-navy (single-color contexts) |
| `shopclass-logo-compact-mono.svg` | Short logo, monochrome all-navy |
| `shopclass-icon-mono.svg` | Mark only, monochrome all-navy |
| `shopclass-board.svg` | 1920x1080 brand-guidelines board (all four sections) |

## favicon/

| File | Use |
|---|---|
| `shopclass-favicon.svg` | SVG favicon — navy field, teal mark |
| `favicon.ico` | Multi-size icon (16 + 32 + 48) for `<link rel="icon">` / Windows |
| `favicon-{16,32,48,64,128}.png` | Transparent PNGs, browser & UI sizes |
| `favicon-180.png` | Apple touch icon (`apple-touch-icon`) |
| `favicon-{192,256,512}.png` | PWA / Android icons |
| `favicon-maskable-512.png` | Full-bleed maskable icon (mark inside the 80% safe zone) |
| `site.webmanifest` | Web app manifest wired to the icons above |

Deploy the `favicon/` folder at the site root (paths in the manifest assume
`/favicon/...`) and add:

```html
<link rel="icon" href="/favicon/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon/shopclass-favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/favicon/favicon-180.png">
<link rel="manifest" href="/favicon/site.webmanifest">
```

## Palette

- Deep Navy `#0F2742`
- Teal `#12A6A0`
- Warm Off-White `#F7F5F1`
- Slate Gray `#435466`
- Coral accent `#FF6B4A`

## Typography

- Headings / wordmark: **Manrope ExtraBold (800)** — SIL Open Font License
- Body: **Inter Regular/Medium** — SIL Open Font License

Both fonts are OFL-licensed, so embedding their outlines in these logos is
permitted, including commercial use.
