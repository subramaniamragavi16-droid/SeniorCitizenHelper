import streamlit as st
from datetime import datetime
import time

st.title("👴 Senior Citizen Helper - Mudhiyorkalukku Uthavum App")

# --- Voice Assistant ---
st.subheader("🎤 Voice Assistant")
if st.button("🔊 Sathama Kelu"):
    st.success("Vanakkam! Enna venum nu sollunga...")

if st.button("Clear"):
    st.rerun()

# --- Ready Messages ---
st.subheader("Ready Messages:")
if st.button("💧 Thanni Venum"):
    st.info("Thanni venum nu message anupiyachu!")

if st.button("💊 Marunthu Venum"):
    st.info("Marunthu venum nu message anupiyachu!")

if st.button("🆘 Udhavi Venum"):
    st.error("Udhavi venum nu SOS anupiyachu!")

st.divider()

# --- NEW: SOS EMERGENCY ---
st.subheader("🚨 SOS Emergency")
st.write("Avasara udhavikku keela button-a azhuthavum")
if st.button("🚨 SOS - Enakku Udhavi Venum!"):
    st.error("🚨 SOS Alert Sent to Family! Location Shared!")
    st.balloons()
    # Inga un family number ku WhatsApp/Call logic add pannalam

st.divider()

# --- NEW: MEDICINE REMINDER ---
st.subheader("💊 Medicine Reminder")
med_name = st.text_input("Marunthu Peyar:")
med_time = st.time_input("Maniku Reminder Venum?")

if st.button("⏰ Reminder Set Pannu"):
    if med_name:
        st.success(f"✅ {med_name} ku {med_time} mani ku reminder set panniyachu!")
        st.write(f"⏰ Time: {med_time}")
    else:
        st.warning("Marunthu peyar type pannu da!")
