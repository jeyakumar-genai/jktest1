import streamlit as st

st.title("Password Strength Checker")

# Define the minimum length requirement
MIN_PASSWORD_LENGTH = 8

# Input field for the password (hidden input)
password = st.text_input("Enter your password:", type="password")

if password:
    if len(password) >= MIN_PASSWORD_LENGTH:
        st.success(f"Password is valid. Length: {len(password)} characters.")
    else:
        st.error(f"Password is too short. Must be at least {MIN_PASSWORD_LENGTH} characters.")
else:
    st.info("Please enter a password to check.")
