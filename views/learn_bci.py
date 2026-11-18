"""Screen 05 — Learn BCI Monograph View for NeuroLink.

Comprehensive educational monograph covering:
- Biophysical origins of EEG and pyramidal neuron post-synaptic potentials
- Real BCI systems vs NeuroLink Simulator comparison
- Clinical & engineering applications (neuroprosthetics, augmentative spellers)
- Scientific & technological limitations (volume conduction, SNR, ITR)
- Official team and academic deliverables metadata from TEAM_AND_DELIVERABLES.md
"""
import streamlit as st
from ui_theme import render_html
from views.common import render_header, render_footer


def render_learn_bci_view() -> None:
    """Render the approved Stitch Learn BCI educational monograph."""
    render_header(current_page="learn-bci", page_title="LEARN BCI MONOGRAPH")

    render_html(
        """
        <main style="max-width: 860px; margin: 0 auto; padding-top: 1rem;">
          <!-- Article Header -->
          <header style="border-bottom: 1px solid #CCD6D0; padding-bottom: 2rem; margin-bottom: 2.5rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #64748B; margin-bottom: 1rem;">
              <span>CURRICULUM SPECIFICATION</span>
              <span>•</span>
              <span>BIOLOGY FOR ENGINEERS</span>
              <span>•</span>
              <span style="color: #173F3A; font-weight: 600;">PEER-REVIEWED PEDAGOGY</span>
            </div>

            <h1 class="text-display-lg" style="color: #173F3A; margin: 0 0 1rem 0;">
              Principles of Brain-Computer Interfaces &amp; Electrophysiology
            </h1>

            <p class="text-body-lg" style="color: #252D2B; opacity: 0.85; line-height: 1.65; margin: 0;">
              An engineering primer on how synchronous neuronal populations generate detectable scalp potentials, the mathematics of digital signal conditioning, and the boundaries between biological reality and synthetic simulators.
            </p>
          </header>

          <!-- Section 01: What is a BCI? -->
          <section style="margin-bottom: 3rem;">
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #79B6A5; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.25rem;">
              01 // THE PARADIGM
            </div>
            <h2 class="text-headline-xl" style="color: #173F3A; margin: 0 0 1rem 0;">
              What is a Brain-Computer Interface?
            </h2>
            <div class="text-body-md" style="color: #252D2B; opacity: 0.9; line-height: 1.65; display: flex; flex-direction: column; gap: 1rem;">
              <p style="margin: 0;">
                A Brain-Computer Interface (BCI) is a direct communication pathway between the central nervous system and an external computational actuator. Unlike conventional human-computer interfaces such as keyboards, touchscreens, or eye trackers, a BCI bypasses the peripheral nervous system and somatic musculature entirely.
              </p>
              <p style="margin: 0;">
                BCIs intercept neurophysiological manifestations of user cognitive states or intentions, convert these microvolt potentials into digital telemetry, extract discriminative spectral or spatial features, and classify them into control commands for neuroprosthetic effectors, communication spellers, or assistive systems.
              </p>
            </div>

            <div style="background: rgba(229, 238, 231, 0.4); border: 1px solid #CCD6D0; border-radius: 4px; padding: 1.25rem; margin-top: 1.5rem;">
              <h4 style="font-family: 'Manrope', sans-serif; font-size: 0.875rem; font-weight: 700; color: #173F3A; margin: 0 0 0.5rem 0;">
                Standard BCI Closed-Loop Architecture:
              </h4>
              <ol style="margin: 0; padding-left: 1.25rem; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #252D2B; display: flex; flex-direction: column; gap: 0.35rem; line-height: 1.5;">
                <li><strong>Signal Acquisition:</strong> Scalp electrodes convert ionic currents in tissue into electric voltages.</li>
                <li><strong>Signal Conditioning:</strong> Analog-to-digital conversion (ADC) and band-pass filtering (1–40 Hz).</li>
                <li><strong>Feature Extraction:</strong> Power spectral density (PSD) computation via Fourier or Welch estimators.</li>
                <li><strong>Pattern Classification:</strong> Supervised machine learning (logistic regression, linear discriminant analysis).</li>
                <li><strong>Feedback &amp; Actuation:</strong> Real-time visual, auditory, or physical feedback closing the sensorimotor loop.</li>
              </ol>
            </div>
          </section>

          <!-- Section 02: How EEG Works -->
          <section style="margin-bottom: 3rem; padding-top: 2rem; border-top: 1px solid #CCD6D0;">
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #79B6A5; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.25rem;">
              02 // BIOPHYSICAL ORIGINS
            </div>
            <h2 class="text-headline-xl" style="color: #173F3A; margin: 0 0 1rem 0;">
              How Electroencephalography (EEG) Works
            </h2>
            <div class="text-body-md" style="color: #252D2B; opacity: 0.9; line-height: 1.65; display: flex; flex-direction: column; gap: 1rem;">
              <p style="margin: 0;">
                Scalp EEG does not measure individual action potentials. Action potentials are brief (~1 millisecond) and spatially localized. Instead, EEG detects <strong>summed post-synaptic potentials (PSPs)</strong> from pyramidal neurons organized perpendicularly to the cortical surface.
              </p>
              <p style="margin: 0;">
                When tens of thousands of pyramidal neurons receive synchronized excitatory or inhibitory synaptic inputs, their extracellular ionic currents generate dipoles. These electric fields conduct passively through cerebrospinal fluid, the skull bone, and scalp tissue—attenuating drastically from millivolts at the cortical surface to faint <strong>5–100 µV</strong> fluctuations at scalp surface electrodes.
              </p>
            </div>

            <!-- Comparison Table: Real EEG vs NeuroLink Simulator -->
            <div class="neurolink-card" style="padding: 1.5rem; margin-top: 1.5rem;">
              <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
                <span class="material-symbols-outlined" style="font-size: 20px; color: #173F3A;">compare_arrows</span>
                <h3 class="text-headline-sm" style="color: #173F3A; margin: 0;">
                  Real BCI Systems vs. The NeuroLink Simulator
                </h3>
              </div>

              <div style="overflow-x: auto;">
                <table style="width: 100%; border-collapse: collapse; font-size: 0.8125rem;">
                  <thead>
                    <tr style="background: #E5EEE7; color: #173F3A; font-family: 'Inter', sans-serif; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.04em;">
                      <th style="padding: 0.65rem 0.75rem; text-align: left; border-bottom: 1px solid #CCD6D0;">DIMENSION</th>
                      <th style="padding: 0.65rem 0.75rem; text-align: left; border-bottom: 1px solid #CCD6D0;">REAL-WORLD BCI</th>
                      <th style="padding: 0.65rem 0.75rem; text-align: left; border-bottom: 1px solid #CCD6D0;">NEUROLINK SIMULATOR</th>
                    </tr>
                  </thead>
                  <tbody style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;">
                    <tr style="border-bottom: 1px solid rgba(204,214,208,0.5);">
                      <td style="padding: 0.65rem 0.75rem; font-weight: 700; color: #173F3A;">Signal Source</td>
                      <td style="padding: 0.65rem 0.75rem;">Cortical post-synaptic potentials</td>
                      <td style="padding: 0.65rem 0.75rem; color: #79B6A5; font-weight: 600;">Synthetic sinusoidal + Gaussian pink noise</td>
                    </tr>
                    <tr style="border-bottom: 1px solid rgba(204,214,208,0.5);">
                      <td style="padding: 0.65rem 0.75rem; font-weight: 700; color: #173F3A;">Amplitude Unit</td>
                      <td style="padding: 0.65rem 0.75rem;">Physical microvolts (5–100 µV)</td>
                      <td style="padding: 0.65rem 0.75rem;">Dimensionless arbitrary units (au)</td>
                    </tr>
                    <tr style="border-bottom: 1px solid rgba(204,214,208,0.5);">
                      <td style="padding: 0.65rem 0.75rem; font-weight: 700; color: #173F3A;">Filtering Mode</td>
                      <td style="padding: 0.65rem 0.75rem;">Causal online filtering (phase delay)</td>
                      <td style="padding: 0.65rem 0.75rem;">Zero-phase offline filtfilt (no delay)</td>
                    </tr>
                    <tr style="border-bottom: 1px solid rgba(204,214,208,0.5);">
                      <td style="padding: 0.65rem 0.75rem; font-weight: 700; color: #173F3A;">Class Labels</td>
                      <td style="padding: 0.65rem 0.75rem;">Subjective mental imagery / intent</td>
                      <td style="padding: 0.65rem 0.75rem; color: #D98B62; font-weight: 600;">Artificial proxies (LEFT: ~8Hz, RIGHT: ~22Hz)</td>
                    </tr>
                    <tr>
                      <td style="padding: 0.65rem 0.75rem; font-weight: 700; color: #173F3A;">Hardware</td>
                      <td style="padding: 0.65rem 0.75rem;">Electrode cap, ADC, bio-amplifier</td>
                      <td style="padding: 0.65rem 0.75rem;">Zero hardware (100% in-browser)</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </section>

          <!-- Section 03: Applications -->
          <section style="margin-bottom: 3rem; padding-top: 2rem; border-top: 1px solid #CCD6D0;">
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #79B6A5; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.25rem;">
              03 // CLINICAL TRANSLATION
            </div>
            <h2 class="text-headline-xl" style="color: #173F3A; margin: 0 0 1rem 0;">
              Real-World Clinical &amp; Assistive Applications
            </h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem;">
              <div class="neurolink-card" style="padding: 1.25rem;">
                <h4 style="font-family: 'Manrope', sans-serif; font-size: 1rem; font-weight: 700; color: #173F3A; margin: 0 0 0.5rem 0;">
                  Neuroprosthetics
                </h4>
                <p class="text-body-sm" style="color: #475569; line-height: 1.55; margin: 0;">
                  Translating motor cortex sensorimotor rhythm modulation directly into multi-axis robotic arm and motorized wheelchair guidance for individuals with tetraplegia.
                </p>
              </div>

              <div class="neurolink-card" style="padding: 1.25rem;">
                <h4 style="font-family: 'Manrope', sans-serif; font-size: 1rem; font-weight: 700; color: #173F3A; margin: 0 0 0.5rem 0;">
                  Augmentative Communication
                </h4>
                <p class="text-body-sm" style="color: #475569; line-height: 1.55; margin: 0;">
                  P300 event-related spellers and steady-state visually evoked potential (SSVEP) communication grids enabling non-verbal communication for ALS patients.
                </p>
              </div>

              <div class="neurolink-card" style="padding: 1.25rem;">
                <h4 style="font-family: 'Manrope', sans-serif; font-size: 1rem; font-weight: 700; color: #173F3A; margin: 0 0 0.5rem 0;">
                  Stroke Neuro-rehabilitation
                </h4>
                <p class="text-body-sm" style="color: #475569; line-height: 1.55; margin: 0;">
                  Contingent sensory electrical stimulation triggering exoskeleton actuation when ipsilateral motor imagery is detected, inducing neuroplastic recovery.
                </p>
              </div>
            </div>
          </section>

          <!-- Section 04: Scientific Limitations -->
          <section id="limitations" style="margin-bottom: 3rem; padding-top: 2rem; border-top: 1px solid #CCD6D0;">
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #D98B62; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.25rem;">
              04 // ETHICAL &amp; TECHNICAL BOUNDARIES
            </div>
            <h2 class="text-headline-xl" style="color: #173F3A; margin: 0 0 1rem 0;">
              Current Scientific &amp; Technological Limitations
            </h2>
            <div class="text-body-md" style="color: #252D2B; opacity: 0.9; line-height: 1.65; display: flex; flex-direction: column; gap: 1rem;">
              <p style="margin: 0;">
                Public media frequently misinterprets BCIs as telepathic mind-reading devices. In scientific reality, non-invasive electroencephalography is constrained by severe fundamental physical limits:
              </p>
              <ul style="margin: 0; padding-left: 1.25rem; display: flex; flex-direction: column; gap: 0.5rem;">
                <li><strong>Volume Conduction:</strong> The poorly conducting human skull acts as a spatial low-pass filter, blurring and spreading electrical currents across scalp sensors. Solving the inverse source-localization problem is mathematically ill-posed without anatomical MRI priors.</li>
                <li><strong>Low Signal-to-Noise Ratio (SNR):</strong> Endogenous background cortical dynamics, sweating impedance shifts, ocular saccades, and electromyographic (jaw clenching) artifacts are orders of magnitude greater than cognitive sensorimotor rhythms.</li>
                <li><strong>Information Transfer Rate (ITR):</strong> Current non-invasive BCI communications peak at approximately 10 to 60 bits per minute—exponentially slower than typing or speech.</li>
              </ul>
            </div>

            <!-- Formal Educational Simulator Disclaimer -->
            <div style="background: rgba(229, 238, 231, 0.6); border: 1px solid #CCD6D0; border-left: 4px solid #173F3A; border-radius: 4px; padding: 1.25rem; margin-top: 1.5rem;">
              <div style="display: flex; align-items: center; gap: 0.5rem; font-family: 'Manrope', sans-serif; font-weight: 700; color: #173F3A; margin-bottom: 0.25rem;">
                <span class="material-symbols-outlined" style="font-size: 20px;">verified_user</span>
                Official Educational Simulator Disclaimer
              </div>
              <p style="font-size: 0.8125rem; color: #252D2B; line-height: 1.55; margin: 0;">
                "This is an educational simulator using synthetic EEG-like signals, not live brain data. LEFT and RIGHT are artificial demonstration labels. It does not read thoughts, measure human intentions, or provide medical or clinical predictions."
              </p>
            </div>
          </section>

          <!-- Section 05: Academic Deliverables & Team -->
          <section style="margin-bottom: 2rem; padding-top: 2rem; border-top: 1px solid #CCD6D0;">
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #79B6A5; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.25rem;">
              05 // ACADEMIC PROVENANCE
            </div>
            <h2 class="text-headline-xl" style="color: #173F3A; margin: 0 0 1rem 0;">
              About the Project
            </h2>

            <div class="neurolink-card" style="padding: 1.5rem; margin-bottom: 1.5rem;">
              <p class="text-body-md" style="color: #252D2B; line-height: 1.6; margin: 0 0 1.25rem 0;">
                <strong>NeuroLink</strong> was developed as an experiential learning capstone project for <em>Biology for Engineers</em> (Class CE-SE-A, Team 2) to provide an open, interactive computational laboratory for signal processing, zero-phase filtering, and linear classification.
              </p>

              <div style="padding-top: 0.75rem; border-top: 1px solid #CCD6D0;">
                <a href="https://github.com/CoBrIX44/neurolink-bci-simulator" target="_blank" rel="noopener" style="display: inline-flex; align-items: center; gap: 0.35rem; color: #173F3A; font-weight: 600; text-decoration: underline; font-size: 0.8125rem;">
                  <span class="material-symbols-outlined" style="font-size: 16px;">open_in_new</span>
                  <span>Inspect GitHub Repository (CoBrIX44/neurolink-bci-simulator)</span>
                </a>
              </div>
            </div>
          </section>
        </main>
        """
    )

    render_footer()
