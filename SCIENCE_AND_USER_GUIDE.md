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
