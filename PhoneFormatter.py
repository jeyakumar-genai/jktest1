import streamlit as st

st.title("Format 10-Digit Number as (XXX) XXX-XXXX")

# Input field for the 10-digit number as a string (to keep leading zeros if any)
phone_input = st.text_input("Enter a 10-digit phone number (digits only):")

def format_phone_number(number):
    # Format as (XXX) XXX-XXXX
    return f"({number[0:3]}) {number[3:6]}-{number[6:10]}"

if phone_input:
    # Remove spaces or special characters if user enters any by mistake
    digits_only = ''.join(filter(str.isdigit, phone_input))
    
    if len(digits_only) == 10:
        formatted_number = format_phone_number(digits_only)
        st.success(f"Formatted Number: {formatted_number}")
    else:
        st.error("Please enter exactly 10 digits.")
else:
    st.info("Enter a 10-digit number to see it formatted.")
