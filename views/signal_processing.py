"""Screen 03 — Signal Processing View for NeuroLink.

Presents the complete 5-stage mathematical electrophysiology pipeline:
1. Synthetic signal generation (256 Hz, 512 samples)
2. Butterworth 1–40 Hz band-pass filtering (zero-phase SOS filtfilt)
3. Frequency-domain feature extraction (mean spectral power in 1–12 Hz and 12–40 Hz)
4. Classification preparation (StandardScaler normalization)
5. Simulated output (1D kinematic cursor deflection)
"""
import streamlit as st
from ui_theme import render_html
from views.common import render_header, render_footer


def render_signal_processing_view() -> None:
    """Render the approved Stitch Signal Processing Pipeline page."""
    render_header(current_page="signal-processing", page_title="SIGNAL PROCESSING PIPELINE")

    render_html(
        """
        <main>
          <!-- Page Hero -->
          <div style="border-bottom: 1px solid #CCD6D0; padding-bottom: 2rem; margin-bottom: 2rem;">
            <div style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.25rem 0.75rem; border-radius: 3px; background: #E5EEE7; color: #173F3A; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; border: 1px solid rgba(23,63,58,0.2); margin-bottom: 1rem;">
              <span class="material-symbols-outlined" style="font-size: 16px; color: #79B6A5;">timeline</span>
              Signal Conditioning &amp; Feature Extraction Architecture
            </div>
            <h1 class="text-display-lg" style="color: #173F3A; margin: 0 0 1rem 0;">
              The Mathematical Transformation of Neural Voltages
            </h1>
            <p class="text-body-lg" style="color: #252D2B; opacity: 0.85; max-width: 780px; margin: 0;">
              Step through the five mathematical stages that bridge raw synthetic analog voltages to binary classification. Designed for engineering undergraduates to grasp frequency filtering and spectral estimation without sacrificing algorithmic fidelity.
            </p>
          </div>
        """
    )

    # State for selected pipeline stage inspector
    if "selected_stage" not in st.session_state:
        st.session_state.selected_stage = 1

    render_html(
        """
        <!-- Interactive 5-Stage Pipeline Mapper -->
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1.25rem;">
          <div>
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #79B6A5; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; display: block;">INTERACTIVE PIPELINE</span>
            <h2 class="text-headline-xl" style="color: #173F3A; margin: 0;">Five-Stage BCI Signal Architecture</h2>
          </div>
          <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #64748B;">Select a stage to inspect its transformation</span>
        </div>
        """
    )

    # Stage tab selector buttons
    stage_cols = st.columns(5, gap="small")
    stages = [
        (1, "01 // SYNTHESIS", "Signal Generation", "Sine superposition + Pink noise"),
        (2, "02 // CONDITIONING", "Butterworth 1–40 Hz", "Zero-phase forward-backward"),
        (3, "03 // SPECTRAL", "Feature Extraction", "1–12 Hz & 12–40 Hz Power"),
        (4, "04 // INFERENCE", "Logistic Regression", "StandardScaler + Sigmoid"),
        (5, "05 // OUTPUT", "Simulated Output", "1D Kinematic Deflection"),
    ]

    for idx, (stage_num, tag, title, desc) in enumerate(stages):
        with stage_cols[idx]:
            is_active = (st.session_state.selected_stage == stage_num)
            border_style = "2px solid #173F3A" if is_active else "1px solid #CCD6D0"
            bg_style = "#E5EEE7" if is_active else "#F4F1E9"
            btn_label = f"Stage {stage_num}"
            if st.button(
                f"{tag}\n\n{title}",
                key=f"stage_btn_{stage_num}",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ):
                st.session_state.selected_stage = stage_num
                st.rerun()

    # Dynamic Stage Detail Inspector Card
    selected = st.session_state.selected_stage

    stage_data = {
        1: {
            "badge": "STAGE 01",
            "title": "Synthetic Signal Generation",
            "desc": "Creates a 512-sample (2.0s) synthetic electrophysiology signal sampled at 256 Hz. It injects a primary sinusoid depending on chosen class (~8 Hz for LEFT or ~22 Hz for RIGHT), combined with 0.3 Hz slow DC baseline drifts and broad Gaussian pink noise.",
            "math": "V(t) = A·sin(2πf t + φ) + Drift(t) + η(t)",
            "backend": "signal_generator.generate_eeg (numpy.sin + np.random.normal)",
            "svg_color": "#D98B62",
            "svg_path": "M 0 60 Q 30 10, 60 70 T 120 40 T 180 80 T 240 30 T 300 65",
            "viz_label": "Raw Voltage: Stochastic Noise + Drift",
        },
        2: {
            "badge": "STAGE 02",
            "title": "Butterworth 1–40 Hz Zero-Phase Filtering",
            "desc": "Applies a 4th-order Butterworth bandpass filter using Second-Order Sections (SOS). The signal is filtered forward, reversed, and filtered backward via scipy.signal.sosfiltfilt to eliminate group delay and preserve true latency of oscillatory waves.",
            "math": "H(s) = 1 / [Π (s - s_k)], y(t) = filtfilt(SOS, x(t))",
            "backend": "processing.filter_eeg (scipy.signal.butter + sosfiltfilt)",
            "svg_color": "#173F3A",
            "svg_path": "M 0 60 Q 30 35, 60 85 T 120 45 T 180 75 T 240 45 T 300 60",
            "viz_label": "Filtered Waveform: Isolated Sensorimotor Rhythm",
        },
        3: {
            "badge": "STAGE 03",
            "title": "Frequency-Domain Feature Extraction",
            "desc": "Computes real Fast Fourier Transform (rFFT) after subtracting the mean. Evaluates mean spectral power across two discrete pedagogical bands: [1, 12) Hz and [12, 40] Hz. The 12 Hz boundary is counted exactly once into the high band to avoid leakage.",
            "math": "P_band = (1 / |B|) · Σ_{f ∈ B} |rFFT(x - x̄)_f / N|²",
            "backend": "features.extract_features (numpy.fft.rfft)",
            "svg_color": "#79B6A5",
            "svg_path": "M 10 100 L 50 100 L 50 30 L 100 30 L 100 100 L 160 100 L 160 65 L 220 65 L 220 100 L 290 100",
            "viz_label": "Spectral Bands: Mean Power per Frequency Bin",
        },
        4: {
            "badge": "STAGE 04",
            "title": "StandardScaler Normalization & Logistic Regression",
            "desc": "Standardizes the 2D feature vector using training-split mean and variance: z = (x - μ) / σ. Logistic regression applies linear weights and a sigmoid activation function to compute class probabilities.",
            "math": "P(RIGHT | x) = 1 / [1 + exp(-(w^T z + b))]",
            "backend": "model_utils.predict_command (StandardScaler + LogisticRegression)",
            "svg_color": "#173F3A",
            "svg_path": "M 10 110 L 140 110 Q 150 110, 160 60 Q 170 10, 180 10 L 290 10",
            "viz_label": "Sigmoid Decision Curve: P in [0, 1]",
        },
        5: {
            "badge": "STAGE 05",
            "title": "Simulated Cursor Deflection Actuation",
            "desc": "Maps the discrete predicted label into a simulated 1D kinematic actuator. When enabled, a predicted LEFT decrements the position by 10 units; RIGHT increments it by 10 units within bounds [0, 100]. Start position is 50.",
            "math": "pos_{t+1} = clip(pos_t + (-10 if LEFT else +10), 0, 100)",
            "backend": "cursor.move_cursor (bounded stateful position)",
            "svg_color": "#79B6A5",
            "svg_path": "M 10 60 L 290 60 M 150 40 L 150 80 M 190 50 L 190 70",
            "viz_label": "1D Actuator Track: Position ∈ [0, 100]",
        },
    }

    info = stage_data[selected]

    render_html(
        f"""
        <div class="neurolink-card" style="padding: 1.75rem; margin-top: 1rem; margin-bottom: 2.5rem;">
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; align-items: center;">
            <div>
              <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.75rem;">
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; background: #173F3A; color: #F4F1E9; padding: 0.25rem 0.65rem; border-radius: 3px; font-weight: 600;">{info['badge']}</span>
                <h3 class="text-headline-lg" style="color: #173F3A; margin: 0;">{info['title']}</h3>
              </div>
              <p class="text-body-md" style="color: #252D2B; opacity: 0.9; line-height: 1.6; margin-bottom: 1.5rem;">
                {info['desc']}
              </p>
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; padding-top: 1rem; border-top: 1px solid #CCD6D0; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;">
                <div>
                  <span style="color: #64748B; display: block; font-size: 0.6875rem;">MATHEMATICAL FORMULATION</span>
                  <span style="color: #173F3A; font-weight: 600;">{info['math']}</span>
                </div>
                <div>
                  <span style="color: #64748B; display: block; font-size: 0.6875rem;">PYTHON MODULE & METHOD</span>
                  <span style="color: #173F3A; font-weight: 600;">{info['backend']}</span>
                </div>
              </div>
            </div>

            <!-- Mini Stage Output Graphic -->
            <div style="background: rgba(229, 238, 231, 0.4); border: 1px solid #CCD6D0; border-radius: 4px; padding: 1.25rem;">
              <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #64748B; text-transform: uppercase; letter-spacing: 0.04em; display: block; margin-bottom: 0.75rem;">Stage Visual Transformation</span>
              <div style="aspect-ratio: 16/9; background: #F4F1E9; border: 1px solid #CCD6D0; border-radius: 3px; display: flex; align-items: center; justify-content: center; padding: 0.75rem;">
                <svg viewBox="0 0 300 120" style="width: 100%; height: 100%;">
                  <line x1="0" y1="60" x2="300" y2="60" stroke="#CCD6D0" stroke-dasharray="2 2" stroke-width="1"/>
                  <path d="{info['svg_path']}" fill="none" stroke="{info['svg_color']}" stroke-width="2.5"/>
                </svg>
              </div>
              <div style="display: flex; justify-content: space-between; font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #64748B; margin-top: 0.5rem;">
                <span>{info['viz_label']}</span>
                <span style="color: #173F3A; font-weight: 600;">256 Hz Time Base</span>
              </div>
            </div>
          </div>
        </div>
        """
    )

    # In-Depth Scientific Comparison: Filtering & Zero-Phase Processing
    render_html(
        """
        <section style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2.5rem; padding-top: 2rem; border-top: 1px solid #CCD6D0;">
          <!-- Left Column: Scientific Deep-Dive -->
          <div>
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #79B6A5; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 0.25rem;">ELECTROPHYSIOLOGY ENGINEERING</span>
            <h2 class="text-headline-xl" style="color: #173F3A; margin: 0 0 1rem 0;">
              Why 1–40 Hz Zero-Phase Butterworth Filtering?
            </h2>
            <div style="font-size: 0.9375rem; color: #252D2B; line-height: 1.6; display: flex; flex-direction: column; gap: 0.75rem;">
              <p style="margin: 0;">
                In biological electroencephalography (EEG), raw scalp potentials are corrupted by severe physical artifacts:
              </p>
              <ul style="margin: 0; padding-left: 1.25rem; display: flex; flex-direction: column; gap: 0.5rem;">
                <li><strong>Low-frequency drift (&lt;1 Hz):</strong> Galvanic skin impedance shifts, sweating, and slow head movements create large baseline fluctuations that overpower microvolt-scale neural rhythms.</li>
                <li><strong>High-frequency noise (&gt;40 Hz):</strong> Electromyographic (EMG) muscle activity from facial clenching and 50/60 Hz electrical mains hum contaminate the recording.</li>
              </ul>
              <p style="margin: 0;">
                The 4th-order Butterworth band-pass filter isolates the sensorimotor rhythm range (1–40 Hz). Crucially, the simulator executes <strong>zero-phase offline filtering</strong> via SciPy's <code>sosfiltfilt</code>.
              </p>
            </div>

            <!-- Zero Phase Callout -->
            <div style="background: rgba(229, 238, 231, 0.4); border: 1px solid #CCD6D0; border-left: 4px solid #173F3A; border-radius: 4px; padding: 1rem 1.25rem; margin-top: 1.5rem;">
              <strong style="color: #173F3A; display: block; font-size: 0.875rem; margin-bottom: 0.25rem;">The Zero-Phase Tradeoff (filtfilt vs Online Real-Time)</strong>
              <p style="font-size: 0.8125rem; color: #252D2B; margin: 0 0 0.5rem 0; line-height: 1.5;">
                <code>filtfilt</code> processes the input signal forward, reverses the array, and filters backward. This squares the magnitude response and cancels nonlinear phase delay entirely, ensuring peaks do not shift in time.
              </p>
              <div style="display: flex; align-items: center; gap: 0.5rem; font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #D98B62;">
                <span class="material-symbols-outlined" style="font-size: 16px;">warning</span>
                <span>Limitation: Zero-phase requires the entire signal buffer and cannot run instantaneously sample-by-sample in closed-loop live telemetry.</span>
              </div>
            </div>
          </div>

          <!-- Right Column: Spectral Power Band Visualizer -->
          <div class="neurolink-card" style="padding: 1.5rem;">
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #D98B62; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 0.25rem;">FREQUENCY DOMAIN</span>
            <h3 class="text-headline-md" style="color: #173F3A; margin: 0 0 0.5rem 0;">Mean Spectral Power Features</h3>
            <p class="text-body-sm" style="color: #64748B; margin-bottom: 1.25rem;">
              How the classifier separates mental intent into two scalar dimensions.
            </p>

            <div style="display: flex; flex-direction: column; gap: 1rem;">
              <div style="background: rgba(229, 238, 231, 0.35); border: 1px solid #CCD6D0; border-radius: 4px; padding: 1rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                  <strong style="color: #173F3A; font-size: 0.875rem;">Band 01: [1, 12) Hz — Mu Rhythm</strong>
                  <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #79B6A5; font-weight: 600;">8 Hz TARGET</span>
                </div>
                <p style="font-size: 0.8125rem; color: #475569; margin: 0; line-height: 1.45;">
                  Sensorimotor mu rhythms desynchronize (attenuate) during contralateral motor imagery. In this simulator, the synthetic LEFT class deliberately injects an 8 Hz oscillatory component.
                </p>
              </div>

              <div style="background: rgba(229, 238, 231, 0.35); border: 1px solid #CCD6D0; border-radius: 4px; padding: 1rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                  <strong style="color: #D98B62; font-size: 0.875rem;">Band 02: [12, 40] Hz — Beta Rhythm</strong>
                  <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #D98B62; font-weight: 600;">22 Hz TARGET</span>
                </div>
                <p style="font-size: 0.8125rem; color: #475569; margin: 0; line-height: 1.45;">
                  Beta oscillations reflect active cortical processing. The synthetic RIGHT class injects a 22 Hz oscillatory component. The 12 Hz boundary is assigned exclusively to this band.
                </p>
              </div>
            </div>

            <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid #CCD6D0;">
              <a href="?page=experiment-studio" target="_self" class="neurolink-btn-primary" style="display: flex; justify-content: space-between; width: 100%;">
                <span>Test Waveforms in Experiment Studio</span>
                <span class="material-symbols-outlined" style="font-size: 16px;">science</span>
              </a>
            </div>
          </div>
        </section>
        </main>
        """
    )

    render_footer()
