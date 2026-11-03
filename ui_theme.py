"""Presentation helpers, design system tokens, and Plotly styling for NeuroLink."""
import html
import plotly.graph_objects as go

# Design System Color Tokens
COLOR_CANVAS_BG = "#F8F9FA"
COLOR_SURFACE = "#FFFFFF"
COLOR_CANVAS_DARK = "#0A0F1D"
COLOR_TEXT_PRIMARY = "#0F172A"
COLOR_TEXT_SECONDARY = "#475569"
COLOR_TEXT_LIGHT = "#E2E8F0"
COLOR_BORDER = "#E2E8F0"
COLOR_BORDER_FOCUS = "#0284C7"
COLOR_PRIMARY = "#087E8B"
COLOR_PRIMARY_HOVER = "#06636E"
COLOR_TRACE_RAW = "#94A3B8"
COLOR_TRACE_FILTERED = "#00E5FF"
COLOR_DIFF_BG = "#FFFBEB"
COLOR_DIFF_TEXT = "#B45309"
COLOR_DIFF_BORDER = "#FDE68A"

CUSTOM_CSS = f"""
<style>
/* Base typography & shell styling */
:root {{
    --font-sans: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    --font-mono: ui-monospace, "SF Mono", "Cascadia Code", "Roboto Mono", Consolas, monospace;
}}

html, body, [class*="css"] {{
    font-family: var(--font-sans);
    color: {COLOR_TEXT_PRIMARY};
}}

/* Tabular numerals for all measurements */
.tabular-nums, table, [data-testid="stMetricValue"], [data-testid="stTable"] {{
    font-variant-numeric: tabular-nums;
}}

/* Main block padding & layout */
.block-container {{
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
    max-width: 1200px !important;
}}

/* Compact modern header */
.neurolink-header {{
    margin-bottom: 0.75rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid {COLOR_BORDER};
}}

.neurolink-header h1 {{
    font-size: 1.75rem !important;
    font-weight: 700 !important;
    color: {COLOR_TEXT_PRIMARY} !important;
    margin: 0 0 0.25rem 0 !important;
    letter-spacing: -0.02em;
}}

.neurolink-header-subtitle {{
    font-size: 0.875rem;
    color: {COLOR_TEXT_SECONDARY};
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.5rem;
}}

.neurolink-badge {{
    display: inline-flex;
    align-items: center;
    background: #E0F2FE;
    color: #0369A1;
    font-size: 0.75rem;
    font-weight: 600;
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
    letter-spacing: 0.03em;
    text-transform: uppercase;
}}

/* Setup Card styling */
.neurolink-setup-card {{
    background: {COLOR_SURFACE};
    border: 1px solid {COLOR_BORDER};
    border-radius: 8px;
    padding: 1rem 1.25rem;
    margin-bottom: 1.25rem;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}}

.neurolink-section-title {{
    font-size: 0.875rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: {COLOR_TEXT_SECONDARY};
    margin-bottom: 0.75rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}}

/* Settings changed diff alert */
.neurolink-diff-notice {{
    background: {COLOR_DIFF_BG};
    border: 1px solid {COLOR_DIFF_BORDER};
    color: {COLOR_DIFF_TEXT};
    padding: 0.5rem 0.75rem;
    border-radius: 6px;
    font-size: 0.8125rem;
    font-weight: 500;
    margin-top: 0.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}}

/* Signal Analysis Container */
.neurolink-canvas-frame {{
    background: {COLOR_CANVAS_DARK};
    border-radius: 8px;
    padding: 0.75rem;
    margin-bottom: 1.25rem;
    border: 1px solid #1E293B;
}}

.neurolink-canvas-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.25rem 0.75rem 0.5rem 0.75rem;
    border-bottom: 1px solid #1E293B;
    margin-bottom: 0.5rem;
}}

.neurolink-canvas-title {{
    font-size: 0.8125rem;
    font-weight: 600;
    color: {COLOR_TEXT_LIGHT};
    letter-spacing: 0.02em;
    text-transform: uppercase;
}}

.neurolink-canvas-tag {{
    font-family: var(--font-mono);
    font-size: 0.75rem;
    background: #1E293B;
    color: #38BDF8;
    padding: 0.2rem 0.6rem;
    border-radius: 4px;
}}

/* Empty state styling */
.neurolink-empty-state {{
    background: {COLOR_SURFACE};
    border: 2px dashed {COLOR_BORDER};
    border-radius: 8px;
    padding: 2.5rem 1.5rem;
    text-align: center;
    margin: 1rem 0;
}}

.neurolink-empty-title {{
    font-size: 1.125rem;
    font-weight: 600;
    color: {COLOR_TEXT_PRIMARY};
    margin-bottom: 0.5rem;
}}

.neurolink-empty-desc {{
    font-size: 0.875rem;
    color: {COLOR_TEXT_SECONDARY};
    max-width: 540px;
    margin: 0 auto;
    line-height: 1.5;
}}

/* Interpretation Card styling */
.neurolink-card {{
    background: {COLOR_SURFACE};
    border: 1px solid {COLOR_BORDER};
    border-radius: 8px;
    padding: 1.25rem;
    margin-bottom: 1rem;
    height: 100%;
}}

.neurolink-comparison-box {{
    background: #F1F5F9;
    border-left: 3px solid {COLOR_PRIMARY};
    border-radius: 0 6px 6px 0;
    padding: 0.625rem 0.875rem;
    font-size: 0.8125rem;
    color: {COLOR_TEXT_PRIMARY};
    line-height: 1.45;
    margin-top: 0.75rem;
}}

/* Table adjustments for clean wrapped display */
[data-testid="stTable"] {{
    width: 100% !important;
    overflow-x: auto !important;
}}

[data-testid="stTable"] table {{
    width: 100% !important;
    font-size: 0.875rem !important;
}}

/* Primary button minimum touch target */
button[kind="primary"] {{
    min-height: 44px !important;
    font-weight: 600 !important;
    border-radius: 6px !important;
}}

/* Accessibility focus indicator */
button:focus-visible, input:focus-visible, select:focus-visible {{
    outline: 2px solid {COLOR_BORDER_FOCUS} !important;
    outline-offset: 2px !important;
}}

/* Mobile responsive adjustments */
@media (max-width: 640px) {{
    .block-container {{
        padding-left: 0.75rem !important;
        padding-right: 0.75rem !important;
    }}
    .neurolink-header h1 {{
        font-size: 1.35rem !important;
    }}
}}
</style>
"""


def create_waveform_figure(time_sec, raw_signal, filtered_signal) -> go.Figure:
    """Create a high-contrast dark waveform canvas Plotly figure with responsive legend."""
    fig = go.Figure()

    # Raw signal: subtle slate gray, dotted line
    fig.add_trace(go.Scatter(
        x=time_sec,
        y=raw_signal,
        name="Raw synthetic signal",
        line=dict(color=COLOR_TRACE_RAW, width=1.2, dash="dot"),
        mode="lines"
    ))

    # Filtered signal: vibrant cyan, solid prominent stroke
    fig.add_trace(go.Scatter(
        x=time_sec,
        y=filtered_signal,
        name="Filtered synthetic signal",
        line=dict(color=COLOR_TRACE_FILTERED, width=2.4),
        mode="lines"
    ))

    fig.update_layout(
        title=dict(
            text="Raw and filtered synthetic waveforms",
            font=dict(color=COLOR_TEXT_LIGHT, size=14, family="sans-serif")
        ),
        xaxis=dict(
            title=dict(text="Time (seconds)", font=dict(color=COLOR_TEXT_LIGHT, size=12)),
            tickfont=dict(color="#94A3B8", size=11),
            gridcolor="#1E293B",
            zerolinecolor="#334155",
            showline=True,
            linecolor="#334155"
        ),
        yaxis=dict(
            title=dict(text="Amplitude (arbitrary units)", font=dict(color=COLOR_TEXT_LIGHT, size=12)),
            tickfont=dict(color="#94A3B8", size=11),
            gridcolor="#1E293B",
            zerolinecolor="#334155",
            showline=True,
            linecolor="#334155"
        ),
        plot_bgcolor=COLOR_CANVAS_DARK,
        paper_bgcolor=COLOR_CANVAS_DARK,
        hovermode="x unified",
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.22,
            xanchor="center",
            x=0.5,
            font=dict(color=COLOR_TEXT_LIGHT, size=11),
            bgcolor="rgba(10, 15, 29, 0.7)"
        ),
        margin=dict(l=40, r=20, t=45, b=65),
        height=360
    )
    return fig


def get_feature_comparison_text(features: dict[str, float], generator_label: str) -> str:
    """Generate dynamic explanatory comparison between the two spectral features."""
    p1 = features.get("mean_power_1_12_hz", 0.0)
    p2 = features.get("mean_power_12_40_hz", 0.0)
    
    if p1 > p2:
        ratio = p1 / p2 if p2 > 0 else float("inf")
        ratio_str = f"{ratio:.1f}×" if ratio < 100 else ">100×"
        return (
            f"Low-frequency band [1, 12) Hz is {ratio_str} stronger than high-frequency [12, 40] Hz. "
            f"This matches the synthetic '{html.escape(generator_label)}' pattern (8 Hz target emphasis)."
        )
    else:
        ratio = p2 / p1 if p1 > 0 else float("inf")
        ratio_str = f"{ratio:.1f}×" if ratio < 100 else ">100×"
        return (
            f"High-frequency band [12, 40] Hz is {ratio_str} stronger than low-frequency [1, 12) Hz. "
            f"This matches the synthetic '{html.escape(generator_label)}' pattern (22 Hz target emphasis)."
        )
