import streamlit as st

st.title("Count Positive, Negative, and Zero Numbers")

st.write("Enter numbers separated by commas (e.g. 1, -2, 0, 4, -5)")

# Get input string from the user
numbers_input = st.text_input("Enter list of numbers:")

if numbers_input:
    try:
        # Convert the input string into a list of floats
        numbers = [float(num.strip()) for num in numbers_input.split(",")]
        
        # Count positive, negative, and zero numbers
        positive_count = sum(1 for n in numbers if n > 0)
        negative_count = sum(1 for n in numbers if n < 0)
        zero_count = sum(1 for n in numbers if n == 0)
        
        # Display the counts
        st.success(f"Positive numbers: {positive_count}")
        st.warning(f"Negative numbers: {negative_count}")
        st.info(f"Zeroes: {zero_count}")
    
    except ValueError:
        st.error("Please enter a valid list of numbers separated by commas.")
else:
    st.info("Please enter some numbers to analyze.")
