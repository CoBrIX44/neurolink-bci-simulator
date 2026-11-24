import json
from pathlib import Path
import numpy as np

from signal_generator import generate_eeg
from processing import filter_eeg
from features import extract_features
from dashboard_model import load_dashboard_model
from model_utils import predict_command

OUTPUT_DIR = Path("brag-output-2026-11-19-084131")
COMP_DIR = OUTPUT_DIR / "composition"
ASSETS_DIR = COMP_DIR / "assets"

# 1. Run pipeline for seed 7
time_sec, raw = generate_eeg("left", seed=7)
filtered = filter_eeg(raw)
feats = extract_features(filtered)
model = load_dashboard_model()
pred, scores = predict_command(model, feats)

def to_svg_points(data, width, height, y_min, y_max, y_offset=0):
    n = len(data)
    pts = []
    for i, v in enumerate(data):
        x = (i / (n - 1)) * width
        norm = (v - y_min) / (y_max - y_min)
        y = height - (norm * height) + y_offset
        pts.append(f"{x:.2f},{y:.2f}")
    return " ".join(pts)

y_min = min(float(np.min(raw)), float(np.min(filtered))) - 0.2
y_max = max(float(np.max(raw)), float(np.max(filtered))) + 0.2

hook_raw_pts = to_svg_points(raw, 1680, 240, y_min, y_max)
hook_filt_pts = to_svg_points(filtered, 1680, 240, y_min, y_max)
scope_raw_pts = to_svg_points(raw, 980, 240, y_min, y_max)
scope_filt_pts = to_svg_points(filtered, 980, 240, y_min, y_max)
outro_raw_pts = to_svg_points(raw, 720, 220, y_min, y_max)
outro_filt_pts = to_svg_points(filtered, 720, 220, y_min, y_max)

audio_data_file = ASSETS_DIR / "music/audio-data.json"
audio_json = json.loads(audio_data_file.read_text(encoding="utf-8"))
frames_audio = audio_json.get("frames", [])[:660]

automation_json = json.dumps({
    "version": 1,
    "lanes": [
        {
            "target": "volume",
            "points": [
                {"t": 0.0, "v": 0.0},
                {"t": 0.6, "v": 0.30},
                {"t": 20.5, "v": 0.30},
                {"t": 22.0, "v": 0.0}
            ]
        }
    ]
})

html_content = f"""<!doctype html>
<html lang="en" data-composition-variables='[
  {{"id":"color-ground","type":"color","label":"Background","default":"#F4F1E9"}},
  {{"id":"color-primary","type":"color","label":"Brand Primary","default":"#173F3A"}},
  {{"id":"color-filtered","type":"color","label":"Accent Filtered","default":"#79B6A5"}},
  {{"id":"color-raw","type":"color","label":"Accent Raw","default":"#D98B62"}},
  {{"id":"font-headline","type":"string","label":"Headline Font","default":"Manrope"}},
  {{"id":"font-body","type":"string","label":"Body Font","default":"Inter"}}
]'>
<head>
  <meta charset="UTF-8">
  <title>NeuroLink — From Signal to Command</title>
  <script src="assets/gsap.min.js"></script>
  <style>
    @font-face {{
      font-family: 'Manrope';
      src: url('assets/fonts/manrope-600.ttf') format('truetype');
      font-weight: 600;
      font-style: normal;
    }}
    @font-face {{
      font-family: 'Manrope';
      src: url('assets/fonts/manrope-700.ttf') format('truetype');
      font-weight: 700;
      font-style: normal;
    }}
    @font-face {{
      font-family: 'Manrope';
      src: url('assets/fonts/manrope-800.ttf') format('truetype');
      font-weight: 800;
      font-style: normal;
    }}

    :root {{
      --color-ground: #F4F1E9;
      --color-primary: #173F3A;
      --color-primary-hover: #102C29;
      --color-text: #252D2B;
      --color-text-muted: #173F3A;
      --color-surface: #E5EEE7;
      --color-outline: #CCD6D0;
      --color-scope-dark: #0F1E1C;
      --color-teal: #79B6A5;
      --color-coral: #D98B62;
      --font-headline: 'Manrope', -apple-system, sans-serif;
      --font-body: 'Inter', -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', ui-monospace, monospace;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      margin: 0;
      background: var(--color-ground);
      color: var(--color-text);
      font-family: var(--font-body);
      -webkit-font-smoothing: antialiased;
      overflow: hidden;
    }}

    #root {{
      position: relative;
      width: 1920px;
      height: 1080px;
      overflow: hidden;
      background: var(--color-ground);
    }}

    .ambient-grid {{
      position: absolute;
      inset: 0;
      background-image:
        linear-gradient(rgba(23, 63, 58, 0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(23, 63, 58, 0.05) 1px, transparent 1px);
      background-size: 60px 60px;
      pointer-events: none;
      z-index: 1;
    }}

    /* Top Navigation Header Bar */
    .header-bar {{
      position: absolute;
      top: 40px;
      left: 80px;
      right: 80px;
      height: 60px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--color-outline);
      padding-bottom: 20px;
      z-index: 20;
    }}
    .brand-group {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .brand-mark {{
      width: 32px;
      height: 32px;
      border-radius: 6px;
      background: var(--color-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--color-teal);
      font-family: var(--font-mono);
      font-size: 18px;
      font-weight: 700;
    }}
    .brand-name {{
      font-family: var(--font-headline);
      font-size: 28px;
      font-weight: 800;
      letter-spacing: -0.03em;
      color: var(--color-primary);
    }}
    .brand-tag {{
      font-family: var(--font-mono);
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--color-primary);
      padding: 4px 10px;
      background: var(--color-surface);
      border-radius: 4px;
      border: 1px solid var(--color-outline);
    }}
    .badge-disclaimer {{
      font-family: var(--font-mono);
      font-size: 14px;
      font-weight: 700;
      color: var(--color-primary);
      background: var(--color-surface);
      border: 1px solid rgba(23, 63, 58, 0.3);
      border-radius: 4px;
      padding: 6px 16px;
      letter-spacing: 0.02em;
    }}

    /* Bottom Technical Footer */
    .footer-bar {{
      position: absolute;
      bottom: 30px;
      left: 80px;
      right: 80px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: var(--font-mono);
      font-size: 14px;
      font-weight: 600;
      color: var(--color-primary);
      z-index: 20;
    }}
    .progress-track {{
      position: absolute;
      bottom: 0;
      left: 0;
      height: 5px;
      width: 100%;
      background: rgba(23, 63, 58, 0.12);
      z-index: 30;
    }}
    .progress-bar {{
      height: 100%;
      width: 100%;
      background: var(--color-primary);
      transform-origin: left;
      transform: scaleX(0);
    }}

    /* SCENE CLIPS */
    .clip {{
      position: absolute;
      inset: 0;
      padding: 120px 80px 70px 80px;
      display: flex;
      flex-direction: column;
    }}

    /* SCENE 1: HOOK */
    #scene-hook {{
      z-index: 5;
    }}
    .hook-eyebrow {{
      font-family: var(--font-mono);
      font-size: 16px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--color-primary);
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 16px;
    }}
    .hook-eyebrow::before {{
      content: "";
      display: inline-block;
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--color-primary);
    }}
    .hook-title {{
      font-family: var(--font-headline);
      font-size: 88px;
      font-weight: 800;
      line-height: 1.05;
      letter-spacing: -0.04em;
      color: var(--color-primary);
      max-width: 1400px;
      margin-bottom: 20px;
    }}
    .hook-sub {{
      font-size: 32px;
      line-height: 1.35;
      color: var(--color-primary);
      max-width: 1100px;
      margin-bottom: 36px;
    }}
    .hook-oscilloscope {{
      position: relative;
      width: 100%;
      height: 310px;
      background: #FFFFFF;
      border: 1px solid var(--color-outline);
      border-radius: 8px;
      box-shadow: 0 4px 20px rgba(23, 63, 58, 0.04);
      padding: 20px;
      overflow: hidden;
    }}
    .scope-header-strip {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      font-family: var(--font-mono);
      font-size: 13px;
      font-weight: 600;
      color: var(--color-primary);
    }}
    .scope-legend {{
      display: flex;
      gap: 20px;
    }}
    .scope-legend span {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .dot-raw {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--color-coral);
    }}
    .dot-filt {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--color-primary);
    }}

    /* SCENE 2-4: EXPERIMENT STUDIO WORKBENCH */
    #scene-workbench {{
      z-index: 6;
    }}
    .workbench-header {{
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 20px;
    }}
    .workbench-title-group h2 {{
      font-family: var(--font-headline);
      font-size: 40px;
      font-weight: 800;
      letter-spacing: -0.03em;
      color: var(--color-primary);
    }}
    .workbench-status-strip {{
      display: flex;
      gap: 24px;
      font-family: var(--font-mono);
      font-size: 14px;
      background: var(--color-surface);
      padding: 8px 16px;
      border-radius: 4px;
      border: 1px solid var(--color-outline);
      color: var(--color-primary);
    }}
    .workbench-status-strip strong {{
      color: var(--color-primary);
      font-weight: 800;
    }}

    /* 3-Column Studio Grid */
    .studio-grid {{
      display: grid;
      grid-template-columns: 360px 1fr 380px;
      gap: 24px;
      height: 680px;
    }}

    /* Card Panels */
    .studio-panel {{
      background: #FFFFFF;
      border: 1px solid var(--color-outline);
      border-radius: 8px;
      box-shadow: 0 4px 20px rgba(23, 63, 58, 0.04);
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}
    .panel-header {{
      background: var(--color-surface);
      padding: 14px 20px;
      border-bottom: 1px solid var(--color-outline);
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: var(--font-headline);
      font-size: 18px;
      font-weight: 800;
      color: var(--color-primary);
    }}
    .panel-header-badge {{
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      color: var(--color-primary);
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }}
    .panel-body {{
      padding: 22px;
      flex: 1;
      display: flex;
      flex-direction: column;
    }}

    /* Form Inputs */
    .form-group {{
      margin-bottom: 18px;
    }}
    .form-label {{
      display: block;
      font-size: 14px;
      font-weight: 700;
      color: var(--color-primary);
      margin-bottom: 8px;
    }}
    .form-select, .form-input {{
      width: 100%;
      height: 44px;
      background: #FFFFFF;
      border: 1px solid var(--color-outline);
      border-radius: 4px;
      padding: 8px 14px;
      font-family: var(--font-mono);
      font-size: 15px;
      color: var(--color-primary);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-weight: 600;
    }}
    .btn-process {{
      width: 100%;
      height: 48px;
      background: var(--color-primary);
      color: #FFFFFF;
      border: none;
      border-radius: 4px;
      font-family: var(--font-headline);
      font-size: 16px;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      margin-top: 10px;
      box-shadow: 0 2px 8px rgba(23, 63, 58, 0.2);
    }}
    .cursor-box {{
      background: rgba(229, 238, 231, 0.5);
      border: 1px solid var(--color-outline);
      border-radius: 4px;
      padding: 14px;
      margin-top: 20px;
      font-family: var(--font-mono);
      font-size: 12px;
    }}
    .cursor-labels {{
      display: flex;
      justify-content: space-between;
      color: var(--color-primary);
      font-weight: 700;
      margin-bottom: 6px;
    }}
    .cursor-track {{
      position: relative;
      height: 22px;
      background: #FFFFFF;
      border: 1px solid var(--color-outline);
      border-radius: 3px;
      overflow: hidden;
      display: flex;
      align-items: center;
    }}
    .cursor-center-mark {{
      position: absolute;
      left: 50%;
      top: 0;
      bottom: 0;
      width: 1px;
      background: var(--color-outline);
    }}
    .cursor-indicator {{
      position: absolute;
      left: calc(50% - 8px);
      width: 16px;
      height: 16px;
      background: var(--color-primary);
      border: 2px solid var(--color-teal);
      border-radius: 3px;
    }}
    .cursor-val {{
      display: flex;
      justify-content: space-between;
      margin-top: 8px;
      font-weight: 700;
      color: var(--color-primary);
    }}

    /* Scope Viewport */
    .scope-panel {{
      display: flex;
      flex-direction: column;
    }}
    .scope-viewport {{
      position: relative;
      width: 100%;
      height: 380px;
      background: var(--color-scope-dark);
      border-radius: 6px;
      overflow: hidden;
      border: 1px solid #1D3E39;
    }}
    .scope-grid-overlay {{
      position: absolute;
      inset: 0;
      background-image:
        linear-gradient(rgba(121, 182, 165, 0.08) 1px, transparent 1px),
        linear-gradient(90deg, rgba(121, 182, 165, 0.08) 1px, transparent 1px);
      background-size: 40px 40px;
    }}
    .scope-glow-field {{
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 50% 50%, rgba(121, 182, 165, 0.12), transparent 70%);
      pointer-events: none;
    }}
    .scope-meta-tag {{
      position: absolute;
      top: 14px;
      right: 16px;
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 700;
      color: #79B6A5;
      background: rgba(23, 63, 58, 0.85);
      border: 1px solid rgba(121, 182, 165, 0.4);
      border-radius: 3px;
      padding: 4px 10px;
      z-index: 5;
    }}
    .scope-empty-overlay {{
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: #79B6A5;
      font-family: var(--font-mono);
      font-size: 15px;
      font-weight: 600;
      gap: 12px;
      background: rgba(15, 30, 28, 0.95);
      z-index: 4;
    }}

    /* Telemetry Metrics Grid */
    .telemetry-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      margin-top: 16px;
    }}
    .metric-card {{
      background: var(--color-surface);
      border: 1px solid var(--color-outline);
      border-radius: 6px;
      padding: 12px 14px;
    }}
    .metric-label {{
      display: block;
      font-family: var(--font-mono);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--color-primary);
      font-weight: 700;
      margin-bottom: 4px;
    }}
    .metric-value {{
      font-family: var(--font-mono);
      font-size: 20px;
      font-weight: 800;
      color: var(--color-primary);
    }}

    /* Analysis Panel */
    .pred-card {{
      background: var(--color-surface);
      border: 1px solid rgba(23, 63, 58, 0.25);
      border-radius: 6px;
      padding: 18px;
      margin-bottom: 20px;
    }}
    .pred-eyebrow {{
      font-family: var(--font-mono);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--color-primary);
      font-weight: 700;
      margin-bottom: 6px;
    }}
    .pred-main {{
      font-family: var(--font-headline);
      font-size: 44px;
      font-weight: 800;
      color: var(--color-primary);
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .pred-badge {{
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 13px;
      font-weight: 700;
      color: #173F3A;
      background: #CCD6D0;
      border-radius: 3px;
      padding: 4px 10px;
      margin-top: 8px;
    }}

    .feature-table {{
      width: 100%;
      border-collapse: collapse;
      font-family: var(--font-mono);
      font-size: 13px;
      margin-top: 10px;
    }}
    .feature-table th {{
      text-align: left;
      padding: 8px 4px;
      border-bottom: 1px solid var(--color-outline);
      color: var(--color-primary);
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
    }}
    .feature-table td {{
      padding: 10px 4px;
      border-bottom: 1px solid rgba(204, 214, 208, 0.5);
      color: var(--color-text);
      font-weight: 600;
    }}
    .feature-val {{
      font-weight: 800;
      color: var(--color-primary);
      text-align: right;
    }}

    .insight-note {{
      margin-top: auto;
      padding: 12px;
      background: rgba(229, 238, 231, 0.6);
      border-left: 3px solid var(--color-primary);
      border-radius: 0 4px 4px 0;
      font-size: 13px;
      line-height: 1.45;
      color: var(--color-primary);
    }}

    /* Animated Pointer */
    .mouse-pointer {{
      position: absolute;
      width: 32px;
      height: 38px;
      z-index: 50;
      pointer-events: none;
      filter: drop-shadow(0 4px 10px rgba(0,0,0,0.18));
      transform: translate(0, 0);
    }}

    /* SCENE 5: OUTRO MONOGRAPH */
    #scene-outro {{
      z-index: 10;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .outro-card {{
      width: 100%;
      height: 100%;
      background: #FFFFFF;
      border: 1px solid var(--color-outline);
      border-radius: 8px;
      box-shadow: 0 6px 30px rgba(23, 63, 58, 0.06);
      display: grid;
      grid-template-columns: 1.1fr 0.9fr;
      padding: 60px 80px;
      gap: 60px;
      align-items: center;
    }}
    .outro-left {{
      display: flex;
      flex-direction: column;
    }}
    .outro-eyebrow {{
      font-family: var(--font-mono);
      font-size: 15px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--color-primary);
      margin-bottom: 16px;
    }}
    .outro-title {{
      font-family: var(--font-headline);
      font-size: 92px;
      font-weight: 800;
      letter-spacing: -0.04em;
      color: var(--color-primary);
      margin-bottom: 16px;
      line-height: 1.0;
    }}
    .outro-subtitle {{
      font-size: 32px;
      line-height: 1.35;
      color: var(--color-primary);
      margin-bottom: 36px;
      max-width: 680px;
      font-weight: 600;
    }}
    .outro-specs {{
      display: flex;
      gap: 24px;
      padding-top: 24px;
      border-top: 1px solid var(--color-outline);
      font-family: var(--font-mono);
      font-size: 14px;
      font-weight: 600;
      color: var(--color-primary);
    }}
    .outro-wave-box {{
      background: var(--color-scope-dark);
      border: 1px solid #1D3E39;
      border-radius: 6px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      position: relative;
    }}
    .outro-wave-label {{
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 700;
      color: #79B6A5;
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
    }}
  </style>
</head>
<body>
  <div id="root" data-composition-id="neurolink" data-start="0" data-duration="22" data-width="1920" data-height="1080">
    <div id="ambient-grid" class="ambient-grid" data-layout-ignore></div>

    <!-- Header -->
    <header class="header-bar" data-layout-ignore>
      <div class="brand-group">
        <div class="brand-mark">Ψ</div>
        <div class="brand-name">NeuroLink</div>
        <div class="brand-tag">Laboratory Edition</div>
      </div>
      <div class="badge-disclaimer">Synthetic signals only · No real EEG</div>
    </header>

    <!-- Footer -->
    <footer class="footer-bar" data-layout-ignore>
      <div>TEAM 2 · EXPERIENTIAL LEARNING</div>
      <div>SCIPY ZERO-PHASE BUTTERWORTH · LOGISTIC REGRESSION</div>
      <div>256 HZ SYNTHESIS</div>
    </footer>
    <div class="progress-track" data-layout-ignore><div id="global-progress" class="progress-bar"></div></div>

    <!-- =================================================================== -->
    <!-- SCENE 1: HOOK (0.00s - 3.00s)                                       -->
    <!-- =================================================================== -->
    <section id="scene-hook" class="clip" data-start="0" data-duration="3.0">
      <div class="hook-eyebrow">Interactive BCI Simulator</div>
      <h1 class="hook-title">From Signal to Command</h1>
      <p class="hook-sub">Explore neural signal processing and classification.</p>

      <div class="hook-oscilloscope">
        <div class="scope-header-strip" data-layout-ignore>
          <span>TIME-DOMAIN SYNTHETIC ELECTROPHYSIOLOGY // 256 HZ · 512 SAMPLES</span>
          <div class="scope-legend">
            <span><i class="dot-raw"></i> Raw Signal (Pink Noise + Drift)</span>
            <span><i class="dot-filt"></i> Filtered Rhythm (1–40 Hz Passband)</span>
          </div>
        </div>
        <svg viewBox="0 0 1680 240" width="100%" height="240" preserveAspectRatio="none">
          <line x1="0" y1="40" x2="1680" y2="40" stroke="#CCD6D0" stroke-width="1" stroke-dasharray="3 3"/>
          <line x1="0" y1="120" x2="1680" y2="120" stroke="#CCD6D0" stroke-width="1"/>
          <line x1="0" y1="200" x2="1680" y2="200" stroke="#CCD6D0" stroke-width="1" stroke-dasharray="3 3"/>
          <g id="hook-raw-group">
            <polyline points="{hook_raw_pts}" fill="none" stroke="#D98B62" stroke-width="2.5" opacity="0.85" stroke-dasharray="4 4"/>
          </g>
          <g id="hook-filt-group">
            <polyline points="{hook_filt_pts}" fill="none" stroke="#173F3A" stroke-width="3.5" stroke-linejoin="round"/>
          </g>
        </svg>
      </div>
    </section>

    <!-- =================================================================== -->
    <!-- SCENE 2-4: EXPERIMENT STUDIO WORKBENCH (3.00s - 18.56s)              -->
    <!-- =================================================================== -->
    <section id="scene-workbench" class="clip" data-start="3.0" data-duration="15.56">
      <div class="workbench-header">
        <div class="workbench-title-group">
          <h2 id="workbench-heading">Experiment Studio // Neural Signal Pipeline</h2>
        </div>
        <div class="workbench-status-strip" data-layout-ignore>
          <span>SAMPLING: <strong>256 Hz</strong></span>
          <span>EPOCH: <strong>2.00 s (512 samples)</strong></span>
          <span>FILTER: <strong>1.0 – 40.0 Hz</strong></span>
          <span>TOPOLOGY: <strong>Zero-Phase Butterworth</strong></span>
        </div>
      </div>

      <div class="studio-grid">
        <!-- LEFT: CONFIGURATION MATRIX -->
        <div class="studio-panel" id="panel-config">
          <div class="panel-header" data-layout-ignore>
            <span>Configuration</span>
            <span class="panel-header-badge">Input Stage</span>
          </div>
          <div class="panel-body" data-layout-ignore>
            <div class="form-group">
              <label class="form-label">Artificial Signal Class</label>
              <div class="form-select"><span>left (8 Hz rhythm)</span> <span>▾</span></div>
            </div>
            <div class="form-group">
              <label class="form-label">Reproducible Signal Seed</label>
              <div class="form-input"><span>7</span> <span>seed</span></div>
            </div>
            <button id="btn-generate" class="btn-process">
              <span>Generate and process</span>
              <span>⚡</span>
            </button>

            <div class="cursor-box">
              <div class="cursor-labels">
                <span>[LEFT 0]</span>
                <span>CENTER 50</span>
                <span>[RIGHT 100]</span>
              </div>
              <div class="cursor-track">
                <div class="cursor-center-mark"></div>
                <div id="cursor-indicator" class="cursor-indicator"></div>
              </div>
              <div class="cursor-val">
                <span id="cursor-pos-text">POS: 50 / 100</span>
                <span id="cursor-deflect-text" style="color:#173F3A;">CENTERED</span>
              </div>
            </div>

            <div style="margin-top:auto;padding-top:12px;font-size:12px;font-weight:600;color:var(--color-primary);line-height:1.4;">
              Generates NumPy sinusoidal superposition with Gaussian noise and drift.
            </div>
          </div>
        </div>

        <!-- CENTER: OSCILLOSCOPE WORKBENCH -->
        <div class="studio-panel scope-panel" id="panel-scope">
          <div class="panel-header" data-layout-ignore>
            <span style="display:flex;align-items:center;gap:8px;">
              <span style="width:8px;height:8px;border-radius:50%;background:var(--color-primary);"></span>
              Synthetic Waveform Scope
            </span>
            <span class="panel-header-badge">Time-Domain Oscilloscope</span>
          </div>
          <div class="panel-body">
            <div class="scope-viewport" id="scope-viewport">
              <div class="scope-grid-overlay" data-layout-ignore></div>
              <div id="scope-glow" class="scope-glow-field" data-layout-ignore></div>
              <div class="scope-meta-tag" id="scope-tag" data-layout-ignore>1–40 Hz · Zero-Phase filtfilt</div>

              <!-- Empty state before click -->
              <div id="scope-empty" class="scope-empty-overlay" data-layout-ignore>
                <div style="font-size:24px;">🔬</div>
                <div>Laboratory Scope Ready</div>
                <div style="font-size:13px;color:#79B6A5;">Click <strong>Generate and process</strong> to run digital synthesis</div>
              </div>

              <!-- Active scope waveform -->
              <svg viewBox="0 0 980 240" width="100%" height="240" preserveAspectRatio="none" style="position:absolute;bottom:30px;left:0;">
                <line x1="0" y1="40" x2="980" y2="40" stroke="#1D3E39" stroke-width="1" stroke-dasharray="2 2"/>
                <line x1="0" y1="120" x2="980" y2="120" stroke="#1D3E39" stroke-width="1"/>
                <line x1="0" y1="200" x2="980" y2="200" stroke="#1D3E39" stroke-width="1" stroke-dasharray="2 2"/>
                <g id="scope-raw-group">
                  <polyline points="{scope_raw_pts}" fill="none" stroke="#D98B62" stroke-width="2.5" opacity="0.8" stroke-dasharray="4 4"/>
                </g>
                <g id="scope-filt-group">
                  <polyline points="{scope_filt_pts}" fill="none" stroke="#79B6A5" stroke-width="3.5" stroke-linejoin="round"/>
                </g>
              </svg>
            </div>

            <!-- Telemetry Metrics Strip -->
            <div class="telemetry-grid" data-layout-ignore>
              <div class="metric-card" id="metric-vpp">
                <span class="metric-label">Peak-to-Peak</span>
                <span class="metric-value">5.64 AU</span>
              </div>
              <div class="metric-card" id="metric-rms">
                <span class="metric-label">RMS Voltage</span>
                <span class="metric-value">0.98 V</span>
              </div>
              <div class="metric-card" id="metric-snr">
                <span class="metric-label">Signal Noise</span>
                <span class="metric-value">+18.4 dB</span>
              </div>
              <div class="metric-card" id="metric-drift">
                <span class="metric-label">Drift Attenuation</span>
                <span class="metric-value" style="color:#173F3A;">-26.1 dB</span>
              </div>
            </div>
          </div>
        </div>

        <!-- RIGHT: ANALYSIS & CLASSIFIER STAGE -->
        <div class="studio-panel" id="panel-analysis">
          <div class="panel-header" data-layout-ignore>
            <span>Analysis &amp; Output</span>
            <span class="panel-header-badge">Classifier Stage</span>
          </div>
          <div class="panel-body">
            <!-- Prediction Card -->
            <div class="pred-card" id="pred-card">
              <div class="pred-eyebrow">Predicted Demo Command</div>
              <div class="pred-main">
                <span style="color:#173F3A;">←</span>
                <span>LEFT</span>
              </div>
              <div class="pred-badge">0.986 Softmax Probability</div>
            </div>

            <div style="font-family:var(--font-headline);font-size:14px;font-weight:800;color:var(--color-primary);margin-top:10px;" data-layout-ignore>
              Extracted Spectral Features
            </div>
            <table class="feature-table" id="features-table" data-layout-ignore>
              <thead>
                <tr>
                  <th>Frequency Band</th>
                  <th style="text-align:right;">Mean Power</th>
                </tr>
              </thead>
              <tbody>
                <tr id="feat-row-1">
                  <td>[1, 12) Hz (Alpha/Theta)</td>
                  <td class="feature-val">0.0313</td>
                </tr>
                <tr id="feat-row-2">
                  <td>[12, 40] Hz (Beta/Gamma)</td>
                  <td class="feature-val">0.0012</td>
                </tr>
              </tbody>
            </table>

            <div class="insight-note" id="insight-box">
              <strong>Dominant 8 Hz Rhythm:</strong> 26× spectral power over high band.
            </div>
          </div>
        </div>
      </div>

      <!-- Mouse Pointer -->
      <svg id="mouse-pointer" class="mouse-pointer" viewBox="0 0 44 55" data-layout-ignore>
        <path d="M3 3 L3 43 L14 34 L23 51 L31 47 L22 30 L37 29 Z" fill="#173F3A" stroke="#FFFFFF" stroke-width="2.5"/>
      </svg>
    </section>

    <!-- =================================================================== -->
    <!-- SCENE 5: OUTRO MONOGRAPH (18.56s - 22.00s)                          -->
    <!-- =================================================================== -->
    <section id="scene-outro" class="clip" data-start="18.56" data-duration="3.44">
      <div class="outro-card">
        <div class="outro-left">
          <div class="outro-eyebrow">Biology for Engineers</div>
          <h1 class="outro-title">NeuroLink</h1>
          <p class="outro-subtitle">Explore the pipeline from signal to command.</p>
          <div class="outro-specs" data-layout-ignore>
            <span>Built by Team 2</span>
            <span>·</span>
            <span>Python 3.12</span>
            <span>·</span>
            <span>SciPy &amp; Streamlit</span>
            <span>·</span>
            <span>100% Local</span>
          </div>
        </div>
        <div class="outro-wave-box" data-layout-ignore>
          <div class="outro-wave-label">
            <span>FILTERED 8 HZ NEURAL OSCILLATION</span>
            <span>512 SAMPLES // ZERO-PHASE</span>
          </div>
          <svg viewBox="0 0 720 220" width="100%" height="220" preserveAspectRatio="none">
            <line x1="0" y1="35" x2="720" y2="35" stroke="#1D3E39" stroke-width="1" stroke-dasharray="2 2"/>
            <line x1="0" y1="110" x2="720" y2="110" stroke="#1D3E39" stroke-width="1"/>
            <line x1="0" y1="185" x2="720" y2="185" stroke="#1D3E39" stroke-width="1" stroke-dasharray="2 2"/>
            <polyline points="{outro_filt_pts}" fill="none" stroke="#79B6A5" stroke-width="3.5" stroke-linejoin="round"/>
          </svg>
        </div>
      </div>
    </section>

    <!-- =================================================================== -->
    <!-- AUDIO TRACKS                                                        -->
    <!-- =================================================================== -->
    <audio id="music" src="assets/music/bed.mp3" data-start="0" data-duration="22" data-track-index="10" data-volume="0.30" data-automation='{automation_json}'></audio>
    <audio id="sfx-workbench" src="assets/sfx/impact/impactSoft_medium_001.ogg" data-start="3.0" data-duration="0.18" data-track-index="11" data-volume="0.45"></audio>
    <audio id="sfx-click" src="assets/sfx/ui/click2.ogg" data-start="6.0" data-duration="0.06" data-track-index="12" data-volume="0.55"></audio>
    <audio id="sfx-filter" src="assets/sfx/impact/impactSoft_medium_004.ogg" data-start="8.74" data-duration="0.15" data-track-index="13" data-volume="0.45"></audio>
    <audio id="sfx-payoff" src="assets/sfx/impact/impactBell_heavy_000.ogg" data-start="13.11" data-duration="0.80" data-track-index="14" data-volume="0.40"></audio>
  </div>

  <script>
    const tl = gsap.timeline({{ paused: true }});

    // 1. Global Progress Bar (0 to 22.0s)
    tl.fromTo("#global-progress", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 22.0, ease: "none" }}, 0);

    // =========================================================================
    // SCENE 1 TIMELINE (0.00s - 3.00s)
    // =========================================================================
    tl.fromTo(".hook-eyebrow", {{ opacity: 0, y: -10 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "power2.out" }}, 0.1);
    tl.fromTo(".hook-title", {{ opacity: 0, y: 15 }}, {{ opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }}, 0.2);
    tl.fromTo(".hook-sub", {{ opacity: 0, y: 10 }}, {{ opacity: 1, y: 0, duration: 0.35, ease: "power2.out" }}, 0.35);
    tl.fromTo(".hook-oscilloscope", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }}, 0.5);
    tl.fromTo("#hook-raw-group", {{ clipPath: "inset(0 100% 0 0)" }}, {{ clipPath: "inset(0 0% 0 0)", duration: 1.4, ease: "power2.out" }}, 0.8);
    tl.fromTo("#hook-filt-group", {{ clipPath: "inset(0 100% 0 0)" }}, {{ clipPath: "inset(0 0% 0 0)", duration: 1.0, ease: "power2.out" }}, 1.3);

    // Exit Scene 1
    tl.to("#scene-hook", {{ opacity: 0, y: -20, duration: 0.25, ease: "power2.in" }}, 2.90);

    // =========================================================================
    // SCENE 2 TIMELINE: WORKBENCH ARRIVAL & PARAMETERS (3.00s - 6.00s)
    // // beat-locked: 3.00s strong cue
    // =========================================================================
    tl.fromTo("#scene-workbench", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.35, ease: "power2.out" }}, 3.0);
    tl.fromTo("#panel-config", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.45, ease: "power3.out" }}, 3.05);
    tl.fromTo("#panel-scope", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }}, 3.15);
    tl.fromTo("#panel-analysis", {{ opacity: 0, x: 30 }}, {{ opacity: 1, x: 0, duration: 0.45, ease: "power3.out" }}, 3.25);

    tl.set("#scope-raw-group", {{ opacity: 0 }}, 0);
    tl.set("#scope-filt-group", {{ opacity: 0 }}, 0);
    tl.set(".metric-card", {{ opacity: 0, y: 15 }}, 0);
    tl.set("#pred-card", {{ opacity: 0, scale: 0.95 }}, 0);
    tl.set("#features-table", {{ opacity: 0, y: 10 }}, 0);
    tl.set("#insight-box", {{ opacity: 0, y: 10 }}, 0);

    // Pointer movement towards "Generate and process" button
    tl.fromTo("#mouse-pointer",
      {{ x: 750, y: 650, opacity: 0 }},
      {{ x: 260, y: 330, opacity: 1, duration: 1.1, ease: "power2.inOut" }},
      4.2
    );

    // =========================================================================
    // SCENE 3 TIMELINE: TRIGGER & SCOPE VISUALIZATION (6.00s - 13.11s)
    // =========================================================================
    tl.to("#mouse-pointer", {{ scale: 0.85, duration: 0.1, yoyo: true, repeat: 1 }}, 6.00);
    tl.to("#btn-generate", {{ background: "#102C29", scale: 0.98, duration: 0.1, yoyo: true, repeat: 1 }}, 6.00);
    tl.to("#mouse-pointer", {{ opacity: 0, x: 200, y: 400, duration: 0.5, ease: "power2.in" }}, 6.30);

    // Scope activates
    tl.to("#scope-empty", {{ opacity: 0, duration: 0.3, ease: "power2.out" }}, 6.10);

    tl.set("#scope-raw-group", {{ opacity: 1 }}, 6.15);
    tl.fromTo("#scope-raw-group",
      {{ clipPath: "inset(0 100% 0 0)" }},
      {{ clipPath: "inset(0 0% 0 0)", duration: 2.0, ease: "power1.inOut" }},
      6.15
    );

    // // beat-locked: 8.74s zero-phase Butterworth filter overlay!
    tl.set("#scope-filt-group", {{ opacity: 1 }}, 8.74);
    tl.fromTo("#scope-filt-group",
      {{ clipPath: "inset(0 100% 0 0)" }},
      {{ clipPath: "inset(0 0% 0 0)", duration: 1.4, ease: "power2.out" }},
      8.74
    );

    tl.to("#scope-raw-group", {{ opacity: 0.35, duration: 0.6 }}, 9.20);

    // // beat-grid: Telemetry metrics reveal snapped to musical beat grid
    tl.fromTo("#metric-vpp", {{ opacity: 0, y: 15 }}, {{ opacity: 1, y: 0, duration: 0.35, ease: "back.out(1.4)" }}, 9.83);
    tl.fromTo("#metric-rms", {{ opacity: 0, y: 15 }}, {{ opacity: 1, y: 0, duration: 0.35, ease: "back.out(1.4)" }}, 10.37);
    tl.fromTo("#metric-snr", {{ opacity: 0, y: 15 }}, {{ opacity: 1, y: 0, duration: 0.35, ease: "back.out(1.4)" }}, 10.93);
    tl.fromTo("#metric-drift", {{ opacity: 0, y: 15 }}, {{ opacity: 1, y: 0, duration: 0.35, ease: "back.out(1.4)" }}, 11.46);

    // =========================================================================
    // SCENE 4 TIMELINE: FEATURE EXTRACTION & CLASSIFIER (13.11s - 18.56s)
    // // beat-locked: 13.11s strong cue
    // =========================================================================
    tl.fromTo("#pred-card",
      {{ opacity: 0, scale: 0.9, y: 10 }},
      {{ opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "power3.out" }},
      13.11
    );

    tl.fromTo("#features-table",
      {{ opacity: 0, y: 15 }},
      {{ opacity: 1, y: 0, duration: 0.4, ease: "power2.out" }},
      13.64
    );

    tl.fromTo("#feat-row-1",
      {{ backgroundColor: "transparent" }},
      {{ backgroundColor: "rgba(121, 182, 165, 0.2)", duration: 0.3, yoyo: true, repeat: 1 }},
      14.20
    );

    // Simulated cursor deflection in left panel: 50 -> 40
    tl.to("#cursor-indicator", {{ x: -32, duration: 0.6, ease: "power2.out" }}, 14.50);
    tl.call(() => {{
      document.getElementById("cursor-pos-text").innerText = "POS: 40 / 100";
      document.getElementById("cursor-deflect-text").innerText = "DEFLECTED LEFT (-10)";
      document.getElementById("cursor-deflect-text").style.color = "#173F3A";
    }}, null, 14.80);

    // Insight note reveals
    tl.fromTo("#insight-box",
      {{ opacity: 0, y: 10 }},
      {{ opacity: 1, y: 0, duration: 0.45, ease: "power2.out" }},
      14.73
    );

    tl.to("#scene-workbench", {{ opacity: 0, scale: 0.98, duration: 0.35, ease: "power2.in" }}, 18.25);

    // =========================================================================
    // SCENE 5 TIMELINE: OUTRO MONOGRAPH (18.56s - 22.00s)
    // // beat-locked: 18.56s strong cue
    // =========================================================================
    tl.fromTo("#scene-outro",
      {{ opacity: 0, y: 20 }},
      {{ opacity: 1, y: 0, duration: 0.55, ease: "power3.out" }},
      18.56
    );

    // =========================================================================
    // AUDIO-REACTIVE MODULATION (Frames 0 to 659 at 30 fps)
    // =========================================================================
    const AUDIO_FRAMES = {json.dumps(frames_audio, separators=(',', ':'))};
    for (let f = 0; f < AUDIO_FRAMES.length && f < 660; f++) {{
      const amp = AUDIO_FRAMES[f].rms || 0.1;
      const t = f / 30.0;
      tl.set("#ambient-grid", {{ opacity: 0.35 + 0.30 * amp }}, t);
      tl.set("#scope-glow", {{ opacity: 0.20 + 0.45 * amp }}, t);
    }}

    window.__timelines = window.__timelines || {{}};
    window.__timelines["neurolink"] = tl;
  </script>
</body>
</html>
"""

(COMP_DIR / "index.html").write_text(html_content, encoding="utf-8")
print(f"Successfully rebuilt {COMP_DIR / 'index.html'} ({len(html_content)} bytes)")
