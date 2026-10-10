# Science and User Guide
A BCI measures neural activity, transforms signals into useful features, interprets those features, and maps a result to an external command. Real EEG pipelines may include electrode acquisition, preprocessing, artifact handling, feature extraction, classification and device control.

This MVP simulates the software stages; it does not measure a person's brain. The generator produces a noisy two-second waveform at 256 samples/second. A 1–40 Hz Butterworth band-pass attenuates components outside the selected range but cannot remove every artifact. Eye, muscle and movement artifacts may overlap useful frequency ranges. The app then calculates mean spectral power in 1–12 Hz and 12–40 Hz and classifies these features into an artificial label.

Demo script:
1. Introduce BCI and the pipeline.
2. Explain that synthetic signals avoid the need for a headset in the MVP.
3. Select a class and process it.
4. Compare raw and filtered waveforms.
5. Explain the two band-power features.
6. Show the predicted label/model outputs.
7. Discuss real EEG variability, artifacts, and why synthetic accuracy is not real BCI accuracy.
8. Present a separate real assistive-technology case study; do not claim the app implements it.

Vocabulary: EEG = recording of voltage differences using electrodes; artifact = unwanted signal contribution; band-pass filter = passes a selected frequency range; feature extraction = turns raw data into measurements; classifier = assigns a label; motion artifact = movement-related signal variation.

## Separate real assistive-technology case study

In the 2012 BrainGate study, two participants with tetraplegia used signals
recorded by implanted intracortical electrodes to control robotic reaching and
grasping. This was an investigational human neural-interface study, not scalp
EEG and not a synthetic demonstration. See Hochberg et al., *Nature* (2012),
[Reach and grasp by people with tetraplegia using a neurally controlled robotic arm](https://pmc.ncbi.nlm.nih.gov/articles/PMC3640850/).

For the classroom, compare the stages: actual implanted neural acquisition,
signal decoding and physical robotic control in that study versus generated
sinusoids, two FFT features and an artificial label in NeuroLink. The study
illustrates an assistive application; NeuroLink does not reproduce its hardware,
algorithms, clinical validation or participant results. Two research participants
do not establish universal effectiveness for people with paralysis.

## Exact implementation choices

The generator emphasizes 8 Hz for `left` and 22 Hz for `right`, adding a weaker
component in the other band, drift and noise. All amplitudes are arbitrary.
The feature calculation is mean `abs(rFFT(x - mean(x)) / N) ** 2` over bins in
`[1,12)` and `[12,40]` Hz. Thus 12 Hz belongs only to the second band. These are
mean powers per FFT bin, not integrated power or power spectral density.
Changing window length changes the bin layout and can change these features.
The app deliberately fixes its window at two seconds.

The balanced training dataset has 400 examples split into 300 training and 100
held-out examples. Only the training split fits the scaler and classifier.
Both sets come from the same easy synthetic generator; the test set is not
evidence of generalization to real people, sessions, electrodes or artifacts.
