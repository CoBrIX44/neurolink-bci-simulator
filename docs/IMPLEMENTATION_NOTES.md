# Implementation notes — 9 October 2026

## Follow-up — 10 October 2026: optional hosted deployment

The user chose Streamlit Community Cloud after a Vercel entrypoint mismatch.
Their deployment log reports Python 3.14.8, whereas this project targets 3.12.
The supplied log ends at dependency resolution and does not prove the ultimate
cause of the “in the oven” delay. Recommended recreating the Streamlit deployment
with Python 3.12 explicitly selected (a reboot does not switch Python versions).

Fixed the independent first-use model issue: `dashboard_model.py` loads an
existing local artifact, or lazily caches a synthetic classifier trained in
memory when the artifact is absent. `train_model(path=None)` skips all filesystem
writes, so concurrent sessions do not race over model files. Corrupt artifacts
still surface errors. The original `load_model` missing-file contract and CLI
training/persistence behavior remain unchanged. Hosted mode is now an explicit
user-requested extension to the original local-only scope, documented in README.

Executed `.\.venv\Scripts\python.exe -m pytest -q`: **58 passed in 12.51 s**.
New checks cover both labels with no artifact, one cached training call, and
no file writes during in-memory training. Cloud success has not been verified;
these changes are local and have not been committed or pushed by the assistant.

## Workspace inspection and scope

Read every original Markdown specification and extracted/read the text in
`PRD.docx` using .NET ZipFile/XML. Both PRDs agree. The original workspace
contained eleven specification files and no application code. `git status
--short` reported that the folder is not a Git repository. No ancestor/project
AGENTS.md was found at the inspected E: locations. All supplied files are
preserved without modification.

`py -0p` found Python 3.12, 3.13 and 3.14. The system default was 3.14.3;
the new `.venv` explicitly uses Python 3.12.10. No cloud, paid APIs, credentials,
real EEG data, hardware drivers, or telemetry were added. Dependency downloads
are required only for installation. App processing and model persistence are
local. Streamlit is configured for loopback and disabled usage statistics.

## Decisions and deviations

- Followed the suggested flat module architecture, adding shared `validation.py`.
- Specified the previously ambiguous 12 Hz boundary as `[1,12)` and `[12,40]`,
  counting it once. Feature power is `abs(rFFT(centered) / N)**2`, averaged
  per band, without one-sided doubling; it is not a PSD or integrated power.
- Generator uses 8/22 Hz patterns and a weaker alternate component, random
  phase/amplitude, Gaussian noise, 0.3 Hz drift and 60 Hz interference.
  Custom sampling rates must exceed 120 Hz to represent that interference.
  Filter/features independently require a rate above 80 Hz. Generation rejects
  fractional sample counts and caps arrays at one million samples.
- Fourth-order SOS Butterworth filter; forward/backward zero-phase application.
  It requires at least 28 samples and retains offline/edge-effect caveats.
- Saved joblib artifact wraps the pipeline with schema/feature metadata and
  synthetic evaluation. JSON metrics are also saved alongside it. Trusted local
  model files only; no model-upload feature.
- A displayed result persists across control reruns and is labelled with its
  original class/seed. A failed processing attempt clears stale output.
- Initial broad dependency ranges caused prolonged pip resolver backtracking;
  that installation was interrupted. Direct packages and pandas were pinned
  before retrying installation for a reproducible Python 3.12 environment.
  The pinned attempt hit a files.pythonhosted.org read timeout; a retry with
  `--timeout 120 --retries 5` downloaded NumPy but remained slow on SciPy and
  was interrupted. A temporary helper under ignored `artifacts/` downloaded
  compatible wheels concurrently from official PyPI URLs and verified every
  wheel against the SHA-256 digest in PyPI metadata. No TLS validation was
  disabled and no alternative package mirror was used. A redundant diagnostic
  curl download was interrupted and its partial wheel removed.
- The classroom guide adds a cited real implanted-BCI case study, explicitly
  separate from this app. Original specification documents remain untouched.

## Verification

Python 3.12.10 on Windows; results actually observed:

| Check | Result |
|---|---|
| Syntax compilation | Passed, exit 0 |
| Installed requirements from verified local wheels | Passed, exit 0 |
| `pip check` | No broken requirements found |
| Initial P0 pytest run | 44 passed in 8.43 s |
| P0 rerun after browser-found Plotly compatibility fix | 44 passed in 2.84 s |
| First optional-cursor run | 55 passed, 1 failed: test selected reset button by position |
| Final run after using explicit button keys | **56 passed in 2.93 s**, exit 0 |
| Default training | Saved model and JSON metrics; 300 train / 100 test, 50 test examples per class |
| Synthetic held-out evaluation | Accuracy 1.0; confusion matrix `[[50,0],[0,50]]`; both class precision/recall/F1 1.0 |
| Server launch | Streamlit served `http://127.0.0.1:8501` |
| HTTP health | `/_stcore/health` returned `ok` |
| Effective config | `browser.gatherUsageStats=False`, `server.address=127.0.0.1` |
| Browser interaction | Both classes processed; raw/filtered traces, labelled axes, features, predictions, scores and disclaimer observed |
| Browser cursor | Enabled at 50; synthetic left processing changed it to 40 |
| Model loading from a different working directory | Loaded default project-relative artifact successfully |

Browser testing found that `width="stretch"` was treated as a deprecated
Plotly keyword by Streamlit 1.50. Replaced it with `use_container_width=True`;
the warning disappeared and the P0 tests passed again before cursor work began.
The optional cursor was added only after that P0 gate. Its new test initially
selected the main-area reset button instead of the sidebar process button;
explicit widget keys corrected the test. No unresolved test failure remains.

Screenshot evidence: `artifacts/dashboard.jpg`. AppTest additionally verified
missing/corrupt model handling, invalid processing inputs, clearing stale
results on failure, trace configuration, and state persistence. The local
server was left running for the user after verification. Browser checks were
performed in the Codex in-app browser, including its narrow-panel layout;
this is not an exhaustive cross-browser or accessibility certification.

## Commands actually executed

Inspection used `Get-Location`, `rg --files`, `Get-ChildItem -Force`,
`Get-Content` on all specifications, `py -0p`, `python --version`, and
`git status --short` (the latter failed because no Git repository exists).
The DOCX was read through .NET ZipFile and XML text extraction.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip install --timeout 120 --retries 5 -r requirements.txt
.\.venv\Scripts\python.exe artifacts\download_wheels.py
$verifiedWheels = Get-ChildItem -LiteralPath 'E:\BCI\artifacts\wheels' -Filter '*.whl' | Select-Object -ExpandProperty FullName
& .\.venv\Scripts\python.exe -m pip install --no-index --no-deps $verifiedWheels
.\.venv\Scripts\python.exe -m pip install --no-index --find-links artifacts\wheels -r requirements.txt
.\.venv\Scripts\python.exe -m compileall -q app.py validation.py signal_generator.py processing.py features.py dataset.py model_utils.py train_model.py tests
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe train_model.py
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m streamlit run app.py --server.port 8501
(Invoke-WebRequest -Uri http://127.0.0.1:8501/_stcore/health).Content
.\.venv\Scripts\python.exe -m pip list --format=freeze --exclude pip | Set-Content -Encoding utf8 requirements-lock.txt
```

The standard installation command was attempted twice (resolver interruption,
then download timeout). The extended-timeout attempt was interrupted after
NumPy downloaded. The final local-wheel requirements installation succeeded
with normal dependency resolution, after installing the available wheels with
`--no-deps`; `pip check` then confirmed the complete environment. All 47 wheels
were downloaded and checksum verified by the temporary setup helper.

Additional diagnostics used `pip --version`, global Python 3.12 `pip list`,
`pip cache list/info`, `curl.exe -I --max-time 20` for PyPI endpoints and
`Invoke-RestMethod` on official PyPI metadata. `pip freeze` was initially used
to save the environment, then replaced by `pip list --format=freeze` so the
lock file contains portable version pins rather than local wheel URLs.
Python one-liners checked effective Streamlit configuration and loaded the
default model from the system temporary working directory. Browser verification
used the computer-use tools, not a fabricated browser test log.

## Created files

- Application: `app.py`, `signal_generator.py`, `processing.py`, `features.py`,
  `dataset.py`, `train_model.py`, `model_utils.py`, `validation.py`, `cursor.py`.
- Setup: `requirements.txt`, `requirements-lock.txt`, `.gitignore`,
  `.streamlit/config.toml`.
- Tests: `tests/test_signal_generator.py`, `tests/test_processing.py`,
  `tests/test_features.py`, `tests/test_model.py`, `tests/test_app.py`,
  `tests/test_cursor.py`.
- Documentation: `README.md`, `docs/SCIENCE_AND_USER_GUIDE.md`, this file.
- Generated local outputs: `.venv/`, `models/neurolink.joblib`,
  `models/neurolink.metrics.json`, ignored `artifacts/` with setup downloads,
  the temporary download helper and browser screenshot. Original specifications
  were preserved.

## Limitations

Synthetic generator separability is intentional; synthetic accuracy says nothing
about decoding human intent or real EEG generalization. No patient, headset or
real recording was tested. Model outputs are not calibrated human-intention
confidence. Artifact removal is incomplete and filtering is offline. Browser
rendering and automated checks are different forms of verification and are
reported separately. Windows is the tested platform; other OS setup is guidance.
