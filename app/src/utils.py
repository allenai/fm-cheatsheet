import os

def get_environment():
    return os.getenv('STREAMLIT_ENV', 'dev')