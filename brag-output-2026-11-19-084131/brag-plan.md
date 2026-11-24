# Brag Plan: NeuroLink — BCI Simulator

## What is this app?
NeuroLink is an interactive computational neuroscience laboratory and educational BCI simulator that demonstrates the full journey from raw synthetic electrophysiology to zero-phase Butterworth filtering, FFT spectral feature extraction, and linear classification in a refined editorial scientific workbench.

## The angle
"From signal to command." Demystify the brain-computer interface pipeline with absolute scientific integrity. No hype, no exaggerated thought-reading claims, no medical pretenses: just the pure beauty of signal processing mathematics made visible through an elegant Editorial Scientific Laboratory interface.

## Hook (first 2-3 seconds)
A high-contrast scientific proposition lands on an editorial Warm Ivory canvas: *"What happens between a brain signal and a digital command?"* Beneath the question, an authentic 256 Hz synthetic electrophysiology trace (Signal Coral `#D98B62`) sweeps across the oscilloscope with a prominent *"Synthetic signals only · No real EEG"* guarantee.

## Key moments (the middle)
- **The Experiment Studio Workbench arrives (3.0s):** Forest Green (`#173F3A`) card headers, Soft Sage (`#E5EEE7`) containers, input matrix (Artificial class: `left`, Reproducible seed: `7`), and simulated cursor calibrated at 50/100.
- **The Trigger & Zero-Phase Butterworth Purification (6.0s → 8.74s):** The simulated pointer clicks **"Generate and process"**. The dark scientific oscilloscope (`#0F1E1C`) illuminates; at beat 8.74s, the noisy baseline drift is eliminated as the zero-phase Butterworth band-pass filter reveals the purified 8 Hz rhythm in Neural Teal (`#79B6A5`), alongside real-time physical telemetry (Peak-to-Peak: 5.64, RMS: 0.98 V, SNR: +18.4 dB, Drift Attenuation: -26.1 dB).
- **Spectral Feature Extraction & Linear Command Payoff (13.11s):** At strong beat 13.11s, the FFT analysis stage calculates `mean_power_1_12_hz: 0.0313` and `mean_power_12_40_hz: 0.0012`. The classifier outputs `← left` (0.986 softmax confidence), and the simulated cursor deflecting smoothly from 50 to 40!

## Outro / punchline
The screen resolves into an editorial monograph closing card:
*"NeuroLink — Explore the computational neuroscience pipeline."*
Prominent scientific disclaimer remains: *"Synthetic signals only · Educational prototype"*, accompanied by the distinctive dual-frequency waveform signature.

## User flow worth showing
1. **Entry:** Configure synthetic class `left`, seed `7`, and simulated cursor position 50.
2. **Key Action:** Click **"Generate and process"** to synthesize 512 samples across 2.0 seconds.
3. **Result:** Butterworth band-pass (1–40 Hz) removes pink noise and 60 Hz mains; FFT extracts two stable power bands; logistic regression classifies `← left` with 98.6% probability, deflecting the cursor 50 → 40.

## Tone
- Preset: `polished`
- Creative direction: *editorial scientific laboratory film*
- Interpretation: Precise, intellectually honest, and aesthetically sophisticated. Employs the approved Google Stitch design language with Warm Ivory canvas, Forest Green typography, Soft Sage cards, and JetBrains Mono measurement callouts.

## Format: landscape — 1920x1080
## Duration: 22.0 seconds

## Visual identity (from the project)
- Background: `#F4F1E9` (Warm Ivory)
- Brand Primary: `#173F3A` (Forest Green)
- Text Primary: `#252D2B` (Deep Graphite)
- Accent Filtered: `#79B6A5` (Neural Teal)
- Accent Raw: `#D98B62` (Signal Coral)
- Surface / Cards: `#E5EEE7` (Soft Sage)
- Borders: `#CCD6D0` (Light Outline)
- Scope Viewport: `#0F1E1C` (Deep Scientific Forest Dark)
- Display font: `Manrope` (600, 700, 800)
- Body font: `Inter` (400, 600)
- Mono font: `JetBrains Mono` (400, 600, 700)
- Strongest visual element: Precision dual-trace oscilloscope with dark viewport `#0F1E1C`, Signal Coral raw drift, Neural Teal filtered wave, and real-time telemetry metrics.

## Share copy (draft)
We built NeuroLink: an interactive computational neuroscience lab that visualizes every step of a brain-computer interface pipeline—from synthetic 256 Hz electrophysiology to digital filtering, FFT feature extraction, and linear classification.

## Audio direction
- Role: warm intelligent bed with sparse professional tactile accents
- Music: `happy-beats-business-moves-vol-12-by-ende-dot-app.mp3`
- Music treatment: volume 0.30, fade in 0.0–0.6s, fade out 20.5–22.0s
- Music cue guidance: 109.96 BPM; strong cues at 3.00s (workbench reveal), 8.74s (filtered trace reveal), 13.11s (classification & cursor payoff), 18.56s (outro monograph).
- Audio-reactive treatment: subtle; RMS energy gently modulates background grid intensity and oscilloscope boundary glow.
- SFX posture: sparse, motion-matched, professional restraint.
  * 3.00s: `impactSoft_medium_001.ogg` (warm tactile workbench reveal)
  * 6.00s: `click2.ogg` (crisp button actuation on Generate and process)
  * 8.74s: `impactSoft_medium_004.ogg` (filtered trace and telemetry lock)
  * 13.11s: `impactBell_heavy_000.ogg` (soft harmonic chime on classification & cursor movement)
- Restraint rule: no loud buzzers, synthesizer chirps, or repetitive clicks.

## Storyboard

### Scene 1 — The Scientific Hook — 3.0s (0.00s – 3.00s)
- **Visuals:** Warm Ivory ground with faint precision graph grid. Top navigation bar with "NeuroLink" wordmark and badge "Synthetic signals only · No real EEG". Main headline: *"What happens between a brain signal and a digital command?"* Subtitle: *"An educational laboratory for brain-computer interface simulation."* Below, a live 256 Hz raw synthetic waveform (Signal Coral `#D98B62`) sweeps from left to right across 1680px.
- **Sequential/interaction:** Waveform draws across canvas (0.4s to 2.4s).
- **Audio intent:** Intelligent, intriguing opening; music fades in warmly.
- **Audio-coupled idea:** Music volume ramps from 0 to 0.30 over first 0.6s.
- **Music:** `happy-beats-business-moves-vol-12-by-ende-dot-app.mp3` (109.96 BPM)
- **Transition mood:** Clean wipe / carry across → Scene 2 at 3.00s (strong cue).

### Scene 2 — Experiment Studio Workbench — 3.0s (3.00s – 6.00s)
- **Visuals:** The screen opens into the 3-panel Experiment Studio workbench.
  * Left: Configuration matrix with class dropdown `left`, seed input `7`, simulated cursor widget `POS: 50 / 100`, and primary button "Generate and process".
  * Center: Synthetic Waveform Scope header with sampling badge `256 Hz · 512 samples · 1–40 Hz Band-pass`. Scope empty state: *"Select parameters and trigger generation to run pipeline."*
  * Right: Analysis header with "Output Stage" badge.
- **Sequential/interaction:** Pointer arrives at 4.2s, hovers over "Generate and process" button.
- **Audio intent:** Tactile physical laboratory presence.
- **Audio-coupled idea:** Soft tactile impact at 3.00s (`impactSoft_medium_001.ogg`).
- **Transition mood:** Button press trigger at 6.00s → Scene 3.

### Scene 3 — Synthesis & Waveform Scope — 7.11s (6.00s – 13.11s)
- **Visuals:** Button depresses with active state (`#102C29`). The center scope switches to deep dark viewport (`#0F1E1C`).
  * 6.0s–8.0s: Raw waveform draws in Signal Coral (`#D98B62`, dotted line) showing large 0.3 Hz drift and 60 Hz noise.
  * 8.74s (strong beat lock): The zero-phase Butterworth filter overlay strikes across the canvas in vibrant Neural Teal (`#79B6A5`), revealing the rhythmic 8 Hz sinusoidal envelope!
  * 9.5s–12.5s: Below the scope, four telemetry metric cards reveal sequentially along the beat grid: Peak-to-Peak (5.64), RMS Voltage (0.98 V), SNR (+18.4 dB), and Drift Attenuation (-26.1 dB).
- **Sequential/interaction:** Pointer click at 6.00s; raw trace draws 6.0–8.0s; filtered trace reveals at 8.74s; metric badges snap into place on beat grid (9.83s, 10.37s, 10.93s, 11.46s).
- **Audio intent:** Tension to resolution as noise is stripped away.
- **Audio-coupled idea:** `click2.ogg` at 6.00s; `impactSoft_medium_004.ogg` at 8.74s beat lock.
- **Transition mood:** Carry across to right analysis panel → Scene 4 at 13.11s (strong cue).

### Scene 4 — Feature Extraction & Classifier Payoff — 5.45s (13.11s – 18.56s)
- **Visuals:** Right panel Analysis lights up:
  * Extracted Spectral Features: `[1, 12) Hz: 0.0313` (8 Hz dominant) vs `[12, 40] Hz: 0.0012`.
  * Classification Result Card: Large Forest Green card declaring `← LEFT` with confidence badge `98.6% Softmax Probability`.
  * In the left panel, the simulated cursor moves 10 units leftward: position bar animates smoothly from `50` to `40`, with status indicator changing to `DEFLECTED LEFT (-10)`.
- **Sequential/interaction:** Spectral table populates at 13.11s; classification card highlights at 14.20s; cursor deflects 50 → 40 at 15.29s.
- **Audio intent:** Satisfaction and technical triumph.
- **Audio-coupled idea:** Gentle harmonic chime (`impactBell_heavy_000.ogg`) at 13.11s.
- **Transition mood:** Dissolve / carry across → Scene 5 at 18.56s (strong cue).

### Scene 5 — Outro & Scientific Monograph — 3.44s (18.56s – 22.00s)
- **Visuals:** Elegant full-frame editorial title card.
  * Eyebrow: `COMPUTATIONAL NEUROSCIENCE · BIOLOGY FOR ENGINEERS`
  * Hero Title: `NeuroLink`
  * Subtitle: `Explore the pipeline from signal to command.`
  * Footer: `Built by Team 2 · Python 3.12 · SciPy & Streamlit`
  * Permanent Scientific Badge: `Synthetic signals only · No real EEG`
  * Right side: High-resolution signature loop of the purified 8 Hz neural waveform in Neural Teal.
- **Sequential/interaction:** Title and waveform enter cleanly on beat 18.56s and hold settled until end.
- **Audio intent:** Warm closing resolution; music gracefully fades to zero.
- **Audio-coupled idea:** Music fade begins at 20.50s, fading completely by 22.00s.

**Music mood for this video:** polished, smart, contemporary scientific groove.
**Audio summary:** Steady intellectual groove supporting an empirical progression from messy signal through zero-phase filtering to precise classification.
