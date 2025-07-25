import streamlit as st

st.title("Extract Username from Email Address")

# Input field for email address
email = st.text_input("Enter an email address:")

def extract_username(email_address):
    if "@" in email_address:
        return email_address.split("@")[0]
    else:
        return None

if email:
    username = extract_username(email)
    if username:
        st.success(f"Username extracted: {username}")
    else:
        st.error("Invalid email address. Please include an '@' symbol.")
else:
    st.info("Please enter an email address to extract the username.")
