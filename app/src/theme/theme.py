import os
from os import path

import streamlit as st
from src.utils import get_environment

__location__ = path.realpath(path.join(os.getcwd(), path.dirname(__file__)))


def add_theme():
    with open(os.path.join(__location__, "style.css")) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    # hide the streamlit menu if prod
    if get_environment() != "dev":
        st.markdown(
            """
        <style>
            #MainMenu {
                visibility: hidden;
            }
        </style>
        """,
            unsafe_allow_html=True,
        )
    # add the AI2 banner
    add_header()


def add_header():
    st.write(
        '<div class="header" role="heading"><a href="https://allenai.org"> '
        '<img src="https://cdn.jsdelivr.net/npm/@allenai/varnish@3.0.7/shellac/ai2.svg"'
        ' alt="Allen Institute for AI"> </a></div>',
        unsafe_allow_html=True,
    )


def add_footer():
    """
    Please don't edit or remove this footer as we'd like to include these important links on all AI2 applications
    """
    st.write(
        "© [Allen Institute for AI](https://allenai.org/) All Rights Reserved | "
        "[Privacy Policy](https://allenai.org/privacy-policy) | "
        "[Terms of Use](https://allenai.org/terms) | "
        "[Business Code of Conduct](https://allenai.org/business-code-of-conduct)"
    )
