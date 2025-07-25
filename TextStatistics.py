import streamlit as st
import re

st.title("Count Words, Sentences, and Characters in a Paragraph")

# Input paragraph from user
paragraph = st.text_area("Enter a paragraph:")

if paragraph:
    # Count characters (including spaces)
    char_count = len(paragraph)

    # Count words (split by whitespace)
    words = paragraph.split()
    word_count = len(words)

    # Count sentences (split by '.', '?', '!')
    # Using regex to split on sentence-ending punctuation followed by space or end of string
    sentences = re.split(r'[.!?]+(?:\s|$)', paragraph.strip())
    # Filter out empty strings that may occur from splitting
    sentences = [s for s in sentences if s]
    sentence_count = len(sentences)

    st.success(f"Characters (including spaces): {char_count}")
    st.success(f"Words: {word_count}")
    st.success(f"Sentences: {sentence_count}")
else:
    st.info("Please enter a paragraph to analyze.")
