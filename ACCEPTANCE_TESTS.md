# Acceptance Criteria
- Python 3.12 environment installs requirements without credentials or paid services.
- Default signal is 2 seconds at 256 Hz = 512 samples; time axis aligns.
- Fixed seed gives reproducible generation; invalid labels/parameters fail helpfully.
- Filter preserves shape and finite values; invalid input fails helpfully.
- Feature extraction returns two named finite features and handles empty bins explicitly.
- Dataset is reproducible and balanced; split is stratified and fixed-seed.
- Model uses StandardScaler + LogisticRegression; train script saves to project-relative path and labels metrics synthetic-only.
- App launches with `streamlit run app.py`; both classes can be processed; raw and filtered plots, axes/units, features, prediction and model outputs appear.
- Disclaimer remains visible; missing model and processing errors are actionable.
- Optional cursor stays in [0,100] and is labelled simulated.
- Automated tests cover generator, filter, features, dataset balance/reproducibility, model train/load/predict, and optional cursor.
- Final report lists actual commands, tests, pass/fail, app launch status, unmet criteria and deviations. Never fabricate test results.

Manual smoke test: fresh venv → install requirements → `python train_model.py` → verify model saved → `streamlit run app.py` → process both labels → inspect plots and disclaimer → stop app.
