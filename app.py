import streamlit as st
from datetime import datetime,timedelta
import time
from weather import show_weather
from sos import show_sos
from reminder import show_reminder
from gtts import gTTS
import io

from login import login

st.set_page_config(page_title="Senior Citizen Helper")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()
st.title("👴 Senior Citizen Helper App")

def pesu(text):
    try:
        tts = gTTS(text=text, lang='ta', slow=False)
        audio = io.BytesIO()
        tts.write_to_fp(audio)
        st.audio(audio, autoplay=True)
    except:
        st.write(text)

# --- Voice Assistant ---
st.subheader("🎤 Voice Assistant")
if st.button("🎙️ Sathama Kelu"):
    msg = "Vanakkam! Enna venum nu sollunga"
    st.success(msg + "...")
    pesu(msg)

if st.button("Clear"):
    st.rerun()

# --- Ready Messages ---
st.subheader("Ready Messages:")
if st.button("💧 Thanni Venum"):
    st.info("Thanni venum nu message anupiyachu!")
    pesu("Thanni venum nu message anupiyachu")

if st.button("💊 Marunthu Venum"):
    st.info("Marunthu venum nu message anupiyachu!")
    pesu("Marunthu venum nu message anupiyachu")

# --- Weather ---
st.divider()
show_reminder()
show_weather()
st.divider()
show_sos()

