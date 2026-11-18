"""Shared UI components for NeuroLink: headers, navigation, footers, and disclaimer."""
import html
import streamlit as st
from ui_theme import render_html


def render_header(current_page: str, page_title: str = "") -> None:
    """Render the approved Stitch desktop and mobile navigation header."""
    nav_items = [
        ("landing", "Introduction", "01 // Introduction", "neurology"),
        ("experiment-studio", "Experiment Studio", "02 // Experiment Studio", "science"),
        ("signal-processing", "Signal Processing", "03 // Signal Processing", "timeline"),
        ("classification-lab", "Classification Lab", "04 // Classification Lab", "psychology"),
        ("learn-bci", "Learn BCI", "05 // Learn BCI", "menu_book"),
    ]

    # Generate desktop links
    desktop_links_html = []
    for route, title, _, _ in nav_items:
        is_active = (current_page == route)
        cls = "neurolink-nav-link active" if is_active else "neurolink-nav-link"
        desktop_links_html.append(
            f'<a href="?page={route}" target="_self" class="{cls}">{html.escape(title)}</a>'
        )
    desktop_nav_markup = "\n".join(desktop_links_html)

    # Right side action/badge per screen
    if current_page == "experiment-studio":
        right_action_markup = """
        <div class="neurolink-header-badge" style="display: flex; align-items: center; gap: 0.4rem; background: #E5EEE7; padding: 0.3rem 0.65rem; border-radius: 3px; border: 1px solid rgba(23,63,58,0.2); font-family: 'JetBrains Mono', monospace; font-size: 0.6875rem; color: #173F3A; font-weight: 600;">
          <span style="display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #173F3A;"></span>
          <span class="desktop-text">SYNTHETIC RUNNER READY</span>
          <span class="mobile-text">READY</span>
        </div>
        """
    elif current_page == "landing":
        right_action_markup = """
        <a href="?page=experiment-studio" target="_self" class="neurolink-nav-cta">
          <span class="desktop-text">Explore Laboratory</span>
          <span class="mobile-text">Studio</span>
          <span class="material-symbols-outlined" style="font-size: 14px; color: #79B6A5;">arrow_forward</span>
        </a>
        """
    else:
        right_action_markup = """
        <a href="?page=experiment-studio" target="_self" class="neurolink-nav-cta">
          <span class="desktop-text">Open Studio</span>
          <span class="mobile-text">Studio</span>
          <span class="material-symbols-outlined" style="font-size: 14px; color: #79B6A5;">arrow_forward</span>
        </a>
        """

    # Mobile nav items markup
    mobile_links_html = []
    for route, _, label, icon in nav_items:
        is_active = (current_page == route)
        cls = "neurolink-mobile-link active" if is_active else "neurolink-mobile-link"
        mobile_links_html.append(
            f'<a href="?page={route}" target="_self" class="{cls}">'
            f'  <span style="display: flex; align-items: center; gap: 0.5rem;">'
            f'    <span class="material-symbols-outlined" style="font-size: 16px;">{icon}</span>'
            f'    <span>{html.escape(label)}</span>'
            f'  </span>'
            f'  <span class="material-symbols-outlined" style="font-size: 14px;">arrow_forward</span>'
            f'</a>'
        )
    mobile_nav_markup = "\n".join(mobile_links_html)

    page_title_html = (
        f'<span class="neurolink-header-breadcrumb" style="color: #CCD6D0; margin: 0 0.25rem;">/</span>'
        f'<span class="neurolink-header-breadcrumb" style="font-family: \'JetBrains Mono\', monospace; font-size: 0.75rem; color: #173F3A; font-weight: 600;">{html.escape(page_title)}</span>'
        if page_title
        else ""
    )

    header_html = f"""
    <header class="neurolink-topbar">
      <div class="neurolink-nav-inner">
        <!-- Brand Identity (Left) -->
        <div style="display: flex; align-items: center; gap: 0.75rem;">
          <a href="?page=landing" target="_self" class="neurolink-brand">
            <div class="neurolink-brand-icon">
              <span class="material-symbols-outlined" style="font-size: 16px;">neurology</span>
            </div>
            <div style="display: flex; flex-direction: column;">
              <span class="neurolink-brand-text">NEUROLINK</span>
              <span style="font-family: 'JetBrains Mono', monospace; font-size: 9px; letter-spacing: 0.1em; color: #64748B; line-height: 1;">BCI SIMULATOR</span>
            </div>
          </a>
          {page_title_html}
        </div>

        <!-- Desktop Navigation (Center) -->
        <nav class="neurolink-nav-links" aria-label="Main Navigation">
          {desktop_nav_markup}
        </nav>

        <!-- Right Side CTA / Status (Desktop) -->
        <div class="neurolink-desktop-right" style="display: flex; align-items: center; gap: 0.75rem;">
          {right_action_markup}
        </div>

        <!-- Mobile Hamburger Menu (Details / Summary toggle) -->
        <details class="neurolink-mobile-details">
          <summary class="neurolink-mobile-summary" title="Toggle Navigation Menu">
            <span class="material-symbols-outlined" style="font-size: 20px;">menu</span>
          </summary>
          <div class="neurolink-mobile-dropdown">
            {mobile_nav_markup}
          </div>
        </details>
      </div>
    </header>
    """
    render_html(header_html)


def render_disclaimer_banner(link_to_limitations: bool = True) -> None:
    """Render the official scientific transparency disclaimer banner."""
    link_html = (
        '<a href="?page=learn-bci#limitations" target="_self" style="font-weight: 600; color: #173F3A; font-size: 0.8125rem; white-space: nowrap; text-decoration: underline; margin-left: auto;">Read Full Limits</a>'
        if link_to_limitations
        else ""
    )
    banner_html = f"""
    <div class="neurolink-disclaimer-box">
      <span class="material-symbols-outlined" style="font-size: 22px; color: #173F3A; shrink: 0; margin-top: 2px;">verified_user</span>
      <div style="flex: 1;">
        <div class="neurolink-disclaimer-title">Scientific Transparency & Pedagogical Disclaimer</div>
        <p class="neurolink-disclaimer-text">
          This is an educational simulator using synthetic EEG-like signals, not live brain data. LEFT and RIGHT are artificial demonstration labels. It does not read thoughts, measure human intentions, or provide medical or clinical predictions.
        </p>
      </div>
      {link_html}
    </div>
    """
    render_html(banner_html)


def render_footer() -> None:
    """Render the approved editorial laboratory footer."""
    footer_html = """
    <footer class="neurolink-footer">
      <div class="neurolink-footer-inner">
        <div style="display: flex; align-items: center; gap: 0.5rem;">
          <span style="display: inline-block; width: 8px; height: 8px; background: #173F3A; border-radius: 2px;"></span>
          <strong style="color: #173F3A; font-family: 'Manrope', sans-serif;">NeuroLink Simulator</strong>
          <span>• Biology for Engineers Experiential Learning (Class CE-SE-A, Team 2)</span>
        </div>
        <div style="display: flex; align-items: center; gap: 1.25rem;">
          <a href="?page=landing" target="_self" class="neurolink-footer-nav">Overview</a>
          <a href="?page=experiment-studio" target="_self" class="neurolink-footer-nav">Studio</a>
          <a href="?page=signal-processing" target="_self" class="neurolink-footer-nav">Pipeline</a>
          <a href="?page=classification-lab" target="_self" class="neurolink-footer-nav">Classifier</a>
          <a href="?page=learn-bci" target="_self" class="neurolink-footer-nav">Monograph</a>
          <a href="https://github.com/CoBrIX44/neurolink-bci-simulator" target="_blank" rel="noopener" style="color: #173F3A; text-decoration: underline;">GitHub</a>
        </div>
      </div>
    </footer>
    """
    render_html(footer_html)
