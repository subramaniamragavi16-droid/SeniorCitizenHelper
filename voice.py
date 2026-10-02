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

    st.write("### 🎙️ Available Voice Commands")

    st.write("👋 Hello / Hi")
    st.write("🕐 Time")
    st.write("📅 Date")
    st.write("💊 Medicine / Marunthu")
    st.write("🌤️ Weather")
    st.write("🚨 SOS / Emergency")
    st.write("🆘 Help")
    st.write("👋 Exit / Bye")
    st.write("💧 Water / Thanni")
    st.write("🍚 Food / Saapadu")
    st.write("📞 Call Family")
    st.write("📅 Appointment")

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
            if "hello" in text or "hi" in text or "vanakkam" in text:
                reply = "Hello! How can I help you?"

            # TIME
            elif "time" in text or "neram" in text:
                current_time = datetime.now().strftime("%I:%M %p")
                reply = "The current time is " + current_time

            # DATE
            elif "date" in text:
                current_date = datetime.now().strftime("%d %B %Y")
                reply = "Today's date is " + current_date

            # MEDICINE
            elif "medicine" in text or "marunthu" in text:
                reply = "Medicine reminder is ready."

            # WEATHER
            elif "weather" in text:
                reply = "Weather information is ready."

            # SOS
            elif "sos" in text or "emergency" in text:
                reply = "Emergency SOS activated. Please contact your family member."

            # HELP
            elif "help" in text:
                reply = "I am here to help you. You can ask for medicine, weather, time, date or emergency help."

            # WATER
            elif "water" in text or "thanni" in text:
                reply = "Water request has been noted."

            # FOOD
            elif "food" in text or "saapadu" in text:
                reply = "Food request has been noted."

            # FAMILY
            elif "call family" in text or "family" in text:
                reply = "Family call request has been noted."

            # APPOINTMENT
            elif "appointment" in text:
                reply = "Your appointment reminder is ready."

            # EXIT
            elif "exit" in text or "bye" in text:
                reply = "Goodbye! Take care."

            # UNKNOWN
            else:
                reply = "Sorry, I don't understand that command."

            st.info("🔊 " + reply)

            speak(reply)

        except Exception:
            reply = "Sorry, I could not understand your voice."
            st.error(reply)
            speak(reply)
