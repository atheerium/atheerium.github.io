# atheerium.github.io — Design Tokens & Patterns

> Generated from `src/layouts/Layout.astro`. Source of truth for all design decisions.
> Before changing any value here, verify the intent in Layout.astro's `<style>` block.

## Color Palette

| Token | Value | Usage |
|---|---|---|
| `--bg` | `#fafafa` | Page background |
| `--text-primary` | `#1a1a2e` | Body and heading text |
| `--text-secondary` | `#555` | Descriptions, subtitles |
| `--text-muted` | `#666` | Dates, metadata |
| `--text-dim` | `#888` | Footer text, empty state messages |
| `--link` | `#2563eb` | All links |
| `--link-visited` | `#7c3aed` | Visited links |
| `--nav-bg` | `#ffffff` | Navigation bar |
| `--border-light` | `#e0e0e0` | Nav/footer borders, dividers |
| `--border-dim` | `#e8e8e8` | Entry list dividers |
| `--code-bg` | `#e8e8e8` | Inline code |
| `--pre-bg` | `#0d1117` | Code blocks |
| `--pre-text` | `#e6edf3` | Code block text |
| `--blockquote-bg` | `#f0f4ff` | Blockquote background |
| `--tag-bg` | `#e8e8e8` | Tag pills |
| `--tag-text` | `#555` | Tag text |
| `--hover-bg` | `#f5f5f5` | List item hover |
| `--accent` | `#2563eb` | Blockquote border, link color |

## Typography

| Element | Value |
|---|---|
| Font stack | `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', Arial, sans-serif` |
| Monospace | `'SF Mono', 'Fira Code', 'Fira Mono', 'Roboto Mono', monospace` |
| Base size | `16px` |
| Body line-height | `1.7` |
| Heading line-height | `1.3` |

### Type Scale

| Level | Size |
|---|---|
| `h1` | `2rem` |
| `h2` | `1.5rem` |
| `h3` | `1.25rem` |
| Body | `1rem` |
| Small (`.date`, `.tag`, footer) | `0.8rem–0.9rem` |

## Layout

| Property | Value |
|---|---|
| Content max-width | `720px` |
| Content padding | `2rem 1.5rem` |
| Nav padding | `1rem 1.5rem` |
| Footer padding | `2rem 1.5rem` |
| Nav gap | `1.5rem` |

## Components

### Entry List (`.entry-list`)
- Unstyled `<ul>` used on section index pages and homepage
- Each `<li>` has `margin-bottom: 1.5rem` + `border-bottom: 1px solid #e8e8e8`
- Hover: `background: #f5f5f5`, `border-radius: 4px`
- Title: bold `1.1rem` link
- Description: `0.9rem`, `#555`
- Date: `0.8rem`, `#666`

### Tag Pill (`.tag`)
- Inline span, `0.75rem`, `#e8e8e8` bg, `#555` text, `3px` border-radius

### Blockquote
- Left `3px solid #2563eb` border, `#f0f4ff` background, `0.5em 1em` padding

### Code
- Inline: `#e8e8e8` bg, `0.9em` size, `3px` border-radius
- Block (pre): `#0d1117` bg, `#e6edf3` text, `1rem` padding, `8px` border-radius

### Navigation
- Horizontal flex row with `flex-wrap: wrap`, white background, bottom border
- Site title on the left (`margin-right: auto`)
- Links: `0.9rem`, `#444`, lowercase (except site title)

### Footer
- Centered text, `0.8rem`, `#888`, top border
- Links: `#666`

## Breakpoints / Responsive
- No explicit media queries. Layout is naturally fluid.
- Nav wraps via `flex-wrap: wrap`.
- Content `max-width: 720px` keeps readability on wide screens and collapses below.

## Dark Mode
- Not supported. No `prefers-color-scheme` query.
- Intentionally omitted to keep the site simple.

## Animations
- None. Zero transitions, keyframes, or hover effects beyond `a:hover` underline.

## CSS Architecture
- All styles live in `Layout.astro`'s single `<style>` tag.
- No CSS framework, no preprocessor, no design token file.
- This `DESIGN.md` IS the token reference for agents.
