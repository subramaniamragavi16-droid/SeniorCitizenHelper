import streamlit as st

def login():

    st.title("🔐 Senior Citizen Helper Login")

    username = st.text_input("👤 Enter Username")
    password = st.text_input("🔑 Enter Password", type="password")

    if st.button("Login"):

        if username == "hello" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login Successful!")
            st.rerun()

        else:
            st.error("Invalid Username or Password!")
