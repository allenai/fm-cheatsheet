import pathlib

import streamlit as st
from bs4 import BeautifulSoup

from src.utils import get_environment


def add_goat_counter_tracker():
    script_id = "skiff-stats"
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"

    skiff_stats_script = f"""
        <script id={script_id} src="https://stats.allenai.org/init.min.js" data-spa="true" async></script>
    """

    if get_environment() == "prod":
        # This is an extreme workaround to be able to inject a script tag into the streamlit template.
        # Streamlit goes through well-meaning lengths to prevent this for security reasons.
        # So we are essentially altering the base streamlit index.html file.
        # inspired by: https://github.com/streamlit/streamlit/issues/969#issuecomment-1030832993
        soup = BeautifulSoup(index_path.read_text(), features="lxml")
        if not soup.find(id=script_id):  # if cannot find tag
            html = str(soup)
            # Insert the script directly in the head tag of the static template
            new_html = html.replace("</head>", skiff_stats_script + "</head>")
            index_path.write_text(new_html)
    else:
        # Search for and remove the Skiff Stats script if it is found.
        # This is mainly a tool for aiding development in case the prod ENV is being tested locally.
        soup = BeautifulSoup(index_path.read_text(), features="lxml")
        if soup.find(id=script_id):  # if find tag, remove it
            html = str(soup)
            new_html = html.replace(skiff_stats_script, "")
            index_path.write_text(new_html)
