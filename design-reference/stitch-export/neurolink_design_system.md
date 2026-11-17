---
name: "NeuroLink Editorial Laboratory"
description: "A premium neuroscience research and simulation interface combining editorial typography, precision waveform visualization, and warm ivory/forest green tones."
---

## Overview

NeuroLink is an educational Brain-Computer Interface (BCI) simulator and computational neuroscience exploration environment. It bridges biological signal processing, mathematical filtering, and machine learning into a tangible interactive digital laboratory.

The design fuses contemporary neuroscience research software with premium editorial publication standards and scientific instrument clarity. Rejecting generic corporate dashboards, gratuitous rounded cards, and ungrounded AI aesthetics, NeuroLink privileges intentional negative space, tactile instrument feel, asymmetric column rhythms, high-contrast typography, and scientific data visualization.

- **Primary Persona:** Undergraduate and graduate bioengineering students, computational neuroscience researchers, and academic demonstrators.
- **Tone:** Methodical, intellectually curious, refined, authoritative, and scientifically rigorous.
- **Visual Style:** Editorial Scientific Laboratory — warm ivory background, rich forest green accents, deep graphite typography, neural teal secondary markers, and signal coral indicators.

## Colors

The palette establishes a calm, glare-free, light-theme-first environment evoking archival scientific monographs and high-end electrophysiology instrument displays.

- **Warm Ivory (`#F4F1E9`):** Ground surface providing soft contrast without the sterility of pure white.
- **Forest Green (`#173F3A`):** The primary anchor representing biological stability, academic pedigree, and primary interactive authority.
- **Deep Graphite (`#252D2B`):** Text and structural ink tone providing deep legibility.
- **Neural Teal (`#79B6A5`):** Signal processing, filtered waves, spectral ribbons, and low-frequency power markers.
- **Signal Coral (`#D98B62`):** Highlights, raw synthetic traces, high-frequency spectral markers, and key diagnostic notices.
- **Soft Sage (`#E5EEE7`):** Secondary container surface and subtle structural framing.

```yaml
colors:
  forest-green: "#173F3A"
  deep-graphite: "#252D2B"
  neural-teal: "#79B6A5"
  signal-coral: "#D98B62"
  soft-sage: "#E5EEE7"
  warm-ivory: "#F4F1E9"
  light:
    primary: "#173F3A"
    on-primary: "#F4F1E9"
    surface: "#F4F1E9"
    on-surface: "#252D2B"
    surface-variant: "#E5EEE7"
    on-surface-variant: "#173F3A"
    outline: "#CCD6D0"
```

## Typography

NeuroLink pairs **Manrope** for authoritative, modern architectural headlines and section titles, **Inter** for dense and legible interface controls, scientific parameters, and body text, and **JetBrains Mono** with tabular numerals for time series coordinates, sample rates, and mathematical metrics.

```yaml
typography:
  display-lg:
    fontFamily: "Manrope"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 56px
    letterSpacing: -1.0px
  display-lg-mobile:
    fontFamily: "Manrope"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 40px
    letterSpacing: -0.5px
  headline-xl:
    fontFamily: "Manrope"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 44px
    letterSpacing: -0.75px
  headline-xl-mobile:
    fontFamily: "Manrope"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 36px
    letterSpacing: -0.5px
  headline-lg:
    fontFamily: "Manrope"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 36px
    letterSpacing: -0.5px
  headline-lg-mobile:
    fontFamily: "Manrope"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 30px
    letterSpacing: -0.25px
  headline-md:
    fontFamily: "Manrope"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 28px
    letterSpacing: -0.25px
  body-lg:
    fontFamily: "Inter"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 28px
  body-md:
    fontFamily: "Inter"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 24px
  body-sm:
    fontFamily: "Inter"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 20px
  label-lg:
    fontFamily: "Inter"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 20px
    letterSpacing: 0.1px
  label-sm:
    fontFamily: "Inter"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 16px
    letterSpacing: 0.5px
  mono-data:
    fontFamily: "JetBrains Mono"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 18px
```

## Layout & Spacing

NeuroLink adopts a structured laboratory workbench layout. Screen compositions emphasize wide waveform canvases, disciplined technical sidebars, and crisp tabular metadata.

- **Workbench Grid:** 12-column desktop grid with a max-width container of 1440px.
- **Rhythm:** Standard base-8 spacing scale with 4px micro-steps for oscilloscope rulers and data badges.

```yaml
spacing:
  gutter-xs: 4px
  gutter-sm: 8px
  gutter-md: 16px
  gutter-lg: 24px
  gutter-xl: 32px
  section: 48px
  page-margin: 32px
```

## Elevation & Depth

To preserve an editorial scientific publication feel, NeuroLink eschews heavy drop shadows and glowing neon cards in favor of:

1. **Crisp Structural Outlines (`1px solid #CCD6D0`):** Sharp framing defining oscilloscope viewports and telemetry matrices.
2. **Tonal Surface Nesting:** Soft sage `#E5EEE7` inset surfaces against the warm ivory ground `#F4F1E9`.
3. **Micro Hairline Dividers:** Precise 1px rules dividing frequency stages and tabular figures.

## Shapes

Shapes are architectural and precise. Buttons and inputs maintain a disciplined 4px to 6px corner radius rather than generic pill capsules, referencing scientific test equipment and precision oscilloscopes.

```yaml
rounded:
  sm: 2px
  DEFAULT: 4px
  md: 6px
  lg: 8px
  xl: 12px
  full: 9999px
```

## Motion & Micro-interaction

Motion serves explanatory and instrumentation feedback purposes only. Waveform streams draw with steady linear or ease-out timing to represent physical analog signal capture.

- No looping cosmetic float animations.
- Filter mode switching transitions in 200ms with subtle opacity cross-fades.
- Waveform scrubbing and zoom interactions feel immediate and mechanical.

```yaml
motion:
  state-change:
    duration: 150ms
    delay: 0ms
    timingFunction: cubic-bezier(0.16, 1, 0.3, 1)
  signal-sweep:
    duration: 400ms
    delay: 0ms
    timingFunction: ease-out
  panel-slide:
    duration: 250ms
    delay: 0ms
    timingFunction: cubic-bezier(0.2, 0, 0, 1)
```

## Voice & Content Strategy

The voice is scholarly, precise, and transparent about computational constraints.

- **Scientific Transparency:** Explicitly state the boundaries of synthetic signals (256 Hz, 2.0s duration, 512 samples, artificial motor imagery proxies).
- **Mandatory Disclaimer:** Prominently communicate: *"This is an educational simulator using synthetic EEG-like signals, not live brain data. LEFT and RIGHT are artificial demonstration labels. It does not read thoughts, measure human intentions, or provide medical or clinical predictions."*
- **Metric Formatting:** Tabular figures with clear engineering units (`Hz`, `µV²/Hz`, `s`, `au`).

## Components

Component implementations live as individual HTML sticker sheet files in
`components/`. Each file contains the canonical, styled HTML components with
`<!-- COMPONENT: name -->` comment markers. Read each file before use.

- **Alert** → `@components/alert.html`: `alert-info`
- **Badge** → `@components/badge.html`: `badge-numeric`, `badge-dot`
- **Button** → `@components/button.html`: `button-primary`, `button-icon`, `button-with-icon`
- **Card** → `@components/card.html`: `card-elevated`, `card-action`, `card-interactive`, `card-interactive-2`
- **Tabs** → `@components/tabs.html`: `tabs-horizontal`, `tabs-with-icon`
