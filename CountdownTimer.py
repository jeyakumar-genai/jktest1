import streamlit as st
import time

st.title("Countdown from 10 to 0")

countdown = 10

# Placeholder to update countdown text
counter_text = st.empty()

for i in range(countdown, -1, -1):
    counter_text.markdown(f"### {i}")
    time.sleep(1)
    
st.success("Countdown finished!")
