import streamlit as st
from gtts import gTTS
import io
from datetime import datetime

st.set_page_config(page_title="Senior Citizen Helper", page_icon="👴")

st.title("👴 Senior Citizen Helper App")
st.write("Mudiyavargalukku uthavum app!")

# --- VOICE ASSISTANT ---
st.divider()
st.subheader("🎤 Voice Assistant")

q = st.text_input("Inga type pannu da, naan sathama pesuren:", placeholder="Edhavathu type pannu da...")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔊 Sathama Kelu"):
        if q:
            try:
                tts = gTTS(text=q, lang='ta')
                sound_file = io.BytesIO()
                tts.write_to_fp(sound_file)
                st.audio(sound_file, format='audio/mp3')
                st.success(f"🔊 Pesuthu: {q}")
            except Exception as e:
                tts = gTTS(text=q, lang='en')
                sound_file = io.BytesIO()
                tts.write_to_fp(sound_file)
                st.audio(sound_file, format='audio/mp3')
                st.success(f"🔊 Pesuthu: {q}")
        else:
            st.warning("Edhavathu type pannu da!")

with col2:
    if st.button("🧹 Clear"):
        st.info("Azhichachu!")

st.divider()
st.subheader("Ready Messages:")

if st.button("💧 Thanni Venum"):
    msg = "THANNI VENUM"
    tts = gTTS(text=msg, lang='en')
    sound_file = io.BytesIO()
    tts.write_to_fp(sound_file)
    st.audio(sound_file, format='audio/mp3')
    st.success(f"💧 {msg} - Sathama solliyachu!")

if st.button("💊 Marunthu Venum"):
    msg = "MARUNTHU VENUM"
    tts = gTTS(text=msg, lang='en')
    sound_file = io.BytesIO()
    tts.write_to_fp(sound_file)
    st.audio(sound_file, format='audio/mp3')
    st.success(f"💊 {msg} - Sathama solliyachu!")

if st.button("🆘 Udhavi Venum"):
    msg = "UDHAVI VENUM Emergency"
    tts = gTTS(text=msg, lang='en')
    sound_file = io.BytesIO()
    tts.write_to_fp(sound_file)
    st.audio(sound_file, format='audio/mp3')
    st.error(f"🆘 {msg}!")
