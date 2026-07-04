import streamlit as st

THEMES = {
    "light": {
        "app_bg": "#F8FAFC",
        "app_bg_home": "#4F46E5",
        "surface": "#FFFFFF",
        "surface_alt": "#F1F5F9",
        "text_heading": "#1E1B4B",
        "text_body": "#475569",
        "text_bright": "#F8FAFC",
        "brand_primary": "#4F46E5",
        "brand_secondary": "#7C3AED",
        "brand_ink": "#0F172A",
        "border": "#E2E8F0",
        "shadow": "rgba(15, 23, 42, 0.10)",
    },
    "dark": {
        "app_bg": "#0B1120",
        "app_bg_home": "#1E1B4B",
        "surface": "#1E293B",
        "surface_alt": "#273449",
        "text_heading": "#F8FAFC",
        "text_body": "#CBD5E1",
        "text_bright": "#F8FAFC",
        "brand_primary": "#818CF8",
        "brand_secondary": "#A78BFA",
        "brand_ink": "#F8FAFC",
        "border": "#334155",
        "shadow": "rgba(0, 0, 0, 0.45)",
    },
}


def init_theme():
    if "theme_mode" not in st.session_state:
        st.session_state["theme_mode"] = "light"


def get_theme() -> dict:
    init_theme()
    return THEMES[st.session_state["theme_mode"]]


def theme_toggle():
    """
    Renders a small light/dark toggle button.
    Call this once per page (e.g. right after the header).
    """
    init_theme()
    is_dark = st.session_state["theme_mode"] == "dark"

    left, right = st.columns([8, 1])
    with right:
        if st.button("☀️" if is_dark else "🌙", key="theme_toggle_btn", help="Switch appearance"):
            st.session_state["theme_mode"] = "light" if is_dark else "dark"
            st.rerun()