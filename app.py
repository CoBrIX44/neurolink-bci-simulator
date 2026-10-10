"""Local educational dashboard. No real EEG acquisition or intent decoding."""
import plotly.graph_objects as go
import streamlit as st
from signal_generator import generate_eeg
from processing import filter_eeg
from features import extract_features
from model_utils import predict_command
from dashboard_model import load_dashboard_model
from cursor import move_cursor

st.set_page_config(page_title="NeuroLink — BCI Simulator", page_icon="🧠", layout="wide")
st.title("NeuroLink — BCI Simulator")
st.warning("Educational prototype using simulated EEG signals — not live brain data")
st.caption("SYNTHETIC EDUCATIONAL LAB · 256 Hz · 2 seconds · 512 samples")
st.write("Explore a synthetic waveform from generation through filtering, features and an artificial demo command.")

with st.sidebar:
    st.header("Generate a synthetic example")
    label = st.selectbox("Artificial signal class", ["left", "right"])
    seed = st.number_input("Reproducible signal seed", min_value=0, max_value=2**32 - 1, value=7, step=1)
    process = st.button("Generate and process", type="primary", key="process")
    cursor_enabled = st.checkbox("Enable simulated cursor", value=False)
    st.caption("The selected class controls the generator; it is not your intention. Change the seed to explore another waveform.")

if process:
    st.session_state.pop("result", None)
    try:
        model = load_dashboard_model()
        time, raw = generate_eeg(label, seed=int(seed))
        filtered = filter_eeg(raw)
        features = extract_features(filtered)
        predicted, scores = predict_command(model, features)
        if cursor_enabled:
            st.session_state.cursor_position = move_cursor(st.session_state.get("cursor_position", 50), predicted)
        st.session_state.result = dict(time=time, raw=raw, filtered=filtered, features=features,
                                       predicted=predicted, scores=scores, label=label, seed=int(seed))
    except (ValueError, FileNotFoundError, OSError) as exc:
        st.error(str(exc))
    except Exception:
        st.error("Processing failed. Re-train with python train_model.py and check the installed requirements.")

if "result" in st.session_state:
    result = st.session_state.result
    st.caption(f"Displayed example: synthetic {result['label']} · seed {result['seed']}")
    figure = go.Figure()
    figure.add_trace(go.Scatter(x=result["time"], y=result["raw"], name="Raw synthetic signal",
                               line=dict(color="#8795A5", width=1, dash="dot")))
    figure.add_trace(go.Scatter(x=result["time"], y=result["filtered"], name="Filtered synthetic signal",
                               line=dict(color="#087E8B", width=2)))
    figure.update_layout(title="Raw and filtered synthetic waveforms", xaxis_title="Time (seconds)",
                         yaxis_title="Amplitude (arbitrary units)", hovermode="x unified",
                         legend=dict(orientation="h"), margin=dict(l=20, r=20, t=60, b=20))
    st.plotly_chart(figure, use_container_width=True)
    st.caption("Zoom, pan, or select a legend entry to compare traces. Dotted = raw; solid = filtered.")
    feature_col, output_col = st.columns(2)
    with feature_col:
        st.subheader("Named spectral features")
        st.table([{"Feature": name, "Mean power (arbitrary units²)": value}
                  for name, value in result["features"].items()])
    with output_col:
        st.subheader("Artificial demo output")
        st.metric("Predicted demo command", result["predicted"])
        st.table([{"Artificial class": name, "Model output score": score}
                  for name, score in result["scores"].items()])
        st.caption("Scores are classifier probabilities on generated patterns, not calibrated confidence in human intention.")
else:
    st.info("Select an artificial class and click Generate and process. If no saved model is available, a synthetic demo classifier is prepared automatically.")

if cursor_enabled:
    st.subheader("Simulated cursor — no physical device control")
    position = st.session_state.get("cursor_position", 50)
    st.progress(position / 100, text=f"Simulated position: {position} / 100")
    st.caption("Each successful Generate and process click moves 10 units using the prediction. Left decreases; right increases. Ordinary reruns do not move it.")
    if st.button("Reset simulated cursor", key="reset_cursor"):
        st.session_state.cursor_position = 50
        st.rerun()

with st.expander("How it works", expanded=True):
    st.markdown("""1. **Generate:** two seconds of synthetic sinusoids, drift and noise. Left emphasizes 8 Hz; right emphasizes 22 Hz. Amplitude is arbitrary, not measured voltage.
2. **Filter:** fourth-order Butterworth 1–40 Hz band-pass in second-order sections, applied forward and backward for zero phase.
3. **Extract:** subtract the mean, compute a real FFT, and average squared normalized FFT magnitudes in [1,12) and [12,40] Hz. The 12 Hz bin belongs only to the second band; these are mean powers per bin, not integrated power or a PSD.
4. **Classify:** a StandardScaler and logistic regression learn deliberately different generated patterns. The scaler is fitted only on the training split. Evaluation uses held-out synthetic examples.""")
with st.expander("Scientific limitations", expanded=True):
    st.markdown("""- No headset, electrode recording, real EEG, motor-imagery validation or thought-reading is implemented. Left/right are arbitrary generated categories.
- High synthetic accuracy does not demonstrate real-world BCI performance; the model sees the same generator family during training and evaluation.
- Filtering cannot remove all motion, eye, muscle, electrode or mains artifacts. Artifacts may overlap useful frequencies.
- Zero-phase filtering uses future samples and is offline, not a real-time streaming solution; short windows also have edge effects.
- Frequency bands are pedagogical choices, not universal clinical settings. This prototype is not a medical device and is not diagnostic or clinically validated.""")
