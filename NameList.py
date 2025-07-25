import streamlit as st

st.title("Names and Their Lengths")

# List of 5 names
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

st.write("Here are 5 names and their lengths:")

# Display each name with its length
for name in names:
    st.write(f"{name}: {len(name)} characters")
