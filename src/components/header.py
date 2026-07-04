import streamlit as st
from src.utils.theme import get_theme


def header_home():
    t = get_theme()
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:20px; margin-top:10px; gap:12px;">
            <div style="
                width:80px; height:80px;
                display:flex; align-items:center; justify-content:center;
                background: linear-gradient(135deg, {t['brand_primary']}, {t['brand_secondary']});
                border-radius:20px;
                box-shadow: 0 10px 26px {t['shadow']};
            ">
                <i class="bi bi-mortarboard-fill" style="font-size:2.3rem; color:{t['text_bright']};"></i>
            </div>
            <h1 style='text-align:center; margin:0; color:{t["text_heading"]} !important; -webkit-text-fill-color:{t["text_heading"]} !important; background:none !important;'>ASD-CLASSROOMS</h1>
        </div>
                """, unsafe_allow_html=True)


def header_dashboard():
    t = get_theme()
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:14px;">
            <div style="
                width:64px; height:64px;
                display:flex; align-items:center; justify-content:center;
                background: linear-gradient(135deg, {t['brand_primary']}, {t['brand_secondary']});
                border-radius:16px;
                box-shadow: 0 8px 20px {t['shadow']};
            ">
                <i class="bi bi-mortarboard-fill" style="font-size:1.9rem; color:{t['text_bright']};"></i>
            </div>
            <h2 style='text-align:left; margin:0;'>ASD-CLASSROOMS</h2>
        </div>
                """, unsafe_allow_html=True)