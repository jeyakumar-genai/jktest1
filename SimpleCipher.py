import streamlit as st

st.title("Shift Letters by 1 Position in the Alphabet")

# Input word from user
word = st.text_input("Enter a word:")

def shift_letter(char):
    if char.isalpha():
        # Check if uppercase or lowercase
        if char.islower():
            # Shift within 'a' to 'z'
            return chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        else:
            # Shift within 'A' to 'Z'
            return chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
    else:
        # Non-alphabetical characters remain unchanged
        return char

if word:
    shifted_word = "".join(shift_letter(c) for c in word)
    st.success(f"Original word: {word}")
    st.success(f"Shifted word: {shifted_word}")
else:
    st.info("Please enter a word to shift its letters.")
