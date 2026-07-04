import streamlit as st
from src.utils.theme import get_theme

APP_NAME = "ASD-CLASSROOM"  # Application name to be displayed in the footer


def footer_home():
    t = get_theme()
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:8px; justify-content:center; align-items:center;">
            <i class="bi bi-mortarboard-fill" style="font-size:1rem; color:{t['text_bright']};"></i>
            <p style="font-family:'Inter', sans-serif; font-weight:500; font-size:0.9rem; color:{t['text_bright']}; margin:0; opacity:0.85;">
                {APP_NAME} &middot; crafted for focused learning
            </p>
        </div>
                """, unsafe_allow_html=True)


def footer_dashboard():
    t = get_theme()
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:8px; justify-content:center; align-items:center;">
            <i class="bi bi-mortarboard-fill" style="font-size:1rem; color:{t['brand_primary']};"></i>
            <p style="font-family:'Inter', sans-serif; font-weight:500; font-size:0.9rem; color:{t['text_body']}; margin:0;">
                {APP_NAME} &middot; crafted for focused learning
            </p>
        </div>
                """, unsafe_allow_html=True)