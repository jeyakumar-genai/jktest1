import streamlit as st

st.title("🎨 Personalized Message Generator")

# User input fields
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)
favorite_color = st.color_picker("Pick your favorite color:")

if st.button("Generate Message"):
    if name and age and favorite_color:
        st.markdown(
            f"<div style='padding:1em; border-radius:8px; background-color:{favorite_color}; color:white; font-size:1.2em;'>"
            f"Hello, <b>{name}</b>! At {age} years old, your favorite color is <b>{favorite_color}</b>. "
            "Have a wonderful and colorful day! 🌈"
            "</div>",
            unsafe_allow_html=True
        )
    else:
        st.warning("Please fill in all fields to generate your personalized message.")
