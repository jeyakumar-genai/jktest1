import streamlit as st

def categorize_age(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 64:
        return "Adult"
    else:
        return "Senior"

st.title("Age Category Classifier")

age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)

if st.button("Classify"):
    category = categorize_age(age)
    if category == "Invalid age":
        st.error("Please enter a valid non-negative age.")
    else:
        st.success(f"At age {age}, you are classified as: **{category}**.")
