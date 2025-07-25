import streamlit as st

st.title("Compare Two Numbers")

# Input fields for numbers
num1 = st.number_input("Enter the first number:", value=0.0, format="%.2f")
num2 = st.number_input("Enter the second number:", value=0.0, format="%.2f")

# Button to compare
if st.button("Compare"):
    if num1 > num2:
        st.success(f"The first number ({num1}) is **larger** than the second number ({num2}).")
    elif num1 < num2:
        st.warning(f"The first number ({num1}) is **smaller** than the second number ({num2}).")
    else:
        st.info("Both numbers are **equal**.")
