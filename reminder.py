import streamlit as st
from datetime import datetime
import time

def show_reminder():
    st.subheader("💊 Medicine Reminder")
    
    medicine = st.text_input("Medicine Name Enter Pannunga:", "Vitamin")
    reminder_time = st.time_input("Reminder Time:")
    
    if st.button("⏰ Reminder Set Pannu"):
        st.session_state['rem_time'] = reminder_time.strftime("%H:%M")
        st.session_state['medicine'] = medicine
        st.success(f"Reminder Set! {reminder_time.strftime('%H:%M')} ku {medicine}")

    # Check time
    if 'rem_time' in st.session_state:
        current = datetime.now().strftime("%H:%M")
        if current == st.session_state['rem_time']:
            st.error(f"💊 Time to take medicine! Medicine: {st.session_state['medicine']}")
            st.balloons()
            # Speak
            try:
                from gtts import gTTS
                import io
                tts = gTTS(text=f"Marunthu eduthukka neram vandhachu, {st.session_state['medicine']}", lang='ta')
                audio = io.BytesIO()
                tts.write_to_fp(audio)
                st.audio(audio, autoplay=True)
            except:
                pass
    
    st.info(f"Current Time: {datetime.now().strftime('%I:%M %p')}")