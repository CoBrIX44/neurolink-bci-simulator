# Codex Instructions
Read this file and all project documents before coding. `PRD.docx`/`PRD.md` is the source of truth; architecture, implementation plan, acceptance tests, and decisions files support it. If conflicts exist, follow the PRD and record them in `docs/IMPLEMENTATION_NOTES.md`.

1. Inspect the repository, Python version, files, and git status. Preserve unrelated work.
2. If empty, scaffold the architecture in `ARCHITECTURE.md`.
3. Implement a working vertical slice first: synthetic signal → filter → features → classifier → plots/prediction.
4. Target Python 3.12. Keep code modular and understandable to undergraduate students.
5. Add automated tests, run them, and fix failures.
6. Do not add paid APIs, cloud dependencies, telemetry, credentials, or data transmission.
7. Do not claim untested functionality works; never invent test results.
8. Keep the synthetic-data disclaimer visible in the app and docs.
9. After P0 requirements pass, consider the optional cursor demo.
10. Update README and `docs/IMPLEMENTATION_NOTES.md` with actual commands, tests, results, deviations, and known limitations.

Scientific rules: this MVP does not acquire real EEG. `left`/`right` are artificial labels, not validated human intentions. The app is not medical, diagnostic, or clinically validated. A 1–40 Hz filter does not remove every artifact. Zero-phase filtering is offline, not a streaming solution.

First action: inspect workspace and provide a short plan, then implement without waiting for confirmation unless genuinely blocked. Finish with a truthful summary and test report.
