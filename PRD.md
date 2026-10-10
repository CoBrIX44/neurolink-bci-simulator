# Product Requirements Document (PRD)
## NeuroLink — Educational Brain-Computer Interface Simulator

**Version:** 1.0 | **Runtime:** Python 3.12 | **Class:** CE-SE-A | **Team:** 2

## 1. Executive summary
NeuroLink is a local educational web app demonstrating a simplified Brain-Computer Interface (BCI) signal-processing pipeline. It generates synthetic EEG-like waveforms, filters them, extracts frequency-domain features, classifies them into one of two illustrative labels, and visualizes the process in a dashboard. It is designed for a Biology for Engineers experiential-learning assignment.

**Scientific boundary:** The MVP uses generated signals, not human EEG. `left` and `right` are artificial demo labels, not evidence of a person's intention. This is not a medical device and must not be described as mind-reading or clinically validated.

## 2. Problem and goals
Real EEG hardware and data collection add cost and complexity to a classroom demonstration. A local simulator lets students explore signal processing without a headset.
Goals:
- Demonstrate signal generation → filtering → feature extraction → classification → simulated output.
- Show raw and filtered waveforms together.
- Display named features and the predicted demo label.
- Run locally on Python 3.12 with no paid API, cloud account, or credentials.
- Include automated tests and accurate limitations.

## 3. Non-goals
- Live EEG headset integration in the MVP.
- Diagnosis, treatment, rehabilitation, or clinical claims.
- Actual thought/intent decoding.
- Production real-time BCI.
- Comprehensive motion-artifact removal.
- Cloud hosting, accounts, analytics, telemetry, or paid APIs.
- Using synthetic accuracy as evidence of real-world BCI performance.

## 4. Users and stories
Primary users are undergraduate students presenting the project; secondary users are instructors and classroom audiences.
- As a student, I can select a demo class and generate a waveform.
- I can compare raw and filtered traces to explain filtering.
- I can inspect feature values and understand how classification works.
- I can see the prediction and model outputs.
- I can run the project locally without hardware or credentials.
- I receive actionable errors if the model is missing or inputs are invalid.

## 5. MVP requirements
### F-01 Synthetic signal generation (P0)
Generate a 2-second signal at 256 Hz for labels `left` and `right`, with noise and deliberately distinct frequency patterns. Support deterministic seeds and validate parameters. Default output must contain 512 samples and a matching time axis.

### F-02 Filtering (P0)
Apply a Butterworth band-pass filter from 1–40 Hz using second-order sections and zero-phase offline filtering. Preserve valid input shape and produce finite values. Explain that this does not remove all motion artifacts and is not a real-time streaming implementation.

### F-03 Feature extraction (P0)
Remove the mean, compute a real FFT, and calculate mean spectral power in 1–12 Hz and 12–40 Hz bands. Features must have stable names/order and finite values; empty bands must not silently yield NaN.

### F-04 Training (P0)
Create a reproducible balanced synthetic dataset. Use a stratified train/test split with fixed random state. Train a scikit-learn pipeline using `StandardScaler` and `LogisticRegression`; persist with joblib to a predictable project-relative path. Print held-out metrics labelled as synthetic-data-only.

### F-05 Dashboard (P0)
Build a Streamlit app titled “NeuroLink — BCI Simulator”. Let the user select `left` or `right` and click a button to generate/process a signal. Plot raw and filtered traces using Plotly; display named feature values, predicted demo command, and model output scores. Keep the disclaimer visible and show helpful errors.

### F-06 Learning content (P0)
Include “How it works” and limitations sections explaining synthetic data, arbitrary amplitude, interpretation of model outputs, and motion artifacts.

### F-07 Simulated cursor (P2, optional)
Only after P0 passes, optionally map `left` to decrement and `right` to increment a cursor position in [0,100]. Persist state across Streamlit reruns and label this as a simulation.

## 6. Technical requirements
- Python 3.12; NumPy, SciPy, scikit-learn, joblib, Streamlit, Plotly, pytest.
- Modular, testable code; useful type hints/docstrings.
- Reproducible seeds for tests and training data.
- Project-relative model paths.
- Local-only operation; no data transmission or secrets.
- `.gitignore` for venvs, caches, and generated artifacts.
- Clear errors for invalid inputs and missing model.
- README with setup, train, run, and test commands.

## 7. Signal specification
- Sampling rate: 256 samples/second.
- Default duration: 2 seconds / 512 samples.
- Filter: Butterworth 1–40 Hz, SOS, zero-phase offline filtering.
- Features: mean power for 1–12 Hz and 12–40 Hz.
- Classifier: standardized logistic regression.
- Labels: `left`, `right`, strictly artificial demo labels.
These are educational choices, not universal or clinical EEG settings.

## 8. UX requirements
- Prominent “Educational prototype using simulated EEG signals — not live brain data” notice.
- X-axis “Time (seconds)”; Y-axis “Amplitude (arbitrary units)”.
- Feature names instead of an unlabeled array.
- Raw and filtered traces easy to compare.
- Do not imply that the selected class is the user's actual intention.
- Do not rely on color alone to communicate information.

## 9. Risks and mitigations
| Risk | Mitigation |
|---|---|
| Synthetic data mistaken for real EEG | Persistent disclaimer and explicit labels |
| High synthetic accuracy overinterpreted | Label metrics synthetic-only |
| Filter claimed to remove all artifacts | Explain artifacts may overlap useful frequencies |
| Missing model causes crash | Actionable instruction to train first |
| Working directory breaks model loading | Use project-relative paths |
| Scope expands to hardware too early | Keep hardware and real datasets out of MVP |

## 10. Deliverables
1. Working local Streamlit app.
2. Modular generation, processing, feature, dataset, training, and inference code.
3. Automated tests.
4. Setup/run/test README.
5. Science and limitations guide.
6. Synthetic-only evaluation output.
7. Optional cursor demo if time permits.
8. Implementation notes containing actual tests, limitations, and deviations.

## 11. Definition of done
- Fresh Python 3.12 environment installs dependencies.
- Training saves a model and prints synthetic-only metrics.
- App launches and processes both labels.
- Raw/filtered plots, named features, prediction, and model outputs are visible.
- Tests pass or failures are documented with evidence.
- Disclaimers are clear.
- README commands are accurate and implementation notes report actual verification.

## 12. Future work (not MVP)
A documented open EEG dataset, comparison of artifact-handling approaches, additional classifiers, or real-time hardware can be considered only as a separately scoped extension. If real data is added, cite its source/license, avoid data leakage, use held-out evaluation, and report limitations.
