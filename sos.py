import streamlit as st
from datetime import datetime

def show_sos():
    st.subheader("🆘 Emergency SOS")
    
    name1 = st.text_input("Family Member 1 Name:")
    phone1 = st.text_input("Phone Number 1:")
    name2 = st.text_input("Family Member 2 Name:")
    phone2 = st.text_input("Phone Number 2:")

    if st.button("🚨 SOS Alert Anuppu", type="primary", use_container_width=True):
        st.error("🚨 SOS Alert Sent!")
        st.write(f"Calling: {name1} - {phone1}")
        st.write(f"Calling: {name2} - {phone2}")
        st.balloons()
        st.success(f"Time: {datetime.now().strftime('%d-%m-%Y %I:%M %p')}")