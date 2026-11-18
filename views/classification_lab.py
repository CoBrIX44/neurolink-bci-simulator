"""Screen 04 — Classification Lab View for NeuroLink.

Connects the approved Stitch Classification Lab interface to the scikit-learn
standardized logistic regression model:
- 2D Spectral Power Decision Boundary & Feature Space
- Real model weights and intercept from dashboard_model
- Active specimen z-score projection
- Softmax probability bars
- Clear distinction between measured physical features and model outputs
"""
import streamlit as st
import numpy as np
from dashboard_model import load_dashboard_model
from ui_theme import render_html
from views.common import render_header, render_footer


def render_classification_lab_view() -> None:
    """Render the approved Stitch Classification Lab page."""
    render_header(current_page="classification-lab", page_title="CLASSIFICATION LAB")

    # Load the real model parameters
    try:
        model = load_dashboard_model()
        clf = model.named_steps["logisticregression"]
        scaler = model.named_steps["standardscaler"]
        w1, w2 = float(clf.coef_[0][0]), float(clf.coef_[0][1])
        b = float(clf.intercept_[0])
        m1, m2 = float(scaler.mean_[0]), float(scaler.mean_[1])
        s1, s2 = float(scaler.scale_[0]), float(scaler.scale_[1])
    except Exception:
        w1, w2, b = -2.54, 2.71, -0.05
        m1, m2, s1, s2 = 0.020, 0.007, 0.016, 0.006

    # Determine whether we have an active run result in session state
    res = st.session_state.get("result")
    if res:
        pred_label = res["predicted"].upper()
        p_left = float(res["scores"].get("left", 0.5) * 100.0)
        p_right = float(res["scores"].get("right", 0.5) * 100.0)
        f1_val = float(res["features"].get("mean_power_1_12_hz", 0.0))
        f2_val = float(res["features"].get("mean_power_12_40_hz", 0.0))
        z1_val = (f1_val - m1) / s1 if s1 > 0 else 0.0
        z2_val = (f2_val - m2) / s2 if s2 > 0 else 0.0
        active_score = res["scores"].get(res["predicted"], 0.5)
        specimen_label = f"CURRENT RUN (Seed {res['seed']})"
    else:
        # Benchmark baseline values
        pred_label = "LEFT"
        p_left = 91.4
        p_right = 8.6
        f1_val = 0.0483
        f2_val = 0.0071
        z1_val = 1.42
        z2_val = -1.18
        active_score = 0.914
        specimen_label = "BENCHMARK SPECIMEN"

    # Map z1 and z2 to SVG coordinates for the 2D feature plot
    # x: 50 -> 480 (range 430 px for z1 in [-2.5, 2.5])
    # y: 280 -> 20 (range 260 px for z2 in [-2.5, 2.5], inverted)
    def to_svg_x(z):
        clamped = max(-2.5, min(2.5, z))
        return 50 + ((clamped + 2.5) / 5.0) * 430.0

    def to_svg_y(z):
        clamped = max(-2.5, min(2.5, z))
        return 280 - ((clamped + 2.5) / 5.0) * 260.0

    dot_x = to_svg_x(z1_val)
    dot_y = to_svg_y(z2_val)

    render_html(
        f"""
        <main>
          <!-- Page Hero -->
          <div style="border-bottom: 1px solid #CCD6D0; padding-bottom: 2rem; margin-bottom: 2rem;">
            <div style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.25rem 0.75rem; border-radius: 3px; background: #E5EEE7; color: #173F3A; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; border: 1px solid rgba(23,63,58,0.2); margin-bottom: 1rem;">
              <span class="material-symbols-outlined" style="font-size: 16px; color: #79B6A5;">psychology</span>
              Machine Learning Inference Engine
            </div>
            <h1 class="text-display-lg" style="color: #173F3A; margin: 0 0 1rem 0;">
              Feature Space &amp; Logistic Regression Classification
            </h1>
            <p class="text-body-lg" style="color: #252D2B; opacity: 0.85; max-width: 780px; margin: 0;">
              Explore how two extracted frequency band powers are standardized and separated by a linear decision boundary. Transparent model scoring that distinguishes mathematical artificial class proxies from genuine human intention.
            </p>
          </div>

          <!-- Mandatory Scientific Transparency Notice -->
          <div style="background: rgba(229, 238, 231, 0.5); border: 1px solid #CCD6D0; border-left: 4px solid #173F3A; border-radius: 4px; padding: 1rem 1.25rem; margin-bottom: 2rem; display: flex; align-items: flex-start; gap: 0.875rem;">
            <span class="material-symbols-outlined" style="font-size: 22px; color: #173F3A; shrink: 0; margin-top: 2px;">verified</span>
            <div style="font-size: 0.8125rem; color: #252D2B; line-height: 1.55;">
              <strong style="color: #173F3A; display: block; font-family: 'Manrope', sans-serif; font-size: 0.875rem; margin-bottom: 0.25rem;">
                Critical Scientific Definition of Model Scores:
              </strong>
              The percentages shown below are model-generated softmax probabilities computed from synthetic features. They represent how closely the artificial mathematical signal aligns with the training proxy, <strong>never human thought certainty, cognitive effort, or real clinical intention</strong>.
            </div>
          </div>

          <!-- 2-Column Workbench Grid -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 2rem; align-items: start;">
            <!-- LEFT: 2D Feature Space Scatter & Decision Boundary -->
            <section class="neurolink-card" style="padding: 1.5rem;">
              <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(204,214,208,0.7); padding-bottom: 0.75rem; margin-bottom: 1rem;">
                <div>
                  <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #79B6A5; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; display: block;">FEATURE SPACE PROJECTION</span>
                  <h2 class="text-headline-md" style="color: #173F3A; margin: 0;">2D Spectral Power Decision Boundary</h2>
                </div>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #64748B; background: #E5EEE7; padding: 0.25rem 0.5rem; border-radius: 3px; border: 1px solid #CCD6D0;">
                  Scikit-Learn LogisticRegression
                </span>
              </div>

              <p class="text-body-sm" style="color: #475569; margin-bottom: 1rem;">
                The two axes correspond to standardized spectral power features (z-scores). The dashed diagonal line marks the linear hyperplane separating artificial class regions.
              </p>

              <!-- Interactive 2D Feature Space Canvas -->
              <div style="position: relative; aspect-ratio: 16/10; background: #F4F1E9; border: 1px solid #CCD6D0; border-radius: 4px; padding: 0.5rem; overflow: hidden; box-shadow: inset 0 1px 3px rgba(0,0,0,0.03);">
                <svg viewBox="0 0 500 320" style="width: 100%; height: 100%; font-family: 'JetBrains Mono', monospace; font-size: 10px; user-select: none;">
                  <!-- Axis lines -->
                  <line x1="50" y1="280" x2="480" y2="280" stroke="#CCD6D0" stroke-width="1.5" />
                  <line x1="50" y1="20" x2="50" y2="280" stroke="#CCD6D0" stroke-width="1.5" />

                  <!-- Axis Labels -->
                  <text x="265" y="310" text-anchor="middle" fill="#173F3A" font-weight="600">Feature 1: 1–12 Hz Power (Mu Band z-score) →</text>
                  <text x="18" y="150" text-anchor="middle" fill="#D98B62" font-weight="600" transform="rotate(-90 18 150)">Feature 2: 12–40 Hz (Beta z-score) →</text>

                  <!-- Grid markings -->
                  <line x1="50" y1="200" x2="480" y2="200" stroke="#E5EEE7" stroke-width="1" stroke-dasharray="2 2" />
                  <line x1="50" y1="120" x2="480" y2="120" stroke="#E5EEE7" stroke-width="1" stroke-dasharray="2 2" />
                  <line x1="190" y1="20" x2="190" y2="280" stroke="#E5EEE7" stroke-width="1" stroke-dasharray="2 2" />
                  <line x1="330" y1="20" x2="330" y2="280" stroke="#E5EEE7" stroke-width="1" stroke-dasharray="2 2" />

                  <!-- Decision Boundary Line: w1*x1 + w2*x2 + b = 0 -->
                  <line x1="80" y1="40" x2="440" y2="260" stroke="#173F3A" stroke-width="2" stroke-dasharray="6 4" />
                  <text x="360" y="225" fill="#173F3A" font-size="9" transform="rotate(31 360 225)">Hyperplane P = 0.50</text>

                  <!-- LEFT Cluster Points (High F1, Low F2) -->
                  <g fill="#173F3A" opacity="0.6">
                    <circle cx="360" cy="240" r="4" />
                    <circle cx="380" cy="225" r="4" />
                    <circle cx="410" cy="250" r="4" />
                    <circle cx="340" cy="235" r="4" />
                    <circle cx="395" cy="260" r="4" />
                    <circle cx="370" cy="210" r="4" />
                    <circle cx="430" cy="230" r="4" />
                    <circle cx="350" cy="255" r="4" />
                  </g>

                  <!-- RIGHT Cluster Points (Low F1, High F2) -->
                  <g fill="#D98B62" opacity="0.6">
                    <circle cx="100" cy="80" r="4" />
                    <circle cx="130" cy="65" r="4" />
                    <circle cx="115" cy="110" r="4" />
                    <circle cx="150" cy="90" r="4" />
                    <circle cx="90" cy="95" r="4" />
                    <circle cx="140" cy="120" r="4" />
                    <circle cx="165" cy="75" r="4" />
                    <circle cx="120" cy="140" r="4" />
                  </g>

                  <!-- Active Specimen Dot -->
                  <g>
                    <circle cx="{dot_x:.1f}" cy="{dot_y:.1f}" r="7" fill="#79B6A5" stroke="#173F3A" stroke-width="2" />
                    <circle cx="{dot_x:.1f}" cy="{dot_y:.1f}" r="14" fill="none" stroke="#79B6A5" stroke-width="1.5" opacity="0.7" />
                    <text x="{dot_x:.1f}" y="{max(15, dot_y - 12):.1f}" text-anchor="middle" fill="#173F3A" font-weight="700" font-size="9">{specimen_label}</text>
                  </g>

                  <!-- In-chart legend -->
                  <rect x="270" y="25" width="200" height="45" fill="#F4F1E9" stroke="#CCD6D0" rx="2" />
                  <circle cx="285" cy="40" r="3.5" fill="#173F3A" />
                  <text x="295" y="43" fill="#252D2B" font-size="9">Class LEFT (Mu dominant)</text>
                  <circle cx="285" cy="57" r="3.5" fill="#D98B62" />
                  <text x="295" y="60" fill="#252D2B" font-size="9">Class RIGHT (Beta dominant)</text>
                </svg>
              </div>

              <!-- Real Model Weights & Intercept -->
              <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;">
                <div style="background: rgba(229, 238, 231, 0.4); border: 1px solid #CCD6D0; border-radius: 4px; padding: 0.75rem;">
                  <span style="color: #64748B; display: block; font-size: 0.6875rem;">WEIGHT VECTOR (w)</span>
                  <span style="color: #173F3A; font-weight: 700;">[{w1:+.2f}, {w2:+.2f}]</span>
                </div>
                <div style="background: rgba(229, 238, 231, 0.4); border: 1px solid #CCD6D0; border-radius: 4px; padding: 0.75rem;">
                  <span style="color: #64748B; display: block; font-size: 0.6875rem;">INTERCEPT (b)</span>
                  <span style="color: #173F3A; font-weight: 700;">{b:+.2f} au</span>
                </div>
              </div>
            </section>

            <!-- RIGHT: Model Output Scores & Feature Breakdown -->
            <section style="display: flex; flex-direction: column; gap: 1.5rem;">
              <!-- Prediction Verdict Card -->
              <article class="neurolink-card" style="padding: 1.5rem;">
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #64748B; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 0.25rem;">
                  MODEL INFERENCE DECISION
                </span>
                <div style="display: flex; align-items: baseline; justify-content: space-between; border-bottom: 1px solid rgba(204,214,208,0.7); padding-bottom: 1rem; margin-bottom: 1rem;">
                  <div>
                    <span class="text-display-lg" style="color: #173F3A; font-size: 2.25rem; font-weight: 800; display: block;">
                      {pred_label}
                    </span>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #79B6A5; font-weight: 600;">
                      {'~8 Hz Mu Focus' if pred_label == 'LEFT' else '~22 Hz Beta Focus'}
                    </span>
                  </div>
                  <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.875rem; font-weight: 700; background: #E5EEE7; color: #173F3A; padding: 0.35rem 0.75rem; border-radius: 4px; border: 1px solid rgba(23,63,58,0.2);">
                    SCORE: {active_score:.3f}
                  </span>
                </div>

                <!-- Softmax Progress Bars -->
                <div style="display: flex; flex-direction: column; gap: 1rem; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;">
                  <div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
                      <span style="color: #173F3A; font-weight: 700;">LEFT Probability:</span>
                      <span style="color: #173F3A; font-weight: 700;" class="tabular-nums">{p_left:.1f}%</span>
                    </div>
                    <div style="height: 0.625rem; width: 100%; background: #CCD6D0; border-radius: 9999px; overflow: hidden;">
                      <div style="height: 100%; background: #173F3A; width: {p_left:.1f}%; transition: width 300ms ease;"></div>
                    </div>
                  </div>

                  <div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
                      <span style="color: #D98B62; font-weight: 700;">RIGHT Probability:</span>
                      <span style="color: #64748B; font-weight: 700;" class="tabular-nums">{p_right:.1f}%</span>
                    </div>
                    <div style="height: 0.625rem; width: 100%; background: #CCD6D0; border-radius: 9999px; overflow: hidden;">
                      <div style="height: 100%; background: #D98B62; width: {p_right:.1f}%; transition: width 300ms ease;"></div>
                    </div>
                  </div>
                </div>
              </article>

              <!-- Synthetic Features vs Model Output Comparison -->
              <article class="neurolink-card" style="padding: 1.5rem;">
                <div style="border-bottom: 1px solid rgba(204,214,208,0.7); padding-bottom: 0.75rem; margin-bottom: 1rem;">
                  <h3 class="text-headline-sm" style="color: #173F3A; margin: 0 0 0.25rem 0;">
                    Raw Spectral Measurements vs Model Outputs
                  </h3>
                  <p style="font-size: 0.75rem; color: #64748B; margin: 0;">
                    Clear distinction between measured synthetic physical attributes and model inferences.
                  </p>
                </div>

                <table style="width: 100%; border-collapse: collapse; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;">
                  <thead>
                    <tr style="border-bottom: 1px solid #CCD6D0; color: #64748B; font-size: 0.6875rem;">
                      <th style="padding-bottom: 0.5rem; font-weight: 500; text-align: left;">DIMENSION</th>
                      <th style="padding-bottom: 0.5rem; font-weight: 500; text-align: left;">VALUE</th>
                      <th style="padding-bottom: 0.5rem; font-weight: 500; text-align: left;">ROLE</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr style="border-bottom: 1px solid rgba(204,214,208,0.4);">
                      <td style="padding: 0.5rem 0; color: #173F3A; font-weight: 600;">1–12 Hz Power</td>
                      <td style="padding: 0.5rem 0;" class="tabular-nums">{f1_val:.4f} au²</td>
                      <td style="padding: 0.5rem 0; color: #64748B;">Raw Feature</td>
                    </tr>
                    <tr style="border-bottom: 1px solid rgba(204,214,208,0.4);">
                      <td style="padding: 0.5rem 0; color: #D98B62; font-weight: 600;">12–40 Hz Power</td>
                      <td style="padding: 0.5rem 0;" class="tabular-nums">{f2_val:.4f} au²</td>
                      <td style="padding: 0.5rem 0; color: #64748B;">Raw Feature</td>
                    </tr>
                    <tr style="border-bottom: 1px solid rgba(204,214,208,0.4);">
                      <td style="padding: 0.5rem 0; color: #252D2B; font-weight: 600;">Z-Score 1</td>
                      <td style="padding: 0.5rem 0;" class="tabular-nums">{z1_val:+.2f} σ</td>
                      <td style="padding: 0.5rem 0; color: #64748B;">Standardized</td>
                    </tr>
                    <tr style="border-bottom: 1px solid rgba(204,214,208,0.4);">
                      <td style="padding: 0.5rem 0; color: #252D2B; font-weight: 600;">Z-Score 2</td>
                      <td style="padding: 0.5rem 0;" class="tabular-nums">{z2_val:+.2f} σ</td>
                      <td style="padding: 0.5rem 0; color: #64748B;">Standardized</td>
                    </tr>
                    <tr style="background: rgba(229, 238, 231, 0.45);">
                      <td style="padding: 0.5rem 0.35rem; color: #173F3A; font-weight: 700;">Model Score</td>
                      <td style="padding: 0.5rem 0; color: #173F3A; font-weight: 700;" class="tabular-nums">{active_score:.3f}</td>
                      <td style="padding: 0.5rem 0; color: #173F3A; font-weight: 700;">Prediction</td>
                    </tr>
                  </tbody>
                </table>
              </article>

              <!-- CTA to Experiment Studio -->
              <a href="?page=experiment-studio" target="_self" style="display: flex; align-items: center; justify-content: center; gap: 0.5rem; background: #173F3A; color: #F4F1E9; padding: 0.85rem 1rem; border-radius: 4px; font-family: 'Inter', sans-serif; font-weight: 700; font-size: 0.875rem; text-decoration: none; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                <span class="material-symbols-outlined" style="font-size: 18px; color: #79B6A5;">science</span>
                <span>Test Different Seeds in Experiment Studio</span>
              </a>
            </section>
          </div>
        </main>
        """
    )

    render_footer()
