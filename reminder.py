import streamlit as st
from datetime import datetime, timedelta
import time

def show_reminder():
    st.subheader("💊 Medicine Reminder")
    
    medicine = st.text_input("Medicine Name Enter Pannunga:", "Vitamin")
    reminder_time = st.time_input("Reminder Time:")
    
    if st.button("⏰ Reminder Set Pannu"):
        st.session_state['rem_time'] = reminder_time.strftime("%H:%M")
        st.session_state['medicine'] = medicine
        st.success(f"Reminder Set! {reminder_time.strftime('%I:%M %p')} ku {medicine} - IST")

    # Check time - IST
    if 'rem_time' in st.session_state:
        ist_now = datetime.utcnow() + timedelta(hours=5, minutes=30)
        current = ist_now.strftime("%H:%M")
        if current == st.session_state['rem_time']:
            st.error(f"💊 Time to take medicine! Medicine: {st.session_state['medicine']}")
            st.balloons()
            # Speak in Tamil
            try:
                from gtts import gTTS
                import io
                tts = gTTS(text=f"Marunthu eduthukka neram vandhachu, {st.session_state['medicine']}", lang='ta')
                audio = io.BytesIO()
                tts.write_to_fp(audio)
                st.audio(audio, autoplay=True)
            except:
                pass
        st.info(f"Current Time: {ist_now.strftime('%I:%M %p')} (IST)")
    else:
        ist_now = datetime.utcnow() + timedelta(hours=5, minutes=30)
        st.info(f"Current Time: {ist_now.strftime('%I:%M %p')} (IST)")