import streamlit as st

st.title("Full Name Formatter")

st.write("Enter your full name (First [Middle] Last):")

# Input full name
full_name = st.text_input("Full Name:")

def format_name(name):
    parts = name.strip().split()
    n = len(parts)
    if n == 0:
        return {}
    elif n == 1:
        return {
            "Single Name": parts[0]
        }
    elif n == 2:
        first, last = parts
        return {
            "First Last": f"{first} {last}",
            "Last, First": f"{last}, {first}",
            "Last First": f"{last} {first}",
        }
    else:
        first = parts[0]
        last = parts[-1]
        middle = " ".join(parts[1:-1])
        return {
            "First Middle Last": f"{first} {middle} {last}",
            "Last, First Middle": f"{last}, {first} {middle}",
            "Last First Middle": f"{last} {first} {middle}",
        }

if full_name:
    formatted = format_name(full_name)
    for fmt, val in formatted.items():
        st.write(f"**{fmt}:** {val}")
else:
    st.info("Please enter your full name to see different formats.")
