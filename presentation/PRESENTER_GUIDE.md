# NeuroLink — Team 2 presenter guide

Target duration: 12–15 minutes plus questions. Roles below are assigned responsibilities for preparation and presentation, not a claim of individually verified past work. Rehearse and confirm ownership as a team.

## 1. NeuroLink
Presenter: Aditya Dugar

Introduce Team 2 and the Biology for Engineers experiential-learning project. Explain that the goal is to learn the software stages of a BCI without a headset. Say clearly that all displayed signals are generated and that left/right are artificial labels. The presentation moves from biology to the processing pipeline, a demonstration, and the limits of what the result proves.

## 2. Team 2 · contribution & presentation plan
Presenter: All members

These are assigned responsibilities, not a historical authorship claim. Each member should understand their module, rehearse the explanation, and review the associated code or evidence. Aditya frames the biology; Kushal explains signals; Prince covers filtering and limitations; Raunak covers features and learning; Vijaya demonstrates and validates; Yashas connects the case study and learning outcomes. Use this table to organize rehearsal.

## 3. The learning challenge
Presenter: Aditya Dugar

Our learning question is how a noisy time-domain signal becomes a compact representation and a command. Real acquisition would require equipment and experimental controls beyond this prototype. A simulator makes the stages observable and repeatable. Explain success in terms of an understandable pipeline, reproducibility and honest boundaries, not a clinical performance target.

## 4. Biology first: what a BCI measures
Presenter: Aditya Dugar

A real BCI measures neural activity and maps selected patterns to an output. EEG measures electrical potential differences through electrodes; it is affected by the recording setup and unwanted signal contributions. Our app does not perform that acquisition step. Make the distinction before showing any waveform so the audience does not mistake synthetic sinusoids for recordings. Hand over to Kushal to explain how the simulation replaces acquisition.

## 5. The complete software pipeline
Presenter: Kushal Chaudhary

Walk from left to right through the pipeline. Every example uses 512 samples. Filtering returns the same number of samples; feature extraction reduces that waveform to two numbers. The trained classifier maps those numbers to an artificial category. The Streamlit dashboard shows the intermediate evidence rather than hiding it behind a final label. Name NumPy, SciPy and scikit-learn as implementation tools, without treating a software library as biological validation.

## 6. Create two deliberately distinct patterns
Presenter: Kushal Chaudhary

These native charts contain actual outputs from generate_eeg using seed 7, not stock EEG images. Left emphasizes 8 Hz and right 22 Hz. The generator adds a weaker alternate component, 0.3 Hz drift, 60 Hz interference and Gaussian noise with randomized phase and amplitude. At 256 samples per second for two seconds, the output has 512 samples. Explain that the deliberately different patterns make classification easy; a fixed seed makes the example repeatable.

## 7. Filter the signal, not every artifact
Presenter: Prince Jatheen Rout

The chart compares the actual raw and filtered left example at seed 7. Explain the fourth-order Butterworth band-pass, represented as second-order sections. The algorithm runs forward and backward to produce zero-phase output. This uses future samples and therefore is an offline demonstration. Filtering attenuates out-of-band content but cannot distinguish an artifact inside the useful band from desired content. Edge effects are also possible in this short window.

## 8. Reduce 512 samples to two features
Presenter: Raunak Bothra

First subtract the mean, then calculate the real FFT. For each positive-frequency bin, square the magnitude normalized by the sample count. Average those values in each band. We choose a nonoverlapping convention: 1 inclusive to 12 exclusive, then 12 through 40 inclusive. These are mean powers per FFT bin, not integrated power or a PSD. The chart uses actual processed seed-7 examples. Explain that the relative power distribution gives the classifier useful separation.

## 9. Train a reproducible classifier
Presenter: Raunak Bothra

The dataset has 200 examples in each class. A fixed-seed stratified split preserves balance: 300 examples for training and 100 for testing. StandardScaler is fitted on the training split only, preventing test statistics from entering training. Logistic regression learns the separation between the two synthetic feature patterns. A local joblib artifact can be loaded later; on a fresh hosted deployment the dashboard can build a cached in-memory synthetic model. Probabilities remain model outputs, not confidence about human intent.

## 10. Validation: what the results demonstrate
Presenter: Vijaya Rupesh N

The saved seed-42 training report contains 100 test examples: 50 per class, all correctly classified. Report the 100% figure only with the synthetic-only qualification. These classes were designed to be different, so this is not comparable to a clinical BCI result. Automated tests cover parameter validation, signal determinism, filter behavior, FFT band boundaries, dataset balance, saved models, dashboard interactions, model fallback and cursor bounds. Cite the actual local test run reported in the presenter guide.

## 11. An interactive dashboard makes the stages visible
Presenter: Vijaya Rupesh N

This slide is a schematic of the implemented dashboard, not a screenshot. The sidebar selects the artificial class, reproducible seed and optional cursor. The output contains a Plotly raw/filtered chart, named feature values, prediction and class scores. The displayed result retains its original seed and label until processed again. Missing local model files trigger cached in-memory synthetic training; other failures are shown as actionable errors. The synthetic-data notice is always included in the app.

## 12. Live demonstration · about 90 seconds
Presenter: Vijaya Rupesh N

Before presenting, open the local dashboard or the working Streamlit deployment. Start at seed 7 with the cursor disabled. Generate left and point out the slower dominant oscillation and larger low-band feature. Generate right and compare the faster oscillation and higher upper-band feature. Enable the cursor and reset to 50: process left once for 40, then right once for 50. Changing controls alone should not move the cursor. If the network is unavailable, run locally using the command on this slide; the preceding charts provide a backup.

## 13. Real assistive technology: the BrainGate study
Presenter: Yashas L Rao

Keep this case study clearly separate from NeuroLink. Hochberg and colleagues reported in 2012 that two participants with tetraplegia controlled robotic reaching and grasping using implanted motor-cortex electrode arrays. This was an investigational intracortical neural-interface study, not scalp EEG. It illustrates the motivation for assistive BCI work but does not validate our classifier or simulator. Do not generalize a two-participant research demonstration to universal effectiveness. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3640850/

## 14. Scientific boundaries we must keep visible
Presenter: Prince Jatheen Rout

Use this slide to prevent overclaiming during questions. We have no measured neural signal, no verified motor-imagery label and no clinical validation. Filtering is not complete artifact removal and zero-phase filtering is not streaming. Synthetic train and test samples come from the same generator family. A future real-EEG project would require a documented licensed dataset, careful leakage controls such as subject/session separation as appropriate, and evaluation on genuinely held-out data. It would be a separate study.

## 15. Experiential learning: build, observe, explain
Presenter: Yashas L Rao

Frame these as learning takeaways and a reflection plan rather than invented student testimonials. Each member should be able to explain a transformation using evidence from the app. Ask the team what changes when seed changes, why a filter cannot remove every artifact, and why a high test score can be misleading. Close by restating that the outcome is a working and testable educational signal-processing pipeline. Invite questions on either the engineering implementation or the distinction from real BCI research.

## 16. References & project resources
Presenter: Yashas L Rao / all members

Use the repository and local documentation for implementation-specific statements, and the cited primary research for the assistive case study. The class should not treat framework documentation as evidence of biological efficacy. The app deployment was reported successful by the team during setup; the deck does not claim an independent cloud availability test. Confirm the current hosted link from the repository About section before the presentation. Thank the audience and invite questions.

## Verification record
12 October 2026: `.\.venv\Scripts\python.exe -m pytest -q` returned 58 passed in 3.98 seconds. Charts use actual seed-7 generated examples. Evaluation uses the saved seed-42 model report: 100 held-out synthetic examples, all correctly classified. This is not real EEG performance.
