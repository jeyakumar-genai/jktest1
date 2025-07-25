import streamlit as st

st.title("Find the Largest Number in a List (Without max())")

st.write("Enter numbers separated by commas (e.g. 3, 7, 2, 9, 4)")

# Input string from user
numbers_input = st.text_input("Enter list of numbers:")

if numbers_input:
    try:
        # Convert input string to list of floats
        numbers = [float(num.strip()) for num in numbers_input.split(",")]
        
        if not numbers:
            st.warning("Please enter at least one number.")
        else:
            # Initialize largest_num as the first element
            largest_num = numbers[0]
            
            # Loop through numbers to find the largest
            for num in numbers[1:]:
                if num > largest_num:
                    largest_num = num
                    
            st.success(f"The largest number in the list is: {largest_num}")
    except ValueError:
        st.error("Please enter a valid list of numbers separated by commas.")
else:
    st.info("Please enter some numbers to find the largest.")
