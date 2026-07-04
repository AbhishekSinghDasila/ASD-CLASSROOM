import streamlit as st
from src.utils.theme import get_theme


def style_background_home():
    t = get_theme()
    st.markdown(f"""
        <style>
                .stApp {{
                    background: radial-gradient(circle at 20% 0%, {t['brand_secondary']} 0%, {t['app_bg_home']} 55%) !important;
                }}
                .stApp div[data-testid="stColumn"]{{
                    background-color:{t['surface']} !important;
                    padding:2.5rem !important;
                    border-radius: 2rem !important;
                    box-shadow: 0 25px 60px {t['shadow']} !important;
                    border: 1px solid {t['border']} !important;
                    }}
        </style>
                """, unsafe_allow_html=True)


def style_background_dashboard():
    t = get_theme()
    st.markdown(f"""
        <style>
                .stApp {{
                    background: {t['app_bg']} !important;
                }}
        </style>
                """, unsafe_allow_html=True)


def style_base_layout():
    t = get_theme()
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Sora:wght@400..800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400..700&display=swap');
        @import url('https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css');

            #MainMenu, footer, header {{
                visibility: hidden;
            }}

            .block-container {{
                padding-top:1.5rem !important;
            }}

            .stApp {{
                transition: background 0.3s ease;
            }}

            /* ---- Live theme tokens (recomputed every render) ---- */
            :root {{
                --brand-primary: {t['brand_primary']};
                --brand-secondary: {t['brand_secondary']};
                --brand-dark: {t['text_heading']};
                --brand-ink: {t['brand_ink']};
                --text-bright: {t['text_bright']};
                --text-body: {t['text_body']};
                --surface: {t['surface']};
                --surface-muted: {t['surface_alt']};
                --border-color: {t['border']};
                --shadow-color: {t['shadow']};
            }}

            h1 {{
                font-family: 'Sora', sans-serif !important;
                font-weight: 800 !important;
                font-size: 3rem !important;
                line-height:1.15 !important;
                margin-bottom:0.4rem !important;
                color: var(--brand-dark) !important;
                letter-spacing: -0.02em !important;
                background: linear-gradient(90deg, var(--brand-primary), var(--brand-secondary));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                display: inline-block;
            }}

            h2 {{
                font-family: 'Sora', sans-serif !important;
                font-weight: 700 !important;
                font-size: 1.75rem !important;
                line-height:1.2 !important;
                margin-bottom:0rem !important;
                color: var(--brand-dark) !important;
            }}

            h3, h4, p {{
                font-family: 'Inter', sans-serif;
                color: var(--text-body) !important;
            }}

            /* ---- Cards: give panels depth instead of flat fills ---- */
            div[data-testid="stVerticalBlockBorderWrapper"] {{
                background: var(--surface) !important;
                border-radius: 1.25rem !important;
                border: 1px solid var(--border-color) !important;
                box-shadow: 0 8px 24px var(--shadow-color) !important;
                transition: transform 0.2s ease, box-shadow 0.2s ease !important;
            }}
            div[data-testid="stVerticalBlockBorderWrapper"]:hover {{
                transform: translateY(-2px) !important;
                box-shadow: 0 14px 34px var(--shadow-color) !important;
            }}

            /* ---- Inputs ---- */
            input, textarea, .stSelectbox div[data-baseweb="select"] {{
                border-radius: 0.75rem !important;
                border: 1.5px solid var(--border-color) !important;
                background: var(--surface) !important;
                color: var(--text-body) !important;
            }}

            /* ---- Buttons ---- */
            button{{
                border-radius: 0.85rem !important;
                background: linear-gradient(135deg, var(--brand-primary), var(--brand-secondary)) !important;
                color: var(--text-bright) !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 600 !important;
                padding: 10px 22px !important;
                border: none !important;
                box-shadow: 0 4px 14px var(--shadow-color) !important;
                transition: transform 0.2s ease, box-shadow 0.2s ease !important;
                }}
            button[kind="secondary"]{{
                border-radius: 0.85rem !important;
                background: var(--surface) !important;
                color: var(--brand-primary) !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 600 !important;
                padding: 10px 22px !important;
                border: 1.5px solid var(--brand-primary) !important;
                transition: transform 0.2s ease, background-color 0.2s ease !important;
                }}
            button[kind="tertiary"]{{
                border-radius: 0.85rem !important;
                background: var(--brand-ink) !important;
                color: var(--text-bright) !important;
                font-family: 'Inter', sans-serif !important;
                font-weight: 600 !important;
                padding: 10px 22px !important;
                border: none !important;
                transition: transform 0.2s ease !important;
                }}
            button:hover{{
                transform: scale(1.03) !important;
            }}
            button[kind="secondary"]:hover {{
                background-color: var(--surface-muted) !important;
            }}

            /* ---- Badge / pill helper, e.g. "Live", "New" tags ---- */
            .pill {{
                display:inline-flex; align-items:center; gap:6px;
                padding: 4px 12px;
                border-radius: 999px;
                font-family: 'Inter', sans-serif;
                font-size: 0.78rem;
                font-weight: 600;
                background: color-mix(in srgb, var(--brand-primary) 15%, transparent);
                color: var(--brand-primary);
            }}

            /* ---- Icon helper class ---- */
            .icon {{
                font-size: 1.2rem;
                vertical-align: -2px;
                margin-right: 6px;
                color: var(--brand-primary);
            }}
        </style>
                """, unsafe_allow_html=True)


def icon(name: str, size: str = "1.2rem", color: str = None) -> str:
    """
    Returns an HTML snippet for a Bootstrap Icon.
    Usage: st.markdown(icon("house-door-fill"), unsafe_allow_html=True)
    Browse icon names at https://icons.getbootstrap.com/
    """
    t = get_theme()
    color = color or t["brand_primary"]
    return f'<i class="bi bi-{name}" style="font-size:{size};color:{color};"></i>'


def pill(text: str, icon_name: str = None) -> str:
    """Small rounded badge, e.g. pill('Live', 'broadcast')"""
    icon_html = f'<i class="bi bi-{icon_name}"></i> ' if icon_name else ""
    return f'<span class="pill">{icon_html}{text}</span>'