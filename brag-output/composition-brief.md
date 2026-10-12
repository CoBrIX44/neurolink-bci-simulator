# Hyperframes composition brief: NeuroLink

Produce the 22-second 1920 x 1080 launch video specified in brag-plan.md. Save composition under composition/ and final MP4/poster in this directory. Keep all work local.

## Sources and required copy
Project E:/BCI. Inspect app.py, README.md, .streamlit/config.toml and presentation/signal_examples.json. Recreate the app's controls and output faithfully with deliberate editorial enlargement, not a claim of literal screen capture.
Required wording: “NeuroLink”, “BCI Simulator”, “Generate and process”, “Artificial signal class”, “Predicted demo command”, “Synthetic signals only · No real EEG”. Generated left/seed7 data are the source of all waveforms and numerical feature values.

## Design
Polished scientific demonstration. App teal #087E8B, raw trace #8795A5; editorial background #F4F7F7, ink #16313B, white panels. Segoe UI/Arial system fonts. Large readable type and graph marks. Persistent synthetic-only badge. Clear dotted raw / solid filtered encoding. No real brain/headset visuals or claims of live acquisition. Three sparse transitions; waveform is the visual through-line.

## Audio
Copy bundled vol-12 music to composition/assets/music. Use local trimmed/faded 22-second bed at 0.30. Strong-cue locks at 8.74, 13.11, 18.56 sec. Sparse SFX: low-risk impactSoft_medium_001 at dashboard reveal, ui/click2 at actual button press, impactSoft_medium_004 at result reveal. Read brag skill sfx-analysis.md. Copy chosen assets locally. No narration. Use current Hyperframes audio-reactive helper for subtle background treatment if available; document absence rather than blocking export.

## Implementation contract
Read hyperframes-core, hyperframes-animation, hyperframes-creative, hyperframes-keyframes and hyperframes-cli. Use seek-safe timeline animation and current native composition contract. Run npx hyperframes check with zero errors, open local preview, render high quality, inspect representative frames, select a settled poster and bake it into frame zero. Validate file duration/resolution/audio streams. Do not edit application code.
