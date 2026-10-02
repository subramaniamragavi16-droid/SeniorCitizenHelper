import streamlit as st
import speech_recognition as sr
import io
from datetime import datetime
from gtts import gTTS


def speak(text):
    try:
        audio = io.BytesIO()
        tts = gTTS(text=text, lang="en")
        tts.write_to_fp(audio)
        st.audio(audio.getvalue(), format="audio/mp3", autoplay=True)
    except:
        st.write(text)


def show_voice_assistant():

    st.subheader("🎤 Voice Assistant")

    audio = st.audio_input("🎙️ Speak Now")

    if audio is not None:

        recognizer = sr.Recognizer()

        try:
            audio_bytes = io.BytesIO(audio.getvalue())

            with sr.AudioFile(audio_bytes) as source:
                recorded_audio = recognizer.record(source)

            text = recognizer.recognize_google(
                recorded_audio,
                language="en-IN"
            ).lower()

            st.success("You said: " + text)

            # HELLO
            if "hello" in text or "hi" in text:
                reply = "Hello! How can I help you?"

            # TIME
            elif "time" in text:
                current_time = datetime.now().strftime("%I:%M %p")
                reply = "The current time is " + current_time

            # DATE
            elif "date" in text:
                current_date = datetime.now().strftime("%d %B %Y")
                reply = "Today's date is " + current_date

            # MEDICINE
            elif "medicine" in text or "marunthu" in text:
                reply = "Opening medicine reminder."

            # WEATHER
            elif "weather" in text:
                reply = "Opening weather report."

            # SOS
            elif "sos" in text or "emergency" in text:
                reply = "Emergency SOS activated. Please contact your family member."

            # EXIT
            elif "exit" in text or "bye" in text:
                reply = "Goodbye! Take care."

            # UNKNOWN
            else:
                reply = "Sorry, I don't understand your command."

            st.info("🔊 " + reply)
            speak(reply)

        except Exception:
            reply = "Sorry, I could not understand your voice."
            st.error(reply)
            speak(reply)
