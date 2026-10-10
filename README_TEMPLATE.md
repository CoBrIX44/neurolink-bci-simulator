# NeuroLink — BCI Simulator
Educational local-first BCI pipeline demo using synthetic signals. Not live EEG, not a medical device, and not thought-reading.

## Setup (Windows PowerShell)
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```
If activation is blocked, run the venv interpreter directly:
```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```
Train: `python train_model.py`
Run: `streamlit run app.py`
Test: `python -m pytest -q`

Pipeline: synthetic waveform → 1–40 Hz filter → two band-power features → logistic-regression classifier → dashboard.
Metrics are synthetic-only. Filtering does not remove all artifacts. Read the PRD and all supporting docs before scope changes.
