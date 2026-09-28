import streamlit as st
import requests

def show_weather():
    st.subheader("🌤️ Weather Report")
    
    city = st.text_input("Enter City Name:", "Salem")
    
    if st.button("Check Weather"):
        try:
            url = f"https://wttr.in/{city}?format=3"
            response = requests.get(url)
            st.success(response.text)
            
            # Extra info
            url2 = f"https://wttr.in/{city}?format=%C+%t+%w+%h"
            response2 = requests.get(url2)
            st.info(f"Details: {response2.text}")
            
        except:
            st.error("Weather kidaikala da, city name check pannu!")

# Streamlit ku direct call
show_weather()