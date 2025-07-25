import streamlit as st

st.title("Vowel Counter in a Word")

st.write("Enter a word to find out how many vowels it contains (a, e, i, o, u):")

# Input field for the word
word = st.text_input("Enter a word:")

# Set of vowels for comparison
vowels = set("aeiouAEIOU")

if word:
    # Count the number of vowels in the word
    count = sum(1 for char in word if char in vowels)
    st.success(f"The word '{word}' contains {count} vowel(s).")
else:
    st.info("Please enter a word to check for vowels.")
