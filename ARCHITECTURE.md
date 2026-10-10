# Architecture
## Stack
Python 3.12, NumPy, SciPy, scikit-learn, joblib, Streamlit, Plotly, pytest. No MNE or real EEG dataset in MVP.

## Suggested tree
```text
bci-project/
├── app.py
├── signal_generator.py
├── processing.py
├── features.py
├── dataset.py
├── train_model.py
├── model_utils.py
├── requirements.txt
├── README.md
├── .gitignore
├── tests/
│   ├── test_signal_generator.py
│   ├── test_processing.py
│   ├── test_features.py
│   └── test_model.py
└── docs/
    ├── IMPLEMENTATION_NOTES.md
    └── SCIENCE_AND_USER_GUIDE.md
```

## Data flow
User chooses `left`/`right` → generate 2-second signal at 256 Hz → 1–40 Hz Butterworth SOS zero-phase filter → mean spectral power features in 1–12 and 12–40 Hz → StandardScaler + LogisticRegression → prediction and model scores → Streamlit/Plotly output.

## Module responsibilities
- `signal_generator.py`: `generate_eeg(label, duration=2.0, sampling_rate=256, seed=None)`, returns time axis and 1-D synthetic signal. Validate inputs and document arbitrary amplitude.
- `processing.py`: `filter_eeg(signal, sampling_rate=256)`, validate shape, finite values, sampling rate and length; preserve shape; helpful ValueErrors.
- `features.py`: remove mean; real FFT; mean spectral power in 1–12 and 12–40 Hz; stable feature order; no silent NaNs.
- `dataset.py`: balanced, reproducible dataset with deterministic seed derivation.
- `train_model.py`: stratified split, fixed random state, scaler + logistic regression, synthetic-only metrics, joblib persistence.
- `model_utils.py`: project-relative model path, helpful missing-model error, testable prediction helper.
- `app.py`: visible synthetic-data disclaimer; selector and process button; raw/filtered chart; named features; prediction and model scores; “How it works” and limitations; helpful errors.

## Signal assumptions
256 Hz, 2 seconds, 512 samples. Demo classes use distinct synthetic patterns plus noise. Filter is an educational offline choice, not a universal EEG prescription.

## UX and security
Label x-axis in seconds and y-axis in arbitrary units. Scores are model outputs, not calibrated human-intention confidence. No secrets, user accounts, external APIs, or transmission. Keep model paths independent of current working directory.
