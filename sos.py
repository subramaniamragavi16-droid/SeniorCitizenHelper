import streamlit as st
from datetime import datetime


def show_sos():
    st.subheader("🆘 Emergency SOS")

    name1 = st.text_input("Family Member 1 Name:")
    phone1 = st.text_input("Phone Number 1:")

    name2 = st.text_input("Family Member 2 Name:")
    phone2 = st.text_input("Phone Number 2:")

    if st.button("🚨 SOS Alert", type="primary", use_container_width=True):

        # Emergency Alert
        st.error("🚨 EMERGENCY SOS ACTIVATED!")

        # Balloons
        st.balloons()

        # Family Member 1
        if name1 and phone1:
            st.markdown(
                f"👤 **{name1}** - "
                f"[📞 Call {phone1}](tel:{phone1})"
            )

        # Family Member 2
        if name2 and phone2:
            st.markdown(
                f"👤 **{name2}** - "
                f"[📞 Call {phone2}](tel:{phone2})"
            )

        # Time
        current_time = datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )

        st.success(
            f"⏰ SOS Activated Time: {current_time}"
        )

        st.warning(
            "🚨 Please contact the family member immediately."
        )