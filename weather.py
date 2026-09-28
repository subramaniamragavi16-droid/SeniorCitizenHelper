import streamlit as st
import requests

def show_weather():
    st.subheader("🌤️ Weather Report")
    city = st.text_input("Enter City Name:", "Salem", key="weather_city")
    if st.button("Check Weather", key="weather_btn"):
        try:
            url = f"https://wttr.in/{city}?format=3"
            response = requests.get(url)
            st.success(response.text)
        except:
            st.error("City name thappu da!")