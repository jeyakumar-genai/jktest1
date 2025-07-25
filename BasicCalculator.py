import streamlit as st

st.title("🧮 Simple Calculator")

# Input two numbers
num1 = st.number_input("Enter first number:", format="%f")
num2 = st.number_input("Enter second number:", format="%f")

# Select operation
operation = st.selectbox("Choose an operation:", ["Add (+)", "Subtract (-)", "Multiply (*)", "Divide (/)"])

if st.button("Calculate"):
    try:
        if operation == "Add (+)":
            result = num1 + num2
        elif operation == "Subtract (-)":
            result = num1 - num2
        elif operation == "Multiply (*)":
            result = num1 * num2
        elif operation == "Divide (/)":
            if num2 == 0:
                st.error("Error: Division by zero is not allowed.")
                result = None
            else:
                result = num1 / num2
        else:
            result = None

        if result is not None:
            st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
