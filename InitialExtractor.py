import streamlit as st

st.title("Extract Initials from Full Name")

# Input full name
full_name = st.text_input("Enter your full name:")

def get_initials(name):
    parts = name.strip().split()
    if not parts:
        return ""
    initials = [part[0].upper() + "." for part in parts if part]
    return " ".join(initials)

if full_name:
    initials = get_initials(full_name)
    st.success(f"Initials: {initials}")
else:
    st.info("Please enter your full name to extract initials.")
