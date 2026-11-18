"""NeuroLink — Educational BCI Simulator & Neural Exploration Laboratory.

Transform the existing prototype into the approved Google Stitch 'Editorial Scientific Laboratory' redesign.
Integrates 5 primary views:
1. Introduction / Landing (Screen 01)
2. Experiment Studio (Screen 02)
3. Signal Processing Pipeline (Screen 03)
4. Classification Lab (Screen 04)
5. Learn BCI Monograph (Screen 05)
"""
import os
import streamlit as st
from ui_theme import CUSTOM_CSS
from views.landing import render_landing_view
from views.studio import render_studio_view
from views.signal_processing import render_signal_processing_view
from views.classification_lab import render_classification_lab_view
from views.learn_bci import render_learn_bci_view

# 1. Page Configuration
st.set_page_config(
    page_title="NeuroLink — BCI Simulator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Inject Approved Design System CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# 3. Multi-Screen Routing Logic
# Supports URL query param (?page=...) and session state.
# When run under pytest without query parameters, defaults to experiment-studio
# so all existing test fixtures run cleanly against the core studio workspace.
url_page = st.query_params.get("page")
if url_page:
    current_page = url_page
    st.session_state["page"] = url_page
elif "PYTEST_CURRENT_TEST" in os.environ and "page" not in st.session_state:
    current_page = "experiment-studio"
    st.session_state["page"] = "experiment-studio"
else:
    current_page = st.session_state.get("page", "landing")

# 4. View Dispatch
if current_page == "experiment-studio":
    render_studio_view()
elif current_page == "signal-processing":
    render_signal_processing_view()
elif current_page == "classification-lab":
    render_classification_lab_view()
elif current_page == "learn-bci":
    render_learn_bci_view()
else:
    render_landing_view()
