import streamlit as st
import pandas as pd
from pathlib import Path

# Set page config
st.set_page_config(page_title="Smart Wireless Earbuds ", layout="wide")

# =============================================
# BACKGROUND VIDEO SECTION
# =============================================

# Video HTML/CSS (place at the beginning to load first)
video_html = """
<style>
#background-video 
{
    position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%; 
    min-height: 100%;
    width: auto;
    height: auto;
    z-index: -100;
    background-size: cover;
    opacity: 0.3;  /* Adjust transparency */
}

.content {
    position: relative;
    z-index: 1;
    background-color: rgba(0,0,0,0.7);  /* Semi-transparent overlay */
    padding: 2rem;
    border-radius: 10px;
}
</style>

<video autoplay muted loop id="background-video">
    <source src="ear.mp4" type="video/mp4">
</video>
"""

st.markdown(video_html, unsafe_allow_html=True)
# =============================================

# Main content wrapped in a div with our content class
st.markdown('<div class="content">', unsafe_allow_html=True)

# Dashboard Title
st.title("🎧 Smart Wireless Earbuds Specifications Dashboard")
st.write("Collect and analyze specifications and features of smart wireless earbuds.")
st.markdown("---")

# =============================================
# YOUR EXISTING DASHBOARD CODE
# =============================================
# Data Collection Section


import requests
import streamlit as st

def submit_to_google_sheets(data):
    url = "https://script.google.com/macros/s/AKfycby37I3RHtLusxmUN5s0NDXPnlzJhl0JrVMvUtsS_JthCbfbvGwhLxGfPHqq1-_ZPPYMxQ/exec"  # Replace with your Web App URL
    response = requests.post(url, json=data)
    return response

# Example UI
st.title("Smart Wireless Earbuds")

connectivity = st.selectbox("Connectivity Technology", ["Wireless", "Wired"])
communication = st.selectbox("Wireless Communication Technology", ["Bluetooth", "NFC"])
charging_time = st.number_input("Charging Time (Minutes)", min_value=0)
water_resistant = st.selectbox("Water Resistance Level", ["Water Resistant", "Not Water Resistant"])
controller = st.text_input("Controller Type")
battery_life = st.number_input("Battery Life (Hours)", min_value=0)
bluetooth_range = st.number_input("Bluetooth Range (Metres)", min_value=0)
audio_latency = st.number_input("Audio Latency (Milliseconds)", min_value=0)
driver_size = st.slider("Audio Driver Size (Millimetres)", 0, 20, 12)
noise_cancellation = st.selectbox("Noise Cancellation", ["Yes", "No"])
country = st.text_input("Country of Origin", "India")

if st.button("Submit Specifications"):
    data = {
        "connectivity": connectivity,
        "communication": communication,
        "charging_time": charging_time,
        "water_resistant": water_resistant,
        "controller": controller,
        "battery_life": battery_life,
        "bluetooth_range": bluetooth_range,
        "audio_latency": audio_latency,
        "driver_size": driver_size,
        "noise_cancellation": noise_cancellation,
        "country": country
    }

    res = submit_to_google_sheets(data)
    if res.status_code == 200:
        st.success("✅ Specifications submitted and saved to Google Sheets!")
    else:
        st.error("❌ Failed to submit data.")
