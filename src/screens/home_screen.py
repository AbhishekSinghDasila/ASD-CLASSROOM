import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout
from src.utils.theme import get_theme, theme_toggle


def _clean(html: str) -> str:
    """
    Strips leading whitespace from every line before handing to st.markdown.
    Prevents Streamlit's markdown parser from mistaking indented HTML for a
    fenced code block (4+ leading spaces = code block in CommonMark).
    """
    return "\n".join(line.strip() for line in html.strip("\n").split("\n"))


def _hero_illustration(t: dict) -> str:
    """Self-contained, theme-aware SVG illustration: a teacher and a seated student."""
    skin = "#F4C9A0"
    return _clean(f"""
    <div style="display:flex; align-items:center; justify-content:center; height:100%; min-height:440px;">
      <svg width="100%" height="440" viewBox="0 0 460 420" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="heroGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{t['brand_primary']}"/>
            <stop offset="100%" stop-color="{t['brand_secondary']}"/>
          </linearGradient>
        </defs>

        <ellipse cx="230" cy="368" rx="190" ry="16" fill="{t['brand_primary']}" opacity="0.08"/>

        <rect x="90" y="300" width="280" height="16" rx="8" fill="{t['border']}"/>
        <rect x="110" y="316" width="14" height="40" fill="{t['border']}"/>
        <rect x="336" y="316" width="14" height="40" fill="{t['border']}"/>

        <g>
          <rect x="190" y="86" width="90" height="60" rx="8" fill="{t['surface']}" stroke="{t['border']}" stroke-width="2"/>
          <path d="M206 118 L222 132 L256 100" stroke="url(#heroGrad)" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        </g>

        <g>
          <path d="M100 300 C100 250 108 220 145 220 C182 220 190 250 190 300 Z" fill="url(#heroGrad)"/>
          <circle cx="145" cy="188" r="30" fill="{skin}"/>
          <path d="M118 178 a27 24 0 0 1 54 0 L172 170 a27 20 0 0 0 -54 0 Z" fill="{t['brand_ink']}"/>
          <path d="M175 240 L206 205" stroke="url(#heroGrad)" stroke-width="12" stroke-linecap="round"/>
          <circle cx="145" cy="300" r="0" />
        </g>

        <g>
          <rect x="288" y="230" width="70" height="34" rx="10" fill="{t['border']}"/>
          <path d="M296 260 C296 230 302 210 323 210 C344 210 350 230 350 260 Z" fill="url(#heroGrad)" opacity="0.92"/>
          <circle cx="323" cy="188" r="26" fill="{skin}"/>
          <path d="M299 180 a24 22 0 0 1 48 0 L343 172 a24 18 0 0 0 -48 0 Z" fill="{t['brand_ink']}"/>
          <g transform="translate(300,246)">
            <path d="M0 0 L20 -6 L20 14 L0 20 Z" fill="{t['surface']}" stroke="{t['border']}" stroke-width="1.5"/>
            <path d="M40 0 L20 -6 L20 14 L40 20 Z" fill="{t['surface']}" stroke="{t['border']}" stroke-width="1.5"/>
          </g>
        </g>

        <g>
          <circle cx="60" cy="120" r="20" fill="{t['surface']}" stroke="{t['border']}" stroke-width="2">
            <animateTransform attributeName="transform" type="translate" values="0 0; 0 -10; 0 0" dur="3.2s" repeatCount="indefinite"/>
          </circle>
          <path d="M52 120 L58 126 L70 112" stroke="url(#heroGrad)" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <animateTransform attributeName="transform" type="translate" values="0 0; 0 -10; 0 0" dur="3.2s" repeatCount="indefinite"/>
          </path>

          <circle cx="400" cy="150" r="18" fill="{t['surface']}" stroke="{t['border']}" stroke-width="2">
            <animateTransform attributeName="transform" type="translate" values="0 0; 0 10; 0 0" dur="2.6s" repeatCount="indefinite"/>
          </circle>
          <text x="391" y="157" font-size="18" font-family="Inter, sans-serif">
            <animateTransform attributeName="transform" type="translate" values="0 0; 0 10; 0 0" dur="2.6s" repeatCount="indefinite"/>
            📘
          </text>

          <circle cx="370" cy="60" r="14" fill="url(#heroGrad)" opacity="0.85">
            <animateTransform attributeName="transform" type="translate" values="0 0; -8 -6; 0 0" dur="3.8s" repeatCount="indefinite"/>
          </circle>
        </g>
      </svg>
    </div>
    """)


def _register_card(t: dict, fa_icon: str, title: str, tagline: str, button_label: str, session_key: str):
    with st.container(border=True):
        st.markdown(_clean(f"""
            <div style="display:flex; align-items:center; gap:14px; margin-bottom:6px;">
                <div style="
                    width:52px; height:52px; flex-shrink:0;
                    display:flex; align-items:center; justify-content:center;
                    border-radius:14px;
                    background: linear-gradient(135deg, {t['brand_primary']}, {t['brand_secondary']});
                    box-shadow: 0 6px 16px {t['shadow']};
                ">
                    <i class="fa-solid {fa_icon}" style="font-size:1.4rem; color:{t['text_bright']};"></i>
                </div>
                <div>
                    <h2 style="margin:0;">{title}</h2>
                    <p style="margin:0; font-size:0.9rem;">{tagline}</p>
                </div>
            </div>
        """), unsafe_allow_html=True)

        if st.button(button_label, type='primary', icon=':material/arrow_outward:',
                     icon_position='right', key=f"btn_{session_key}", use_container_width=True):
            st.session_state['login_type'] = session_key
            st.rerun()


def _animated_white_background(t: dict):
    """Soft, theme-aware base with slow-drifting, gentle gradient blobs for visual life."""
    st.markdown(_clean(f"""
        <style>
            .stApp {{
                background: {t['app_bg']} !important;
                position: relative;
                overflow: hidden;
            }}
            .stApp::before, .stApp::after {{
                content: "";
                position: fixed;
                width: 520px;
                height: 520px;
                border-radius: 50%;
                filter: blur(150px);
                opacity: 0.16;
                z-index: 0;
                pointer-events: none;
            }}
            .stApp::before {{
                background: {t['brand_primary']};
                top: -160px;
                left: -160px;
                animation: floatBlobA 14s ease-in-out infinite;
            }}
            .stApp::after {{
                background: {t['brand_secondary']};
                bottom: -180px;
                right: -140px;
                animation: floatBlobB 16s ease-in-out infinite;
            }}
            @keyframes floatBlobA {{
                0%, 100% {{ transform: translate(0, 0) scale(1); }}
                50%      {{ transform: translate(60px, 40px) scale(1.15); }}
            }}
            @keyframes floatBlobB {{
                0%, 100% {{ transform: translate(0, 0) scale(1); }}
                50%      {{ transform: translate(-50px, -30px) scale(1.1); }}
            }}
            [data-testid="stAppViewContainer"], [data-testid="stHeader"] {{
                position: relative;
                z-index: 1;
            }}
        </style>
    """), unsafe_allow_html=True)


def home_screen():
    t = get_theme()

    st.markdown(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">',
        unsafe_allow_html=True
    )

    _animated_white_background(t)
    style_base_layout()
    header_home()
    theme_toggle()

    left, right = st.columns([1.1, 1], gap="large")

    with left:
        st.markdown(_hero_illustration(t), unsafe_allow_html=True)

    with right:
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        _register_card(
            t,
            fa_icon="fa-user-graduate",
            title="I'm a Student",
            tagline="Mark attendance in seconds",
            button_label="Register as Student",
            session_key="student",
        )
        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
        _register_card(
            t,
            fa_icon="fa-chalkboard-user",
            title="I'm a Teacher",
            tagline="Manage classes effortlessly",
            button_label="Register as Teacher",
            session_key="teacher",
        )

    footer_home()