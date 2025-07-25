import streamlit as st

st.title("Test Scores Average - Pass/Fail Checker")

# Input fields for 5 test scores
score1 = st.number_input("Enter score 1:", min_value=0.0, max_value=100.0, value=0.0)
score2 = st.number_input("Enter score 2:", min_value=0.0, max_value=100.0, value=0.0)
score3 = st.number_input("Enter score 3:", min_value=0.0, max_value=100.0, value=0.0)
score4 = st.number_input("Enter score 4:", min_value=0.0, max_value=100.0, value=0.0)
score5 = st.number_input("Enter score 5:", min_value=0.0, max_value=100.0, value=0.0)

PASS_MARK = 40  # You can change the pass mark as needed

if st.button("Calculate Average and Result"):
    scores = [score1, score2, score3, score4, score5]
    average = sum(scores) / len(scores)
    st.write(f"Average score: {average:.2f}")

    if average >= PASS_MARK:
        st.success("Result: Pass")
    else:
        st.error("Result: Fail")
