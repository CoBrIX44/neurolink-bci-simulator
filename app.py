"""NeuroLink — Educational BCI Simulator dashboard.

Demonstrates a simplified brain–computer interface processing pipeline:
synthetic signal generation → filtering → feature extraction → classification → visualization.
Operates strictly on artificial waveforms, not real EEG or human intentions.
"""
import streamlit as st
from signal_generator import generate_eeg
from processing import filter_eeg
from features import extract_features
from model_utils import predict_command
from dashboard_model import load_dashboard_model
from cursor import move_cursor
from ui_theme import (
    CUSTOM_CSS,
    create_waveform_figure,
    get_feature_comparison_text,
)

# 1. Page Configuration
st.set_page_config(
    page_title="NeuroLink — BCI Simulator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Inject custom scoped CSS for modern scientific workspace
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# 2. Header & Persistent Scientific Disclaimer
st.title("NeuroLink — BCI Simulator")
st.warning("Educational prototype using simulated EEG signals — not live brain data")

st.markdown(
    """
<div class="neurolink-header-subtitle">
    <span class="neurolink-badge">Synthetic Educational Lab</span>
    <span>• 256 Hz Sampling Rate • 2.0 Seconds Duration • 512 Discrete Samples</span>
</div>
<p style="font-size: 0.9375rem; color: #475569; margin: 0.5rem 0 1rem 0; line-height: 1.5;">
    Explore a synthetic waveform through zero-phase digital filtering, frequency-band power feature extraction, and linear classification to an artificial command.
</p>
""",
    unsafe_allow_html=True,
)

# 3. Experiment Setup Controls
st.markdown('<div class="neurolink-section-title">1. Experiment Setup</div>', unsafe_allow_html=True)

ctrl_col1, ctrl_col2, ctrl_col3 = st.columns([1.5, 1.5, 1.2], gap="medium")

with ctrl_col1:
    label = st.selectbox(
        "Artificial signal class",
        ["left", "right"],
        help="Sets generator frequency emphasis (left: ~8 Hz; right: ~22 Hz). This is not human intent.",
    )

with ctrl_col2:
    seed = st.number_input(
        "Reproducible signal seed",
        min_value=0,
        max_value=2**32 - 1,
        value=7,
        step=1,
        help="Deterministic pseudo-random seed controlling noise and harmonic drift.",
    )

with ctrl_col3:
    st.write("")  # Vertical alignment spacer for button
    process = st.button("Generate and process", type="primary", key="process", use_container_width=True)

# Secondary Setup Options: Simulated Cursor
cursor_enabled = st.checkbox(
    "Enable simulated cursor",
    value=False,
    help="Optional visualization demonstrating simulated linear control without physical hardware.",
)

# Check for settings divergence (quiet diff feedback)
if "result" in st.session_state:
    prev_label = st.session_state.result.get("label")
    prev_seed = st.session_state.result.get("seed")
    if label != prev_label or int(seed) != prev_seed:
        st.markdown(
            '<div class="neurolink-diff-notice">'
            '<span>ℹ️</span>'
            '<span><strong>Settings changed:</strong> Currently displaying synthetic '
            f'<code>{prev_label}</code> (seed {prev_seed}). Click <strong>Generate and process</strong> to apply changes.</span>'
            '</div>',
            unsafe_allow_html=True,
        )

# 4. Processing Pipeline Execution
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

# 5. Signal Analysis & Interpretation Display
if "result" in st.session_state:
    res = st.session_state.result

    st.markdown('<div class="neurolink-section-title" style="margin-top: 1.5rem;">2. Signal Analysis</div>', unsafe_allow_html=True)
    st.caption(f"Displayed example: synthetic {res['label']} · seed {res['seed']}")

    # Dark high-contrast waveform viewport
    figure = create_waveform_figure(res["time"], res["raw"], res["filtered"])
    st.plotly_chart(figure, use_container_width=True)
    st.caption("Zoom, pan, or select a legend entry to compare traces. Dotted = raw; solid = filtered.")

    # Interpretation Area: Two Columns
    st.markdown('<div class="neurolink-section-title" style="margin-top: 1.5rem;">3. Feature Extraction & Classification</div>', unsafe_allow_html=True)
    feature_col, output_col = st.columns(2, gap="large")

    with feature_col:
        st.subheader("Named spectral features")
        feature_data = [
            {"Feature": name, "Mean power (arbitrary units²)": value}
            for name, value in res["features"].items()
        ]
        st.table(feature_data)

        # Dynamic explanatory comparison derived from actual run measurements
        comparison_text = get_feature_comparison_text(res["features"], res["label"])
        st.markdown(
            f'<div class="neurolink-comparison-box">'
            f'<strong>Measurement Insight:</strong> {comparison_text}'
            f'</div>',
            unsafe_allow_html=True,
        )

    with output_col:
        st.subheader("Artificial demo output")
        st.metric("Predicted demo command", res["predicted"])

        score_data = [
            {"Artificial class": name, "Model output score": score}
            for name, score in res["scores"].items()
        ]
        st.table(score_data)
        st.caption("Scores are classifier probabilities on generated patterns, not calibrated confidence in human intention.")
else:
    # Purposeful Empty State before first run
    st.markdown(
        """
<div class="neurolink-empty-state">
    <div class="neurolink-empty-title">Ready for Signal Analysis</div>
    <div class="neurolink-empty-desc">
        Select an artificial class and random seed in <strong>Experiment Setup</strong> above, then click 
        <strong>Generate and process</strong> to run synthetic signal generation, zero-phase filtering, 
        spectral feature extraction, and linear classification.
    </div>
</div>
""",
        unsafe_allow_html=True,
    )
    st.info("Select an artificial class and click Generate and process. If no saved model is available, a synthetic demo classifier is prepared automatically.")

# 6. Simulated Cursor (Optional Bounded Display)
if cursor_enabled:
    st.markdown('<div class="neurolink-section-title" style="margin-top: 1.5rem;">Simulated Cursor Control</div>', unsafe_allow_html=True)
    st.subheader("Simulated cursor — no physical device control")
    position = st.session_state.get("cursor_position", 50)
    st.progress(position / 100, text=f"Simulated position: {position} / 100")
    st.caption("Each successful Generate and process click moves 10 units using the prediction. Left decreases; right increases. Ordinary reruns do not move it.")
    if st.button("Reset simulated cursor", key="reset_cursor"):
        st.session_state.cursor_position = 50
        st.rerun()

# 7. Pedagogical Explanations & Scientific Limitations (Progressive Disclosure)
st.markdown('<div class="neurolink-section-title" style="margin-top: 2rem;">Scientific Documentation</div>', unsafe_allow_html=True)

with st.expander("How it works", expanded=False):
    st.markdown(
        """1. **Generate:** two seconds of synthetic sinusoids, drift and noise. Left emphasizes 8 Hz; right emphasizes 22 Hz. Amplitude is arbitrary, not measured voltage.
2. **Filter:** fourth-order Butterworth 1–40 Hz band-pass in second-order sections, applied forward and backward for zero phase.
3. **Extract:** subtract the mean, compute a real FFT, and average squared normalized FFT magnitudes in [1,12) and [12,40] Hz. The 12 Hz bin belongs only to the second band; these are mean powers per bin, not integrated power or a PSD.
4. **Classify:** a StandardScaler and logistic regression learn deliberately different generated patterns. The scaler is fitted only on the training split. Evaluation uses held-out synthetic examples."""
    )

with st.expander("Scientific limitations", expanded=False):
    st.markdown(
        """- No headset, electrode recording, real EEG, motor-imagery validation or thought-reading is implemented. Left/right are arbitrary generated categories.
- High synthetic accuracy does not demonstrate real-world BCI performance; the model sees the same generator family during training and evaluation.
- Filtering cannot remove all motion, eye, muscle, electrode or mains artifacts. Artifacts may overlap useful frequencies.
- Zero-phase filtering uses future samples and is offline, not a real-time streaming solution; short windows also have edge effects.
- Frequency bands are pedagogical choices, not universal clinical settings. This prototype is not a medical device and is not diagnostic or clinically validated."""
    )
