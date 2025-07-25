import streamlit as st

st.title("Sum of Numbers from 1 to n")

# Input: Get n from user, default to 1
n = st.number_input("Enter a positive integer n:", min_value=1, step=1, value=1)

# Button to trigger calculation
if st.button("Calculate Sum"):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    st.success(f"The sum of all numbers from 1 to {n} is {total_sum}.")
