import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout, icon
from src.utils.theme import get_theme, theme_toggle

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from PIL import Image
import numpy as np
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject
import time

from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card


def student_dashboard():
    t = get_theme()
    student_data = st.session_state.student_data
    student_id = student_data['student_id']

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.markdown(f"""
            <div style="display:flex; align-items:center; gap:12px;">
                <div style="
                    width:44px; height:44px; flex-shrink:0;
                    display:flex; align-items:center; justify-content:center;
                    border-radius:12px;
                    background: linear-gradient(135deg, {t['brand_primary']}, {t['brand_secondary']});
                ">
                    <i class="fa-solid fa-user-graduate" style="font-size:1.1rem; color:{t['text_bright']};"></i>
                </div>
                <div>
                    <p style="margin:0; font-size:0.78rem; color:{t['brand_primary']}; font-weight:600;">STUDENT</p>
                    <h3 style="margin:0;">Welcome, {student_data['name']}</h3>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Logout", type='secondary', key='loginbackbtn', icon=':material/logout:',
                     shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data
            st.rerun()

    theme_toggle()
    st.space()

    c1, c2 = st.columns(2)
    with c1:
        st.header('Your Enrolled Subjects')
    with c2:
        if st.button('Enroll in Subject', type='primary', icon=':material/add_circle:', width='stretch'):
            enroll_dialog()

    st.divider()

    with st.spinner('Loading your enrolled subjects..'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}

    for log in logs:
        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}

        stats_map[sid]['total'] += 1

        if log.get('is_present'):
            stats_map[sid]['attended'] += 1

    if not subjects:
        with st.container(border=True):
            st.markdown(f"""
                <div style="text-align:center; padding:2rem 1rem;">
                    <i class="fa-solid fa-book-open" style="font-size:2.4rem; color:{t['brand_primary']}; opacity:0.6;"></i>
                    <h3 style="margin-top:1rem;">No subjects enrolled yet</h3>
                    <p>Tap "Enroll in Subject" above to get started.</p>
                </div>
            """, unsafe_allow_html=True)

    cols = st.columns(2)
    for i, sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid = sub['subject_id']

        stats = stats_map.get(sid, {"total": 0, "attended": 0})

        def unenroll_button(sid=sid, sub=sub):
            if st.button("Unenroll from this course", type='tertiary', width='stretch',
                         icon=':material/delete_forever:'):
                unenroll_student_to_subject(student_id, sid)
                st.toast(f"Unenrolled from {sub['name']} successfully!")
                st.rerun()

        with cols[i % 2]:
            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=[
                    ('📅', 'Total', stats['total']),
                    ('✅', 'Attended', stats['attended']),
                ],
                footer_callback=unenroll_button
            )
    footer_dashboard()


def student_screen():
    t = get_theme()

    st.markdown(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">',
        unsafe_allow_html=True
    )

    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn',
                     icon=':material/arrow_back:', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    theme_toggle()

    with st.container(border=True):
        st.markdown(f"""
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:4px;">
                <div style="
                    width:48px; height:48px; flex-shrink:0;
                    display:flex; align-items:center; justify-content:center;
                    border-radius:14px;
                    background: linear-gradient(135deg, {t['brand_primary']}, {t['brand_secondary']});
                ">
                    <i class="fa-solid fa-face-viewfinder" style="font-size:1.3rem; color:{t['text_bright']};"></i>
                </div>
                <h2 style="margin:0;">Login using FaceID</h2>
            </div>
            <p style="margin-top:0;">Look at the camera and hold still for a moment.</p>
        """, unsafe_allow_html=True)

        show_registration = False
        photo_source = st.camera_input("Position your face in the center")

        if photo_source:
            img = np.array(Image.open(photo_source))

            with st.spinner('AI is scanning..'):
                detected, all_ids, num_faces = predict_attendance(img)

                if num_faces == 0:
                    st.warning('Face not found!')
                elif num_faces > 1:
                    st.warning('Multiple faces found')
                else:
                    if detected:
                        student_id = list(detected.keys())[0]
                        all_students = get_all_students()
                        student = next((s for s in all_students if s['student_id'] == student_id), None)

                        if student:
                            st.session_state.is_logged_in = True
                            st.session_state.user_role = 'student'
                            st.session_state.student_data = student
                            st.toast(f"Welcome Back {student['name']}")
                            time.sleep(1)
                            st.rerun()
                    else:
                        st.info('Face not recognized! You might be a new student!')
                        show_registration = True

    if show_registration:
        with st.container(border=True):
            st.markdown(f"""
                <div style="display:flex; align-items:center; gap:12px; margin-bottom:4px;">
                    <div style="
                        width:44px; height:44px; flex-shrink:0;
                        display:flex; align-items:center; justify-content:center;
                        border-radius:12px;
                        background: linear-gradient(135deg, {t['brand_primary']}, {t['brand_secondary']});
                    ">
                        <i class="fa-solid fa-id-card-clip" style="font-size:1.1rem; color:{t['text_bright']};"></i>
                    </div>
                    <h2 style="margin:0;">Register New Profile</h2>
                </div>
            """, unsafe_allow_html=True)

            new_name = st.text_input("Enter your name", placeholder='Abhishek Singh Dasila')

            st.markdown(f"""
                <div style="display:flex; align-items:center; gap:8px; margin-top:1rem;">
                    <i class="fa-solid fa-microphone" style="color:{t['brand_primary']};"></i>
                    <h3 style="margin:0;">Optional: Voice Enrollment</h3>
                </div>
            """, unsafe_allow_html=True)
            st.info("Enroll your voice for voice-only attendance")

            audio_data = None

            try:
                audio_data = st.audio_input('Record a short phrase like "I am present, my name is Abhishek."')
            except Exception:
                st.error('Audio Data failed!')

            if st.button('Create Account', type='primary', icon=':material/how_to_reg:'):
                if new_name:
                    with st.spinner('Creating profile..'):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f'Profile Created! Hi {new_name}!')
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error("Couldn't capture your facial features for registration")

                else:
                    st.warning('Please enter your name!')

    footer_dashboard()