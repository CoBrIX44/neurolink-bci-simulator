# NeuroLink launch video

Final deliverable: `brag.mp4` — 22 seconds, 1920 × 1080, 30 fps, 660 frames, H.264 with AAC audio, approximately 2.24 MB. `brag.jpg` is the selected settled closing frame at 20.8 seconds and is also baked into frame zero. `share-copy.txt` contains the posting caption.

Created with the locally invoked brag skill and Hyperframes 0.8.149. The animated dashboard is an editorial reconstruction of app.py, not a literal screen recording. Waveforms and feature numbers use the project's actual synthetic left/seed-7 output from presentation/signal_examples.json. No real EEG, human-intention, real-time acquisition, clinical, or real-world performance claim is made. No application source was changed.

## Verification performed

- Hyperframes check: zero errors across lint, runtime, layout, motion and contrast. Final contrast sweep: 85/85 checks passed. Browser audit ran successfully.
- Three nonblocking lint warnings recommend sub-compositions for the three nested scene sections. The composition deliberately uses one registered timeline; rendered scene visibility was inspected.
- Inspected hook, button interaction, dashboard/result, final hold, exported demo frame and exported frame-zero cover.
- Keyframe strip verified that the pointer lands on Generate and process.
- FFprobe: 22.000 seconds, 1920 × 1080, 30/1 fps, 660 video frames and an audio stream. Frame count and duration preserved after poster insertion.
- FFmpeg audio measurement: mean -27.9 dBFS, peak -6.2 dBFS. Music and SFX are present; no narration. This was a measured audio check, not human listening review.
- Successful Hyperframes export: screenshot capture, hardware GPU, two workers, 47.4 seconds. The initial automatic-browser render stalled on a browser download; it was stopped and rerun successfully with installed Chrome.

Details: validation.json, keyframes.json, media-verification.json, render.log, qc-frames/.

## Commands executed for production

From E:/BCI, built source with `.venv/Scripts/python.exe brag-output/build_video.py`. Audio bands were extracted using the Hyperframes creative skill's extract-audio-data.py helper. Dependencies and skill documentation were retrieved locally under artifacts/hyperframes-source and the npm cache. Music and three SFX were copied from the brag skill; local Segoe UI fonts and GSAP were bundled for deterministic rendering.

From the composition directory:

```powershell
$env:HYPERFRAMES_NO_TELEMETRY = '1'
npx --yes hyperframes@0.8.149 check --snapshots --json
npx --yes hyperframes@0.8.149 preview --background
npx --yes hyperframes@0.8.149 check --at 1.8,5.9,6.05,11,15.9,20.8 --json
npx --yes hyperframes@0.8.149 keyframes . --selector '#pointer' --shot ../pointer-proof.png --layout strip --from 5.1 --to 6.1 --samples 4 --json
npx --yes hyperframes@0.8.149 snapshot --at 0,6.05,21.966 --output ../qc-frames
$env:HYPERFRAMES_BROWSER_PATH = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
npx --yes hyperframes@0.8.149 render --quality high --fps 30 --workers 2 --output ../brag.mp4
```

From E:/BCI, `.venv/Scripts/python.exe brag-output/finalize_video.py` extracted the poster, inserted it into frame zero, and asserted output properties using FFmpeg/FFprobe. The helper contains the exact media commands. Rebuilding index.html requires the existing project signal_examples.json and extracted music audio-data.json.

Preview: http://localhost:3002/#project/composition while the local server is running. Stop it from composition/ with `npx --yes hyperframes@0.8.149 preview --stop`.

## Audio credits

Music: Happy Beats / Business Moves vol. 12 by ende.app, supplied with the brag skill. SFX: Kenney CC0 — ui/click2, impactSoft_medium_001 and impactSoft_medium_004. Audio reactivity modulates background grid opacity only, never the scientific signal values.
