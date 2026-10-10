# Decisions and Scientific Limitations
- Working title: NeuroLink — BCI Simulator.
- Local educational prototype for Biology for Engineers.
- Python 3.12, Streamlit UI, synthetic signal source.
- 256 Hz, 2 seconds, Butterworth 1–40 Hz offline filter, mean power bands 1–12 and 12–40 Hz, standardized logistic regression.
- `left`/`right` are generated categories only.

Out of scope: live headset, diagnosis/treatment, thought-reading, clinical claims, production real-time BCI, complete artifact removal, cloud, accounts, telemetry, paid APIs.

Required caveats:
1. Signals are synthetic, not brain activity or electrode recordings.
2. Labels are not ground-truth motor imagery.
3. High synthetic accuracy does not demonstrate real-world BCI performance.
4. Model scores do not measure actual human intent.
5. Band-pass filtering attenuates out-of-band components but cannot remove all motion, eye, muscle, electrode, or mains artifacts; some overlap useful frequencies.
6. Zero-phase filtering uses future samples and is not directly suitable for streaming.
7. Frequency bands are pedagogical, not universal clinical settings.
8. This is not a medical device.

Future real-data extension must use a documented openly accessible dataset, respect license/terms, cite source, prevent leakage, evaluate on held-out data, and describe limitations.
