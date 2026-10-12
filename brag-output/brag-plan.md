# NeuroLink / From signal to command

## Planning rubric
1. Product: educational Streamlit simulator of a simplified BCI processing pipeline, using generated signals only.
2. Strongest claim: explore generation, filtering, features and an artificial command in one dashboard. No hardware required for the simulator.
3. Visual hook: a real generated waveform becomes the visual thread linking the whole video.
4. UI: reconstruct the actual class selector, seed field, Generate and process button, raw/filtered chart, named features and artificial output from app.py. This is an editorial animation of the UI, not a screen recording.
5. Length: 22 seconds, landscape 1920 x 1080, 30 fps.
6. Tone: polished; an approachable scientific demonstration, clean off-white, teal from the app theme, ink typography and restrained transitions.
7. Audio: quiet steady music bed, three subtle interaction/reveal accents; no narration.
8. Share caption: We built NeuroLink: a hands-on BCI simulator that takes synthetic signals through filtering, feature extraction and classification. Explore the pipeline in an interactive dashboard—educational simulation only, with no real EEG or thought-reading.
9. User flow: choose artificial left and seed 7 → Generate and process → compare raw/filtered traces → inspect two features and artificial left prediction.

## Creative angle
Make the pipeline visible. Keep the same waveform as the anchor while the video moves from an intriguing signal to an understandable application result. Avoid claims about real-world accuracy, human intent, live streaming or artifact elimination. A persistent synthetic-only label is part of the design.

## Storyboard
| Time | Scene and copy | Action / transition | Sound |
|---|---|---|---|
| 0–3 | Hook: “From signal to command.” / “A hands-on BCI simulator.” | Seed-7 raw waveform draws across the canvas beneath the headline. Synthetic-only label visible immediately. | Music fades in. |
| 3–6 | Reveal: “NeuroLink” / “BCI Simulator” | Dashboard arrives with left selector, seed 7 and actual “Generate and process” label. Pointer approaches button. | Soft reveal accent at 3.0. |
| 6–13.11 | Product flow: “Generate. Filter. Explore.” | Button presses at 6.0; raw signal draws, then filtered signal overlays at 8.74. Keep axis labels and dotted/solid legend. 1–40 Hz offline filter callout. | Quiet click at 6.0. |
| 13.11–18.56 | Payoff: “Features → artificial output” | Two actual seed-7 feature values reveal alongside predicted demo command “left”. Brief formula-level labels support the flow without dense detail. | Soft result accent at 13.11. |
| 18.56–22 | Outro: “NeuroLink” / “Explore the pipeline.” / “Built by Team 2” | Generous final title with a small waveform signature. “Synthetic signals only · No real EEG” remains on screen. | Music fades out during final 1.5 sec. |

Total: 22 seconds. Sentence holds exceed 0.3 seconds per word; major labels hold well over 0.8 seconds. No rapid reading or narration.

## Music cue guidance
Bundled track: happy-beats-business-moves-vol-12-by-ende-dot-app.mp3.
Preset: C:/Users/Admin/.agents/skills/brag/assets/music/cues/happy-beats-business-moves-vol-12-by-ende-dot-app.music-cues.json.
Strong cues selected: filtered reveal 8.74, result reveal 13.11, outro 18.56 seconds. Prioritize readability over other beat points.
Music at 0.30; sparse low-HF-risk SFX quieter than a typical launch trailer.
Audio-reactive treatment: subtle background presence from RMS if supported by the Hyperframes helper; never alter the scientific waveform based on music.

## Evidence
app.py, .streamlit/config.toml, README.md, signal_generator.py, processing.py, features.py and presentation/signal_examples.json. Signal data are actual outputs of this project's synthetic pipeline. No new accuracy or testing claims appear in the video.
