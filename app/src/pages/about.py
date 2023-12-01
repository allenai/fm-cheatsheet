import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Ahoy!")

    st.markdown("""
    This is a fresh application derived from the Skiff Streamlit Template. Skiff provides an AI2 styled Streamlit instance.

    It's deployed to a Google managed Kubernetes cluster and provides DNS, log aggregation, TLS and other capabilities out of the box, thanks to the Skiff project.

    If you have any questions, concerns or feedback please don't hesitate to reach out. You can open a Github Issue or contact us at reviz@allenai.org.

    Smooth sailing!
    """)

    st.image('https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80', 'A rustic wooden boat on a mountain lake')