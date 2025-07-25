import streamlit as st

st.title("Reverse Individual Words in a Sentence")

# Input sentence from the user
sentence = st.text_input("Enter a sentence:")

if sentence:
    # Split the sentence into words
    words = sentence.split()
    # Reverse each word individually
    reversed_words = [word[::-1] for word in words]
    # Join back to a sentence
    reversed_sentence = " ".join(reversed_words)

    st.success("Sentence with reversed words:")
    st.write(reversed_sentence)
else:
    st.info("Please enter a sentence to see the words reversed.")
