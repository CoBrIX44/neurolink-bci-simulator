"""Screen 02 — Experiment Studio View for NeuroLink.

Connects the approved Stitch laboratory interface directly to the real Python backend:
- signal_generator.generate_eeg
- processing.filter_eeg
- features.extract_features
- dashboard_model.load_dashboard_model
- model_utils.predict_command
- cursor.move_cursor
"""
import streamlit as st
from signal_generator import generate_eeg
from processing import filter_eeg
from features import extract_features
from dashboard_model import load_dashboard_model
from model_utils import predict_command
from cursor import move_cursor
from ui_theme import (
    create_waveform_figure,
    compute_signal_metrics,
    get_feature_comparison_text,
    render_html,
)
from views.common import render_header, render_footer


def render_studio_view() -> None:
    """Render the approved Stitch Experiment Studio and connect to real Python backend."""
    # Top navigation header with status pill
    render_header(current_page="experiment-studio", page_title="EXPERIMENT STUDIO")

    # Persistent mandatory scientific disclaimer required by tests & PRD
    st.warning("Educational prototype using simulated EEG signals — not live brain data")

    # Status Strip
    render_html(
        """
        <div class="neurolink-status-strip">
          <div style="display: flex; align-items: center; gap: 1.5rem; flex-wrap: wrap;">
            <span><strong style="color: #64748B; font-size: 0.6875rem;">SAMPLING:</strong> <span style="color: #173F3A; font-weight: 700;">256 Hz</span></span>
            <span><strong style="color: #64748B; font-size: 0.6875rem;">EPOCH WINDOW:</strong> <span style="color: #173F3A; font-weight: 700;">2.00 s (512 samples)</span></span>
            <span><strong style="color: #64748B; font-size: 0.6875rem;">FILTER PASSBAND:</strong> <span style="color: #79B6A5; font-weight: 700;">1.0 – 40.0 Hz</span></span>
          </div>
          <div style="color: #64748B; font-style: italic; font-size: 0.6875rem;">
            Synthesized via NumPy &amp; SciPy filtfilt
          </div>
        </div>
        """
    )

    # 3-Column Workbench Grid
    col_ctrl, col_scope, col_analysis = st.columns([3, 6, 3], gap="medium")

    # =========================================================================
    # LEFT PANEL: EXPERIMENT CONTROLS
    # =========================================================================
    with col_ctrl:
        render_html(
            """
            <div class="neurolink-card-header">
              <span class="neurolink-card-title">
                <span class="material-symbols-outlined" style="font-size: 18px;">tune</span>
                Configuration
              </span>
              <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #64748B;">INPUT MATRIX</span>
            </div>
            """
        )

        # 1. Artificial signal class selection
        label = st.selectbox(
            "Artificial signal class",
            ["left", "right"],
            help="Sets generator frequency emphasis (left: ~8 Hz; right: ~22 Hz). This is not human intent.",
        )

        # 2. Reproducible random seed
        seed = st.number_input(
            "Reproducible signal seed",
            min_value=0,
            max_value=2**32 - 1,
            value=7,
            step=1,
            help="Deterministic pseudo-random seed controlling noise and harmonic drift.",
        )

        # Settings divergence detection
        if "result" in st.session_state:
            prev_label = st.session_state.result.get("label")
            prev_seed = st.session_state.result.get("seed")
            if label != prev_label or int(seed) != prev_seed:
                render_html(
                    '<div class="neurolink-diff-notice">'
                    '<span>ℹ️</span>'
                    '<span><strong>Settings changed:</strong> Currently displaying synthetic '
                    f'<code>{prev_label}</code> (seed {prev_seed}). Click <strong>Generate and process</strong> to apply changes.</span>'
                    '</div>'
                )

        st.write("")
        # 3. Primary Generate and Process Action Button
        process = st.button("Generate and process", type="primary", key="process", use_container_width=True)

        render_html("<hr style='border: none; border-top: 1px solid rgba(204,214,208,0.7); margin: 1rem 0;'>")

        # 4. Optional Simulated Cursor Deflection
        cursor_enabled = st.checkbox(
            "Enable simulated cursor",
            value=False,
            help="Optional visualization demonstrating simulated linear control without physical hardware.",
        )

        if cursor_enabled:
            position = st.session_state.get("cursor_position", 50)
            render_html(
                f"""
                <div style="background: rgba(229, 238, 231, 0.5); border: 1px solid #CCD6D0; border-radius: 4px; padding: 0.75rem; margin-top: 0.5rem; font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem;">
                  <div style="display: flex; justify-content: space-between; color: #64748B; margin-bottom: 0.25rem;">
                    <span>[LEFT 0]</span>
                    <span>CENTER 50</span>
                    <span>[RIGHT 100]</span>
                  </div>
                  <div style="position: relative; height: 1.25rem; background: #F4F1E9; border: 1px solid #CCD6D0; border-radius: 2px; overflow: hidden; display: flex; align-items: center;">
                    <div style="position: absolute; left: 50%; top: 0; bottom: 0; width: 1px; background: #CCD6D0;"></div>
                    <div style="position: absolute; left: calc({position}% - 6px); width: 12px; height: 12px; background: #173F3A; border-radius: 2px; border: 1px solid #79B6A5; transition: left 300ms ease;"></div>
                  </div>
                  <div style="display: flex; justify-content: space-between; margin-top: 0.35rem; color: #173F3A; font-weight: 600;">
                    <span>POS: {position} / 100</span>
                    <span>{'DEFLECTED' if position != 50 else 'CENTERED'}</span>
                  </div>
                </div>
                """
            )
            st.progress(position / 100, text=f"Simulated position: {position} / 100")
            st.caption("Each successful Generate and process click moves 10 units using the prediction. Left decreases; right increases.")
            if st.button("Reset simulated cursor", key="reset_cursor", use_container_width=True):
                st.session_state.cursor_position = 50
                st.rerun()

        # Scientific Guidance Note
        render_html(
            """
            <div style="padding: 0.75rem; background: rgba(229, 238, 231, 0.35); border: 1px solid #CCD6D0; border-radius: 3px; font-size: 0.75rem; color: #475569; margin-top: 1rem; line-height: 1.45;">
              <strong style="color: #173F3A; display: block; margin-bottom: 0.2rem;">Scientific Note:</strong>
              Signal generation uses NumPy sinusoidal superpositions mixed with Gaussian pink noise and high-amplitude baseline drift.
            </div>
            """
        )

    # =========================================================================
    # PIPELINE EXECUTION LOGIC (Deterministic & Session State)
    # =========================================================================
    if process:
        # Clear previous result so failed runs never display stale data
        st.session_state.pop("result", None)
        try:
            model = load_dashboard_model()
            time_sec, raw = generate_eeg(label, seed=int(seed))
            filtered = filter_eeg(raw)
            features = extract_features(filtered)
            predicted, scores = predict_command(model, features)
            if cursor_enabled:
                current_pos = st.session_state.get("cursor_position", 50)
                st.session_state.cursor_position = move_cursor(current_pos, predicted)
            st.session_state.result = dict(
                time=time_sec,
                raw=raw,
                filtered=filtered,
                features=features,
                predicted=predicted,
                scores=scores,
                label=label,
                seed=int(seed),
            )
        except (ValueError, FileNotFoundError, OSError) as exc:
            st.error(str(exc))
        except Exception:
            st.error("Processing failed. Re-train with python train_model.py and check the installed requirements.")

    # =========================================================================
    # CENTER PANEL: LARGE INTERACTIVE WAVEFORM CANVAS
    # =========================================================================
    with col_scope:
        render_html(
            """
            <div class="neurolink-card-header">
              <div>
                <span class="neurolink-card-title">
                  <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #173F3A;"></span>
                  Synthetic Waveform Scope
                </span>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #64748B;">
                  TIME-DOMAIN VOLTAGE TRACE // EPOCH: 0.000s → 2.000s
                </span>
              </div>
            </div>
            """
        )

        if "result" in st.session_state:
            res = st.session_state.result

            # Render real Plotly waveform figure
            figure = create_waveform_figure(res["time"], res["raw"], res["filtered"])
            st.plotly_chart(figure, use_container_width=True)

            # Calculate and render actual physical waveform telemetry metrics
            metrics = compute_signal_metrics(res["raw"], res["filtered"])
            render_html(
                f"""
                <div class="neurolink-metrics-grid">
                  <div class="neurolink-metric-item">
                    <span class="label">Peak-to-Peak</span>
                    <span class="value">{metrics['vpp']}</span>
                  </div>
                  <div class="neurolink-metric-item">
                    <span class="label">RMS Voltage</span>
                    <span class="value">{metrics['rms']}</span>
                  </div>
                  <div class="neurolink-metric-item">
                    <span class="label">Signal Noise Ratio</span>
                    <span class="value">{metrics['snr']}</span>
                  </div>
                  <div class="neurolink-metric-item">
                    <span class="label">Drift Attenuation</span>
                    <span class="value" style="color: #79B6A5;">{metrics['drift']}</span>
                  </div>
                </div>
                """
            )
        else:
            # Purposeful Empty State
            render_html(
                """
                <div class="neurolink-empty-state">
                  <div class="neurolink-empty-title">Laboratory Scope Inactive</div>
                  <div class="neurolink-empty-desc">
                    Select an artificial signal class (LEFT or RIGHT) and seed in <strong>Configuration</strong>, then click 
                    <strong>Generate and process</strong> to synthesize 512 samples through zero-phase digital filtering.
                  </div>
                </div>
                """
            )

    # =========================================================================
    # RIGHT PANEL: ANALYSIS & CLASSIFIER
    # =========================================================================
    with col_analysis:
        render_html(
            """
            <div class="neurolink-card-header">
              <span class="neurolink-card-title">
                <span class="material-symbols-outlined" style="font-size: 18px;">insights</span>
                Analysis
              </span>
              <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #64748B;">OUTPUT STAGE</span>
            </div>
            """
        )

        if "result" in st.session_state:
            res = st.session_state.result

            # 1. Predicted Artificial Class Card
            pred_score = res["scores"].get(res["predicted"], 0.0)
            st.metric("Predicted demo command", res["predicted"])
            st.caption(f"Classifier Output Score: {pred_score:.3f} (Softmax probability)")

            # 2. Model Output Scores
            render_html(
                """
                <span style="font-family: 'Inter', sans-serif; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; color: #475569; display: block; margin: 1rem 0 0.5rem 0;">
                  Model Output Scores
                </span>
                """
            )
            score_data = [
                {"Artificial class": name, "Model output score": score}
                for name, score in res["scores"].items()
            ]
            st.table(score_data)

            # 3. Extracted Spectral Features Table
            render_html(
                """
                <span style="font-family: 'Inter', sans-serif; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; color: #475569; display: block; margin: 1rem 0 0.5rem 0;">
                  Extracted Spectral Features
                </span>
                """
            )
            feature_data = [
                {"Feature": name, "Mean power (arbitrary units²)": value}
                for name, value in res["features"].items()
            ]
            st.table(feature_data)

            # 4. Feature Comparison Measurement Insight
            comparison_text = get_feature_comparison_text(res["features"], res["label"])
            render_html(
                f'<div class="neurolink-comparison-box">'
                f'<strong>Measurement Insight:</strong> {comparison_text}'
                f'</div>'
            )
        else:
            render_html(
                """
                <div style="padding: 1.5rem; text-align: center; color: #64748B; font-size: 0.8125rem; background: rgba(229, 238, 231, 0.3); border: 1px dashed #CCD6D0; border-radius: 4px;">
                  Output telemetry will appear here after triggering signal processing.
                </div>
                """
            )

        # Quick Navigation Links
        render_html(
            """
            <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(204,214,208,0.7); display: flex; flex-direction: column; gap: 0.5rem;">
              <a href="?page=signal-processing" target="_self" class="neurolink-btn-outline">
                <span>Inspect Filter Pipeline</span>
                <span class="material-symbols-outlined" style="font-size: 16px;">arrow_forward</span>
              </a>
              <a href="?page=classification-lab" target="_self" class="neurolink-btn-outline">
                <span>Open Classification Lab</span>
                <span class="material-symbols-outlined" style="font-size: 16px;">psychology</span>
              </a>
            </div>
            """
        )

    # =========================================================================
    # LOWER SECTION: SCIENTIFIC METHODOLOGY & LIMITATIONS
    # =========================================================================
    render_html(
        """
        <section style="margin-top: 2rem; background: rgba(229, 238, 231, 0.35); border: 1px solid #CCD6D0; border-radius: 4px; padding: 1.5rem;">
          <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
            <span class="material-symbols-outlined" style="font-size: 20px; color: #173F3A;">school</span>
            <h3 class="text-headline-sm" style="color: #173F3A; margin: 0;">Scientific Methodology & Backend Specifications</h3>
          </div>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; font-size: 0.8125rem; color: #252D2B; line-height: 1.55;">
            <div>
              <strong style="color: #173F3A; display: block; margin-bottom: 0.25rem;">01 // Synthetic Electrophysiology</strong>
              Signals mimic sensorimotor rhythm desynchronization (ERD/ERS). The 256 Hz time series superimposes target oscillatory sine components on low-frequency baseline drifts (0.3 Hz) and broad Gaussian noise.
            </div>
            <div>
              <strong style="color: #173F3A; display: block; margin-bottom: 0.25rem;">02 // Zero-Phase Filtering</strong>
              SciPy Butterworth bandpass (1–40 Hz, 4th order) operates forward and backward (<code>filtfilt</code>). This preserves waveform peaks at their exact physiological time indices without group delay distortion.
            </div>
            <div>
              <strong style="color: #173F3A; display: block; margin-bottom: 0.25rem;">03 // Feature Normalization</strong>
              Spectral powers in 1–12 Hz and 12–40 Hz bands are extracted and z-scored with <code>StandardScaler</code> before evaluation by Logistic Regression to mimic motor intention detection.
            </div>
          </div>
        </section>
        """
    )

    render_footer()
