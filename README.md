# NeuroLink — BCI Simulator

**Educational prototype using simulated EEG signals — not live brain data.**
This local Biology for Engineers project generates artificial waveforms, filters
them, extracts two features, and predicts an artificial `left` or `right` label.
It is not thought-reading, a medical device, or a clinically validated system.

## Setup and run (Windows PowerShell, Python 3.12)

Run these commands from the project folder:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe train_model.py
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Open http://127.0.0.1:8501 in your browser. Select an artificial class and seed,
then click **Generate and process**. Hover, zoom or toggle the chart legend to
compare the dotted raw trace with the solid filtered trace. Changing a control
does not replace the displayed example until the button is clicked. Stop the
server with Ctrl+C. No headset, account, API key or paid service is needed.

Optional: enable **simulated cursor** to move a bounded position by 10 units
per successful processing click (predicted left decreases, right increases).
It starts at 50, persists across reruns, stays in [0,100] and has a reset button.
It controls no physical device and is not driven by brain activity.

On macOS/Linux, use `python3.12 -m venv .venv` and `.venv/bin/python` in place of
the Windows interpreter path. These platform-specific commands have not been
verified here.

Dependencies are downloaded during installation. Application processing runs
locally; it has no cloud APIs, analytics or external datasets. Streamlit usage
statistics are disabled and its server binds to loopback via
`.streamlit/config.toml`. Launch from this folder so Streamlit reads that config.
`requirements-lock.txt` records the full environment used for verification;
install with `-r requirements-lock.txt` to use those exact versions.

## Training and evaluation

`train_model.py` creates 200 examples per class, with seed 42 and distinct
per-example seeds, then uses a stratified 75/25 split. StandardScaler is fitted
on training examples only, followed by logistic regression. Training writes
`models/neurolink.joblib` and `models/neurolink.metrics.json` relative to the
source directory, independent of the current working directory. Metrics include
accuracy, precision, recall, F1 and a labelled confusion matrix.

**All evaluation metrics are synthetic-only.** The deliberately separable
generator makes this an easy classification exercise; high scores do not
measure real EEG performance or human intentions. Dashboard probabilities are
model outputs, not calibrated human-intention confidence.

Models are generated locally and ignored by Git. Train before first use; retrain
after changing the generator, feature definitions or dependencies. Load only
trusted locally generated joblib files: the format can execute Python code.
Missing/corrupt models produce a retraining message in the dashboard.

## Pipeline and scientific limits

- Generator: 256 Hz, two seconds, 512 samples. Left emphasizes 8 Hz; right
  emphasizes 22 Hz, with random phase/amplitude, Gaussian noise, 0.3 Hz drift
  and a 60 Hz interference component. These are not electrode recordings.
- Filter: fourth-order Butterworth 1–40 Hz, second-order sections,
  forward/backward zero-phase filtering. It uses future samples, has window
  edge effects and is unsuitable as-is for live streaming.
- Features: subtract the mean, compute `rFFT`, square `abs(FFT / N)`, average
  bins in `[1,12)` and `[12,40]` Hz. Stable names are
  `mean_power_1_12_hz`, `mean_power_12_40_hz`. Values have arbitrary amplitude²
  units; they are neither a PSD nor integrated band power. Empty bands error
  explicitly. The 12 Hz bin is counted only once.
- Classifier: standardized logistic regression trained on generated categories.

Band-pass filtering does not remove all motion, eye, muscle, electrode or mains
artifacts: some overlap useful frequencies. These frequency bands are
pedagogical, not universal EEG or clinical settings. No real EEG acquisition,
motor imagery validation, diagnosis or rehabilitation is implemented.

## Tests

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Tests exercise signal validation and determinism, frequency behavior, feature
normalization/boundaries, balanced datasets, held-out evaluation, persistence,
inference, and Streamlit interactions for both classes and error states.
Cursor tests cover both directions, boundaries, reset and rerun persistence.
See [implementation notes](docs/IMPLEMENTATION_NOTES.md) for actual results.

## Project files and classroom guide

`signal_generator.py`, `processing.py`, `features.py`, `dataset.py`,
`train_model.py`, `model_utils.py` and `validation.py` implement the pipeline.
`app.py` provides the interactive Streamlit dashboard; `tests/` contains pytest
and Streamlit AppTest checks. The supplied specifications are preserved.

Read [the science and demo guide](docs/SCIENCE_AND_USER_GUIDE.md),
[the PRD](PRD.md), and [team deliverables](TEAM_AND_DELIVERABLES.md).
Class CE-SE-A, Team 2. Any real-data extension requires its own documented
source/license, leakage controls, held-out evaluation and limitations.
