"""Screen 01 — Introduction / Landing View for NeuroLink."""
import streamlit as st
from ui_theme import render_html
from views.common import render_header, render_disclaimer_banner, render_footer


def render_landing_view() -> None:
    """Render the approved Stitch Introduction / Landing Page."""
    render_header(current_page="landing")

    landing_html = """
    <main>
      <!-- Hero Section -->
      <section style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 3rem; align-items: center; padding-bottom: 3rem; border-bottom: 1px solid #CCD6D0;">
        <!-- Left Editorial Copy -->
        <div style="flex: 1.2;">
          <div style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.25rem 0.75rem; border-radius: 3px; background: #E5EEE7; color: #173F3A; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; border: 1px solid rgba(23,63,58,0.2); margin-bottom: 1.25rem;">
            <span class="material-symbols-outlined" style="font-size: 15px; color: #79B6A5;">waves</span>
            Interactive Computational Neuroscience
          </div>

          <h1 class="text-display-lg" style="color: #173F3A; margin: 0 0 1.25rem 0;">
            What happens between a brain signal and a digital command?
          </h1>

          <p class="text-body-lg" style="color: #252D2B; opacity: 0.9; margin-bottom: 2rem; max-width: 620px;">
            Explore the science behind brain-computer interfaces through an interactive simulation of neural signal processing and machine learning. From 256 Hz synthetic electrophysiology to zero-phase Butterworth filtering and logistic regression classification.
          </p>

          <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 1rem; margin-bottom: 2.5rem;">
            <a href="?page=experiment-studio" target="_self" class="neurolink-btn-primary">
              <span>Launch Experiment Studio</span>
              <span class="material-symbols-outlined" style="font-size: 18px; color: #79B6A5;">science</span>
            </a>

            <a href="?page=learn-bci" target="_self" class="neurolink-btn-secondary">
              <span>Read Scientific Primer</span>
              <span class="material-symbols-outlined" style="font-size: 16px;">menu_book</span>
            </a>
          </div>

          <!-- Instrument specs strip -->
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; padding-top: 1.5rem; border-top: 1px solid rgba(204,214,208,0.7);">
            <div>
              <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #64748B; display: block; text-transform: uppercase;">SAMPLING SPEC</span>
              <strong style="font-family: 'JetBrains Mono', monospace; font-size: 1.25rem; color: #173F3A; display: block;">256 Hz</strong>
              <span style="font-size: 0.75rem; color: #64748B;">512 samples / 2.0s</span>
            </div>
            <div>
              <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #64748B; display: block; text-transform: uppercase;">FILTER TOPOLOGY</span>
              <strong style="font-family: 'JetBrains Mono', monospace; font-size: 1.25rem; color: #173F3A; display: block;">1–40 Hz</strong>
              <span style="font-size: 0.75rem; color: #64748B;">Butterworth band-pass</span>
            </div>
            <div>
              <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #64748B; display: block; text-transform: uppercase;">MODEL PIPELINE</span>
              <strong style="font-family: 'JetBrains Mono', monospace; font-size: 1.125rem; color: #173F3A; display: block;">StandardScaler</strong>
              <span style="font-size: 0.75rem; color: #64748B;">Logistic Regression</span>
            </div>
          </div>
        </div>

        <!-- Right Visual Column: Conceptual Neural Lattice -->
        <div style="flex: 0.9;">
          <div style="background: rgba(229, 238, 231, 0.4); border: 1px solid #CCD6D0; border-radius: 4px; padding: 0.75rem; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
            <div style="position: relative; aspect-ratio: 4/3; border-radius: 3px; overflow: hidden; background: #173F3A; display: flex; align-items: center; justify-content: center;">
              <!-- Embedded Precision SVG Neural Visualization -->
              <svg viewBox="0 0 400 300" style="width: 100%; height: 100%; background: #112B27;">
                <!-- Subtle grid -->
                <defs>
                  <pattern id="hero-grid" width="40" height="30" patternUnits="userSpaceOnUse">
                    <path d="M 40 0 L 0 0 0 30" fill="none" stroke="#1D3E39" stroke-width="0.8"/>
                  </pattern>
                </defs>
                <rect width="400" height="300" fill="url(#hero-grid)" />

                <!-- Waveform Streams -->
                <path d="M 0 150 Q 50 110, 100 150 T 200 150 T 300 150 T 400 150" fill="none" stroke="#79B6A5" stroke-width="2.5" opacity="0.85"/>
                <path d="M 0 170 Q 70 210, 140 170 T 280 170 T 400 170" fill="none" stroke="#D98B62" stroke-width="1.8" opacity="0.8"/>
                <path d="M 0 130 Q 30 80, 70 130 T 150 130 T 230 130 T 310 130 T 400 130" fill="none" stroke="#E5EEE7" stroke-width="1" stroke-dasharray="3 3" opacity="0.5"/>

                <!-- Synaptic Nodes -->
                <g fill="#79B6A5">
                  <circle cx="100" cy="150" r="5" />
                  <circle cx="200" cy="150" r="6" />
                  <circle cx="300" cy="150" r="5" />
                  <circle cx="140" cy="170" r="4" fill="#D98B62"/>
                  <circle cx="280" cy="170" r="5" fill="#D98B62"/>
                </g>
                <!-- Connections -->
                <line x1="100" y1="150" x2="140" y2="170" stroke="#79B6A5" stroke-width="1" stroke-dasharray="2 2" opacity="0.7"/>
                <line x1="200" y1="150" x2="280" y2="170" stroke="#79B6A5" stroke-width="1" stroke-dasharray="2 2" opacity="0.7"/>
              </svg>

              <!-- Telemetry Overlays -->
              <div style="position: absolute; top: 0.75rem; left: 0.75rem; background: rgba(23, 63, 58, 0.92); color: #F4F1E9; padding: 0.35rem 0.65rem; border-radius: 3px; font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; border: 1px solid rgba(121, 182, 165, 0.4); display: flex; align-items: center; gap: 0.5rem;">
                <span style="width: 6px; height: 6px; border-radius: 50%; background: #79B6A5;"></span>
                <span>SYNTH_ARRAY // CHAN_01 (C3/C4)</span>
              </div>
              <div style="position: absolute; bottom: 0.75rem; right: 0.75rem; background: rgba(23, 63, 58, 0.92); color: #F4F1E9; padding: 0.35rem 0.65rem; border-radius: 3px; font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; border: 1px solid rgba(23, 63, 58, 0.4);">
                <span>SPECTRAL ENERGY: 8 Hz / 22 Hz</span>
              </div>
            </div>

            <!-- Visual Caption -->
            <div style="padding: 0.75rem 0.25rem 0.25rem 0.25rem; display: flex; align-items: center; justify-content: space-between; font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #64748B;">
              <span>FIGURE 1.0 — Conceptual Neural Lattice</span>
              <span style="color: #173F3A; font-weight: 600;">Offline Simulated Domain</span>
            </div>
          </div>
        </div>
      </section>

      <!-- Scientific Disclaimer Banner -->
      <section style="margin-top: 2rem;">
        <div class="neurolink-disclaimer-box">
          <span class="material-symbols-outlined" style="font-size: 22px; color: #173F3A; shrink: 0; margin-top: 2px;">verified_user</span>
          <div style="flex: 1;">
            <div class="neurolink-disclaimer-title">Scientific Transparency & Pedagogical Disclaimer</div>
            <p class="neurolink-disclaimer-text">
              This is an educational simulator using synthetic EEG-like signals, not live brain data. LEFT and RIGHT are artificial demonstration labels. It does not read thoughts, measure human intentions, or provide medical or clinical predictions.
            </p>
          </div>
          <a href="?page=learn-bci#limitations" target="_self" style="font-weight: 600; color: #173F3A; font-size: 0.8125rem; white-space: nowrap; text-decoration: underline; margin-left: auto;">Read Full Limits</a>
        </div>
      </section>

      <!-- System Architecture: Five-Stage Pipeline Section -->
      <section style="padding: 3rem 0; border-bottom: 1px solid #CCD6D0;">
        <div style="max-width: 680px; margin-bottom: 2.5rem;">
          <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #79B6A5; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 0.5rem;">SYSTEM ARCHITECTURE</span>
          <h2 class="text-headline-xl" style="color: #173F3A; margin: 0 0 0.75rem 0;">
            The Complete Five-Stage BCI Simulation Pipeline
          </h2>
          <p class="text-body-md" style="color: #475569; margin: 0;">
            Understand how mathematical transformations turn stochastic microvolt fluctuations into discrete binary control vectors.
          </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
          <!-- Card 1: Signal Processing -->
          <article class="neurolink-card" style="display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="width: 2.5rem; height: 2.5rem; border-radius: 3px; background: #E5EEE7; display: flex; align-items: center; justify-content: center; color: #173F3A; margin-bottom: 1.25rem; border: 1px solid rgba(23,63,58,0.2);">
                <span class="material-symbols-outlined" style="font-size: 20px;">filter_alt</span>
              </div>
              <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #64748B; letter-spacing: 0.04em; display: block; margin-bottom: 0.25rem;">STAGE 01 & 02</span>
              <h3 class="text-headline-md" style="color: #173F3A; margin: 0 0 0.75rem 0;">Signal Processing & Butterworth Filtering</h3>
              <p class="text-body-sm" style="color: #475569; line-height: 1.55; margin-bottom: 1.5rem;">
                Synthetic time series synthesis with physiological baseline drift and 50/60 Hz line noise. Filtered via a 1–40 Hz 4th-order zero-phase Butterworth band-pass filter using SciPy.
              </p>
            </div>
            <div style="padding-top: 1rem; border-top: 1px solid rgba(204,214,208,0.7); display: flex; align-items: center; justify-content: space-between; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;">
              <span style="color: #79B6A5; font-weight: 600;">Zero-phase filtfilt</span>
              <a href="?page=signal-processing" target="_self" class="neurolink-action-link">
                <span>Explore Filter</span>
                <span class="material-symbols-outlined" style="font-size: 14px;">arrow_forward</span>
              </a>
            </div>
          </article>

          <!-- Card 2: Feature Extraction -->
          <article class="neurolink-card" style="display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="width: 2.5rem; height: 2.5rem; border-radius: 3px; background: #E5EEE7; display: flex; align-items: center; justify-content: center; color: #173F3A; margin-bottom: 1.25rem; border: 1px solid rgba(23,63,58,0.2);">
                <span class="material-symbols-outlined" style="font-size: 20px;">analytics</span>
              </div>
              <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #64748B; letter-spacing: 0.04em; display: block; margin-bottom: 0.25rem;">STAGE 03</span>
              <h3 class="text-headline-md" style="color: #173F3A; margin: 0 0 0.75rem 0;">Frequency-Domain Feature Extraction</h3>
              <p class="text-body-sm" style="color: #475569; line-height: 1.55; margin-bottom: 1.5rem;">
                Fast Fourier Transform (FFT) analysis computing mean spectral power across two critical neurological bands: 1–12 Hz (Mu rhythm) and 12–40 Hz (Beta rhythm).
              </p>
            </div>
            <div style="padding-top: 1rem; border-top: 1px solid rgba(204,214,208,0.7); display: flex; align-items: center; justify-content: space-between; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;">
              <span style="color: #D98B62; font-weight: 600;">2 Spectral Features</span>
              <a href="?page=signal-processing" target="_self" class="neurolink-action-link">
                <span>View Spectra</span>
                <span class="material-symbols-outlined" style="font-size: 14px;">arrow_forward</span>
              </a>
            </div>
          </article>

          <!-- Card 3: Machine Learning Inference -->
          <article class="neurolink-card" style="display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="width: 2.5rem; height: 2.5rem; border-radius: 3px; background: #E5EEE7; display: flex; align-items: center; justify-content: center; color: #173F3A; margin-bottom: 1.25rem; border: 1px solid rgba(23,63,58,0.2);">
                <span class="material-symbols-outlined" style="font-size: 20px;">psychology</span>
              </div>
              <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #64748B; letter-spacing: 0.04em; display: block; margin-bottom: 0.25rem;">STAGE 04 & 05</span>
              <h3 class="text-headline-md" style="color: #173F3A; margin: 0 0 0.75rem 0;">Logistic Regression & Simulated Command</h3>
              <p class="text-body-sm" style="color: #475569; line-height: 1.55; margin-bottom: 1.5rem;">
                Scikit-learn StandardScaler normalization and Logistic Regression separating synthetic LEFT (accentuating ~8 Hz) and RIGHT (accentuating ~22 Hz) with simulated cursor deflection.
              </p>
            </div>
            <div style="padding-top: 1rem; border-top: 1px solid rgba(204,214,208,0.7); display: flex; align-items: center; justify-content: space-between; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;">
              <span style="color: #173F3A; font-weight: 600;">Binary Decision</span>
              <a href="?page=classification-lab" target="_self" class="neurolink-action-link">
                <span>Open Classifier</span>
                <span class="material-symbols-outlined" style="font-size: 14px;">arrow_forward</span>
              </a>
            </div>
          </article>
        </div>
      </section>

      <!-- Interactive Workbench CTA Banner -->
      <section style="margin-top: 3rem; background: #173F3A; color: #F4F1E9; border-radius: 4px; padding: 2.5rem; box-shadow: 0 4px 12px rgba(23,63,58,0.15);">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2.5rem; align-items: center;">
          <div>
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #79B6A5; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 0.5rem;">EXPERIENTIAL BENCH</span>
            <h2 class="text-display-lg" style="color: #F4F1E9; font-size: 2.25rem; margin: 0 0 1rem 0;">
              Step directly into the Experiment Studio
            </h2>
            <p class="text-body-md" style="color: rgba(244, 241, 233, 0.85); margin-bottom: 1.75rem; max-width: 540px;">
              Adjust random seeds, choose artificial motor imagery classes, calibrate time windows, and inspect real-time waveforms on a high-resolution scientific oscilloscope canvas.
            </p>
            <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 1rem;">
              <a href="?page=experiment-studio" target="_self" class="neurolink-btn-warm">
                <span class="material-symbols-outlined" style="font-size: 18px;">play_circle</span>
                <span>Open Experiment Studio</span>
              </a>
              <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: rgba(244, 241, 233, 0.6);">
                No live EEG headset required • 100% in-browser simulation
              </span>
            </div>
          </div>

          <div style="background: rgba(17, 47, 43, 0.8); border: 1px solid rgba(121, 182, 165, 0.3); border-radius: 4px; padding: 1.5rem; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;">
            <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(121, 182, 165, 0.2); padding-bottom: 0.75rem; margin-bottom: 1rem;">
              <span style="color: #79B6A5; text-transform: uppercase;">Quick Parameters</span>
              <span style="color: #D98B62; font-weight: 600;">PRE-CONFIGURED</span>
            </div>
            <dl style="display: grid; row-gap: 0.65rem; margin: 0;">
              <div style="display: flex; justify-content: space-between;">
                <dt style="color: rgba(244, 241, 233, 0.7);">Sampling Rate</dt>
                <dd style="font-weight: 600; color: #F4F1E9; margin: 0;">256 Hz</dd>
              </div>
              <div style="display: flex; justify-content: space-between;">
                <dt style="color: rgba(244, 241, 233, 0.7);">Signal Duration</dt>
                <dd style="font-weight: 600; color: #F4F1E9; margin: 0;">2.00 Seconds</dd>
              </div>
              <div style="display: flex; justify-content: space-between;">
                <dt style="color: rgba(244, 241, 233, 0.7);">Total Points</dt>
                <dd style="font-weight: 600; color: #F4F1E9; margin: 0;">512 samples</dd>
              </div>
              <div style="display: flex; justify-content: space-between;">
                <dt style="color: rgba(244, 241, 233, 0.7);">Bandpass Range</dt>
                <dd style="font-weight: 600; color: #79B6A5; margin: 0;">1.0 – 40.0 Hz</dd>
              </div>
              <div style="display: flex; justify-content: space-between;">
                <dt style="color: rgba(244, 241, 233, 0.7);">Class Proxies</dt>
                <dd style="font-weight: 600; color: #D98B62; margin: 0;">LEFT (~8Hz) / RIGHT (~22Hz)</dd>
              </div>
            </dl>
          </div>
        </div>
      </section>
    </main>
    """
    render_html(landing_html)
    render_footer()
