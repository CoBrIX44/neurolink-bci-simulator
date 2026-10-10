# Implementation Plan
1. **Inspect:** preserve existing work; verify Python 3.12; set up requirements, .gitignore, tests.
2. **Generator:** deterministic `left`/`right` synthetic signal; test 512 samples, time axis, repeatability, invalid inputs.
3. **Filter:** 1–40 Hz Butterworth SOS zero-phase filter; test shape, finite output, invalid inputs.
4. **Features:** two named band-power features; test finite values and stable order.
5. **Dataset/model:** reproducible balanced dataset; stratified split; scaler + logistic regression; save/load/predict.
6. **UI:** Streamlit app with raw/filtered plot, features, predicted label, model outputs, disclaimers, and error states.
7. **Optional cursor:** only after all P0 requirements pass; state in [0,100], left/right move in opposite directions.
8. **Verification:** run tests, training, app smoke test where possible; update README and implementation notes with actual evidence.

Priority: P0 working local MVP and scientific honesty; P1 tests/reproducibility/docs; P2 optional cursor. Do not scope creep into hardware, real-time acquisition, cloud, or real EEG datasets.
