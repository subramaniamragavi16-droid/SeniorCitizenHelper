import streamlit as st

st.set_page_config(page_title="Senior Citizen Helper", page_icon="👴")

st.title("👴 Senior Citizen Helper")
st.write("Periyavangalukku uthavum app")

menu = st.sidebar.selectbox("Enna venum?", 
    ["Emergency SOS", "Medicine Reminder", "Voice Assistant"])

if menu == "Emergency SOS":
    st.header("🚨 Emergency SOS")
    st.error("Emergency na button-a amukku!")
    if st.button("📞 SOS SEND", use_container_width=True):
        st.success("SOS Anuppiyachu!")
        st.balloons()
    st.write("Contact: 108")

elif menu == "Medicine Reminder":
    st.header("💊 Medicine Reminder")
    med = st.text_input("Medicine peru?")
    t = st.time_input("Time?")
    if st.button("Reminder Vaikku"):
        st.success(f"{med} ku {t} mani ku reminder!")

else:
    st.header("🎤 Voice Assistant")
    q = st.text_input("Enna help venum?")
    if q:
        st.success(f"Puriyuthu: {q}")
