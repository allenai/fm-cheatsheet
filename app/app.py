import streamlit as st
import awesome_streamlit as ast

from src.components.goat_counter import add_goat_counter_tracker
from src.theme import theme
from src.pages import home, about

# You can define what pages you want to support here.
# They will show up as radio options on the sidebar
PAGES = {
    "Home": home,
    "About": about,
}

def main():
    st.set_page_config(
        # This title is the text that shows up in the browser tab.
        # Update with the name of your application
        page_title="Skiff Template",
        page_icon="https://allenai.org/favicon.ico",
        initial_sidebar_state="expanded",
    )
    # add analytics tracking
    add_goat_counter_tracker()
    # add custom AI2 branded CSS theme and header banner
    theme.add_theme()

    # This is the visible title of your site that can be
    # seen from the side bar
    st.sidebar.title("Skiff")

    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)

    # Please don't edit or remove the content of this footer as we'd like to include these important links on all AI2 applications
    theme.add_footer()

if __name__ == '__main__':
    main()
