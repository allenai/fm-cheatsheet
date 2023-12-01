import streamlit as st
from ..api.api import solve

def write():
    """Used to write the page in the app.py file"""
    st.write("Enter a question and answers below to see what answer our application selects.")
    question = st.text_input('* Question:', 'Enter a question')
    answers = st.multiselect('* Answers:',
    ['Grapefruit', 'Lemon', 'Lime', 'Orange'])
    if st.button('Submit'):
        try:
            result = solve(question, answers)
            answer = result.get('answer', '')
            score = result.get('score', 0)
            st.info(f"Our system answered: {answer} ({score}%)")
        except ValueError as err:
            st.error(err)
            