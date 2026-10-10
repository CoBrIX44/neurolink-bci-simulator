"""Use a local artifact when present, otherwise train a cached synthetic demo model."""
import streamlit as st
from model_utils import load_model
from train_model import train_model


@st.cache_resource(show_spinner="Preparing the synthetic demo classifier…")
def synthetic_demo_model():
    # Shared read-only inference model; no signals or per-user cursor state are cached.
    # No filesystem writes: safe for fresh deployments and concurrent user sessions.
    return train_model(path=None)[0]


def load_dashboard_model():
    try:
        return load_model()
    except FileNotFoundError:
        return synthetic_demo_model()
