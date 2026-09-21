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
        st.success("Family ku SOS Anuppiyachu!")
        st.balloons()
    st.write("Emergency Contact: 108")
    st.write("Family: +91 98XXXXXX10")

elif menu == "Medicine Reminder":
    st.header("💊 Medicine Reminder")
    med = st.text_input("Medicine peru? Ex: BP tablet")
    t = st.time_input("Time?")
    if st.button("Reminder Vaikku"):
        if med:
            st.success(f"✅ {med} ku {t} mani ku reminder set aayiduchu!")
        else:
            st.warning("Medicine peru type pannu da!")

else:
    st.header("🎤 Voice Assistant")
    st.write("Type pannina sathama pesum!")
    
    q = st.text_area("Enna venum nu type pannunga:", placeholder="Ex: Enakku thanni venum")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔊 Sathama Kelu"):
            if q:
                st.success(f"🔊 Pesuthu: {q}")
                st.markdown(f"<p style='font-size:30px'>🗣️ {q}</p>", unsafe_allow_html=True)
            else:
                st.warning("Edhavathu type pannu da!")
    
    with col2:
        if st.button("📝 Clear"):
            st.info("Azhichachu!")
            
    st.divider()
    st.subheader("Ready Messages:")
    if st.button("💧 Thanni Venum"):
        st.success("🗣️ THANNi VENUM! - Sathama solliyachu!")
    if st.button("💊 Marunthu Venum"):
        st.success("🗣️ MARUNTHU VENUM! - Sathama solliyachu!")
    if st.button("🚑 Udhavi Venum"):
        st.error("🗣️ UDHAVI VENUM! Emergency!")
