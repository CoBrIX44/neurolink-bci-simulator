# Hyperframes Composition Brief: NeuroLink — BCI Simulator

## Objective
Create a short, polished launch-style brag video for NeuroLink using the Google Stitch 'Editorial Scientific Laboratory' design system.

## Output
- Composition directory: `brag-output-2026-11-19-084131/composition/`
- Rendered video: `brag-output-2026-11-19-084131/brag.mp4`
- Format: landscape — 1920x1080
- Duration: 22.0 seconds (660 frames at 30 fps)

## Source Material
- Project root: `/home/adityadugar/Documents/Projects/neurolink-bci-simulator`
- Primary files read: `README.md`, `app.py`, `ui_theme.py`, `views/landing.py`, `views/studio.py`, `signal_generator.py`, `processing.py`, `features.py`
- Product name: NeuroLink
- Tagline / strongest claim: "What happens between a brain signal and a digital command? Explore the science behind brain-computer interfaces through an interactive simulation of neural signal processing and machine learning."
- Key UI or visual moment to recreate: The Experiment Studio workbench with its 3-column layout (Configuration, Synthetic Waveform Scope, Analysis stage), showing zero-phase Butterworth filtering stripping pink noise, telemetry metrics, FFT power features, and simulated cursor deflection.
- Copy that must appear verbatim:
  - "NeuroLink"
  - "Synthetic signals only · No real EEG"
  - "What happens between a brain signal and a digital command?"
  - "Generate and process"
  - "SAMPLING: 256 Hz · 512 samples · 2.0s"
  - "FILTER PASSBAND: 1.0 – 40.0 Hz"
  - "Predicted demo command: left"
  - "POS: 50 / 100" → "POS: 40 / 100"
  - "Built by Team 2"

## Creative Direction
- Tone preset: `polished`
- Creative direction: *editorial scientific laboratory film*
- Interpretation: Clean, precise, and intellectually rigorous. Restrained typography and transitions. Grounded strictly in authentic project facts without generic SaaS fluff.
- Angle: From raw noisy signal to digital command. Make the signal processing pipeline tangible and visible with genuine scientific integrity.
- Hook: A direct question (*"What happens between a brain signal and a digital command?"*) paired with a live 256 Hz raw synthetic waveform sweeping across the screen.
- Outro / punchline: Monograph-style closing card: *"NeuroLink — Explore the computational neuroscience pipeline."*
- Avoid:
  - Generic SaaS language ("supercharge your workflow")
  - Exaggerated thought-reading or medical claims
  - Abstract filler visuals that have nothing to do with the actual UI
  - Disconnected neon visualizer styles (keep the editorial warm ivory / forest green aesthetic)

## Visual Identity
- Background: `#F4F1E9` (Warm Ivory)
- Brand Primary: `#173F3A` (Forest Green)
- Text Primary: `#252D2B` (Deep Graphite)
- Accent Filtered: `#79B6A5` (Neural Teal)
- Accent Raw: `#D98B62` (Signal Coral)
- Surface / Containers: `#E5EEE7` (Soft Sage)
- Borders: `#CCD6D0` (Light Outline)
- Oscilloscope Viewport: `#0F1E1C` (Deep Scientific Forest Dark)
- Display font: `Manrope` (local font assets in `assets/fonts/`)
- Body font: `Inter`
- Mono font: `JetBrains Mono`

## Storyboard
Use the storyboard in `brag-plan.md` as the creative contract:
1. Scene 1 — The Scientific Hook (0.00s – 3.00s) — Question, 256 Hz raw waveform stream, synthetic-only disclaimer.
2. Scene 2 — Experiment Studio Workbench (3.00s – 6.00s) — 3-panel laboratory workbench, parameters, pointer hover.
3. Scene 3 — Synthesis & Waveform Scope (6.00s – 13.11s) — Click trigger, raw coral waveform plotted, zero-phase Butterworth filter reveal at 8.74s, telemetry metrics grid.
4. Scene 4 — Feature Extraction & Classifier Payoff (13.11s – 18.56s) — Spectral FFT power bands, classifier `← left` (0.986 score), cursor deflection 50 → 40.
5. Scene 5 — Outro & Scientific Monograph (18.56s – 22.00s) — Monograph closing card, team attribution, waveform signature.

## Audio
- Audio role: warm intelligent bed with sparse professional tactile accents
- Audio arc: subtle introduction, engaging pulse during synthesis, satisfying harmonic resolution on classification, graceful fade out.
- Music: `assets/music/bed.mp3` (volume 0.30, fade in 0.0–0.6s, fade out 20.5–22.0s)
- Music cue guidance: 109.96 BPM; strong cues at 3.00s, 8.74s, 13.11s, 18.56s.
- Audio-reactive treatment: subtle; RMS energy modulates the background graph grid opacity.
- Audio-coupled moments:
  - 3.00s — `assets/sfx/impact/impactSoft_medium_001.ogg` (workbench reveal)
  - 6.00s — `assets/sfx/ui/click2.ogg` (button press)
  - 8.74s — `assets/sfx/impact/impactSoft_medium_004.ogg` (filtered trace payoff)
  - 13.11s — `assets/sfx/impact/impactBell_heavy_000.ogg` (classification & cursor deflection)
- SFX posture: sparse, low-HF risk, professional restraint.
- Audio files: copied locally into `assets/music/` and `assets/sfx/`.

## Hyperframes Instructions
- Composition entry: `index.html` in `composition/`.
- Must pass `npx hyperframes check` with zero errors.
- Ensure all text passes WCAG contrast and readability floors.
- Use seek-safe GSAP timelines with `fromTo`.
