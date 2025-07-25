import streamlit as st

def check_even_odd(number):
    return "even" if number % 2 == 0 else "odd"

st.title("Even or Odd Checker")

# Check a single number
num = st.number_input("Enter a number:", step=1)

if st.button("Check Single Number"):
    st.write(f"The number {num} is {check_even_odd(num)}.")

# Check a list of numbers
numbers_list = [10, 15, 22, 33, 40, 55]
if st.button("Check Predefined List"):
    results = {n: check_even_odd(n) for n in numbers_list}
    for key, val in results.items():
        st.write(f"{key} is {val}")
