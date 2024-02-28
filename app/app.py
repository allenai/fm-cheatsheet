import datetime as dt
import itertools

import pandas as pd
import streamlit as st
from PIL import Image

from src.api.api import filter_resources
from src.components.goat_counter import add_goat_counter_tracker
from src.constants import BASE_DIR, ORDERED_SECTION_HEADERS
from src.theme import theme
from src.utils import create_markdown_img, load_data, load_logos

pd.options.display.html.border = 0


def write_resource(row, logos: dict) -> None:
    col1, col2, col3, col4 = st.columns([0.4, 1, 5, 1], gap="small")

    modality_icons = []
    for mod_img, modality in [
        (logos["text"], "Text"),
        (logos["vision"], "Vision"),
        (logos["speech"], "Speech"),
    ]:
        mod_icon = (
            create_markdown_img(mod_img, None, 20)
            if modality in row["Modalities"]
            else "  "
        )
        modality_icons.append(mod_icon)
    col1.markdown(" ".join(modality_icons), unsafe_allow_html=True)

    col2.write(row["Name"])
    col3.write(row["Description"])

    logo_links = []
    for logo_img, col in [
        (logos["arxiv"], "Paper Link"),
        (logos["hf"], "HuggingFace Link"),
        (logos["github"], "GitHub Link"),
        (logos["web"], "Website Link"),
    ]:
        logo_link = (
            create_markdown_img(logo_img, row[col], dim=20) if row[col] else "  "
        )  # "<div style='width: 30px; height: auto;'></div>"
        logo_links.append(logo_link)
        # col4.markdown(logo_link, unsafe_allow_html=True)
    col4.markdown(" ".join(logo_links), unsafe_allow_html=True)


def streamlit_app():
    st.set_page_config(
        page_title="Foundation Model Development Cheatsheet", layout="wide"
    )  # , initial_sidebar_state='collapsed')

    RESOURCES = load_data()
    LOGOS = load_logos()

    # add analytics tracking
    add_goat_counter_tracker()
    # add custom AI2 branded CSS theme and header banner
    theme.add_theme()

    st.markdown(
        "<p id='logo' style='text-align: center'>"
        + create_markdown_img(LOGOS["cheatsheet"], "/", 200)
        + "</p>",
        unsafe_allow_html=True,
    )

    # st.title("Foundation Model Development Cheatsheet")
    st.markdown(
        "<h1 style='text-align: center'>Foundation Model Development Cheatsheet</h1>",
        unsafe_allow_html=True,
    )

    st.caption(
        "Resources and recommendations for best practices in developing and releasing models."
    )
    st.markdown(
        """
        This cheatsheet serves as a succinct guide, prepared *by* foundation model developers *for* foundation model developers.
        As the field of AI foundation model development rapidly expands, welcoming new contributors, scientists, and
        applications, we hope to lower the barrier for new community members to become familiar with the variety of
        resources, tools, and findings. The focus of this cheatsheet is not only, or even primarily, to support building,
        but to inculcate good practices, awareness of limitations, and general responsible habits as community norms.

        To add to the cheatsheet please see [Contribute Resources](https://github.com/allenai/fm-cheatsheet?tab=readme-ov-file#add-to-cheatsheet)."""
    )
    scope_limitations_text = """
        We've compiled resources, tools, and papers that have helped guide our own intuitions around model development,
        and which we believe will be especially helpful to nascent (and sometimes even experienced) developers in the field.
        However, this guide is far from exhaustive---and here's what to consider when using it:

        * We scope these resources to newer foundation model developers, usually releasing models to the community.
        Larger organizations, with commercial services, have even broader considerations for responsible development and release.

        * Foundation model development is a rapidly evolving science. **To keep this cheatsheet up-to-date, we are open to
        public [contributions](https://github.com/allenai/fm-cheatsheet?tab=readme-ov-file#add-to-cheatsheet)**.

        * We've scoped our content modalities only to **text, vision, and speech**.

        * A cheatsheet **cannot be comprehensive**.
        We prioritize resources we have found helpful, and rely heavily on survey papers and repositories to point out the
        many other awesome works which deserve consideration, especially for developers who plan to dive deeper into a topic.

        * **We cannot take responsibility for these resources---onus is on the reader to assess their viability, particularly for
        their circumstance.** At times we have provided resources with conflicting advice, as it is helpful to be aware of
        divided community perspectives. Our notes throughout are designed to contextualize these resources, to help guide
        the readers judgement.
    """
    with st.expander("Scope & Limitations"):
        st.markdown(scope_limitations_text)
    col1a, col1b, col1c = st.columns([0.3, 0.3, 0.4], gap="small")
    # TODO: Replace button links.
    with col1a:
        st.link_button(
            "FM Dev Cheatsheet Paper",
            "https://github.com/allenai/fm-cheatsheet/app/resources/paper.pdf",
            type="primary",
        )
    with col1b:
        st.link_button(
            "Contribute Resources!",
            "https://github.com/allenai/fm-cheatsheet?tab=readme-ov-file#add-to-cheatsheet",
            type="primary",
        )

    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown(
        "<p id='maker' style='text-align: center'>Assembled by open model developers from AI2, EleutherAI, Google, Hugging Face, Masakhane, McGill, MIT, MLCommons, Princeton, Stanford CRFM, UCSB, and UW.</p>",
        unsafe_allow_html=True,
    )
    st.image("resources/orgs.png", use_column_width=True)
    st.markdown("<br/>", unsafe_allow_html=True)

    #### FILTER MENU STARTS HERE

    with st.form("data_selection"):

        category_select = st.multiselect(
            label="Resource Categories:",
            options=list(ORDERED_SECTION_HEADERS.keys()),
            # default=["All"],
        )

        st.markdown(
            '<p style="font-size: 14px;">Modalities:</p>',
            unsafe_allow_html=True,
        )

        # col1, col2, col3 = st.columns([1, 2, 1], gap="medium")
        # st.markdown("Modality Types:")
        checkbox_text = st.checkbox("Text", value=True)
        checkbox_vision = st.checkbox("Vision")
        checkbox_speech = st.checkbox("Speech")

        date_format = "MMM, YYYY"  # format output
        start_date = dt.date(year=2000, month=1, day=1)
        end_date = dt.datetime.now().date()
        # max_days = end_date - start_date

        time_selection = st.slider(
            label="Start Date:",
            min_value=start_date,
            value=start_date,
            max_value=end_date,
            format=date_format,
        )

        st.divider()

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit Selection")

    #### FILTER MENU ENDS HERE

    # legend:
    st.divider()
    st.markdown("**Legend**")
    col0, col1, col2, col3 = st.columns([1, 1, 1, 1], gap="small")
    text_img = create_markdown_img(LOGOS["text"], None, 20)
    vision_img = create_markdown_img(LOGOS["vision"], None, 20)
    speech_img = create_markdown_img(LOGOS["speech"], None, 20)
    arxiv_img = create_markdown_img(LOGOS["arxiv"], None, 20)
    hf_img = create_markdown_img(LOGOS["hf"], None, 20)
    github_img = create_markdown_img(LOGOS["github"], None, 20)
    web_img = create_markdown_img(LOGOS["web"], None, 20)

    col1.markdown(text_img + " = Text Modality", unsafe_allow_html=True)
    col1.markdown(vision_img + " = Vision Modality", unsafe_allow_html=True)
    col1.markdown(speech_img + " = Speech Modality", unsafe_allow_html=True)

    col2.markdown(arxiv_img + " = Paper Link", unsafe_allow_html=True)
    col2.markdown(hf_img + " = HuggingFace Link", unsafe_allow_html=True)
    col2.markdown(github_img + " = GitHub Link", unsafe_allow_html=True)
    col2.markdown(web_img + " = Web Link", unsafe_allow_html=True)
    st.divider()

    if submitted:
        for category in [s for s in ORDERED_SECTION_HEADERS if s in category_select]:

            filtered_resources = filter_resources(
                RESOURCES,
                # sections=category_select,
                sections=[category],
                text_mod=checkbox_text,
                vision_mod=checkbox_vision,
                speech_mod=checkbox_speech,
                time_range=time_selection,
            )

            html_table = filtered_resources.to_html(
                columns=["Modality", "Name", "Description", "Links"],
                index=False,
                header=False,
                escape=False,
                border=0,
            )
            st.header(category)
            st.write(ORDERED_SECTION_HEADERS[category])
            st.write(html_table, unsafe_allow_html=True)
            st.divider()

    # Please don't edit or remove the content of this footer as we'd like to include these important
    # links on all AI2 applications
    theme.add_footer()


if __name__ == "__main__":
    streamlit_app()
