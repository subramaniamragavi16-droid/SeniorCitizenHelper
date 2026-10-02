import streamlit as st
import speech_recognition as sr
import io
from datetime import datetime


def show_voice_assistant():

    st.subheader("🎤 Voice Assistant")

    audio = st.audio_input("🎙️ Speak Now")

    if audio is not None:

        recognizer = sr.Recognizer()

        try:
            audio_bytes = io.BytesIO(audio.getvalue())

            with sr.AudioFile(audio_bytes) as source:
                recorded_audio = recognizer.record(source)

            text = recognizer.recognize_google(recorded_audio).lower()

            st.success("You said: " + text)

            if "hello" in text:
                st.info("Hello! How can I help you?")

            elif "time" in text:
                current_time = datetime.now().strftime("%I:%M %p")
                st.info("Current Time: " + current_time)

            elif "date" in text:
                current_date = datetime.now().strftime("%d-%m-%Y")
                st.info("Today's Date: " + current_date)

            elif "medicine" in text or "marunthu" in text:
                st.info("💊 Medicine Reminder")

            elif "weather" in text:
                st.info("🌤️ Weather Report")

            elif "sos" in text or "emergency" in text:
                st.error("🚨 Emergency SOS Activated!")

            else:
                st.warning("Sorry, I don't understand that command.")

        except Exception as e:
            st.error("Could not understand your voice.")
