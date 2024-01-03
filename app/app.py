import datetime as dt

import streamlit as st
from PIL import Image
from src.api.api import filter_resources
from src.components.goat_counter import add_goat_counter_tracker
from src.constants import BASE_DIR, ORDERED_SECTION_HEADERS
from src.theme import theme
from src.utils import create_markdown_img, load_data, load_logos


def streamlit_app():
    st.set_page_config(
        page_title="Open Foundation Model Cheatsheet", layout="wide"
    )  # , initial_sidebar_state='collapsed')

    RESOURCES = load_data()
    LOGOS = load_logos()

    # add analytics tracking
    add_goat_counter_tracker()
    # add custom AI2 branded CSS theme and header banner
    theme.add_theme()

    st.title("Open Foundation Model Cheatsheet")
    st.caption(
        "Resources and recommendations for best practices in developing and releasing open models."
    )
    st.markdown(
        """This cheatsheet serves as a succinct guide, prepared *by* open foundation model developers *for*
        developers. As AI foundation model development rapidly expands, welcoming new contributors, scientists,
        and applications, we hope to help new community members become familiar with the latest resources, tools,
        and growing body of research findings. The focus of this cheatsheet is not only to support building, but
        also to inculcate good practices, awareness of limitations, and general responsible habits as
        community norms."""
    )
    scope_limitations_text = """
        There are many exceedingly popular tools to build, distribute and deploy foundation models. But there
        are also many incredible resources that have gone less noticed, in the community's efforts to accelerate,
        deploy, and monetize. We hope to bring wider attention to these core resources that support informed data
        selection, processing, and understanding, precise and limitation-aware artifact documentation,
        resource-frugal model training, advance awareness of the environmental impact from training,
        careful model evaluation and claims, and lastly, responsible model release and deployment practices.

        We've compiled strong resources, tools, and papers that have helped
        guide our own intuitions around model development, and which we believe will be especially helpful to
        nascent (and sometimes even experienced) developers in the field. However, this guide is certainly not
        comprehensive or perfect—and here's what to consider when using it:
        * They are scoped to 'open' model development, by which we mean the model weights will be publicly
        downloadable.
        * Foundation model development is a rapidly evolving science. This cheatsheet is dated to December 2023,
        but our repository is open for on-going public contributions: www.comingsoon.com.
        * We've scoped our content modalities only to text, vision, and speech. We attempt to support multilingual
        resources, but acknowledge these are only a starting point.
        * A cheatsheet cannot be comprehensive. We rely heavily on survey papers and repositories to point out the
        many other awesome works which deserve consideration, especially for developers who plan to dive deeper
        into a topic.
        * Lastly, we do not recommend all these resources for all circumstances, and have provided notes
        throughout to guide this judgement. Instead we hope to bring awareness to good practices that many
        developers neglect in the haste of development (eg careful data decontamination, documentation, and
        carefully specifying the intended downstream uses).
    """
    with st.expander("Scope & Limitations"):
        st.markdown(scope_limitations_text)
    col1a, col1b, col1c = st.columns([0.3, 0.3, 0.4], gap="small")
    # TODO: Replace button links.
    with col1a:
        st.link_button(
            '"2023 Wrapped" Cheatsheet Paper',
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            type="primary",
        )
    with col1b:
        st.link_button(
            "Contribute Resources for 2024!",
            "https://forms.gle/gNtXsqKcG2jwnT9z9",
            type="primary",
        )
    st.markdown(
        """Assembled by open model developers from AI2, EleutherAI, Google, Hugging Face, Masakhane,
        McGill, MIT, Princeton, Stanford CRFM, UCSB, and UW."""
    )

    # SIDEBAR STARTS HERE

    with st.sidebar:
        image = Image.open(BASE_DIR / "resources" / "logos/logo.png")
        # new_size = (width, height)  # Replace 'width' and 'height' with desired values
        # resized_image = image.resize((240,300))
        st.image(image)

        with st.form("data_selection"):
            section_multiselect = st.multiselect(
                label="Resource Types:",
                options=["All"] + list(set(RESOURCES["Type"])),
                default=["All"],
            )

            # st.markdown("######")
            # st.divider()

            st.markdown(
                '<p style="font-size: 14px;">Modality Types:</p>',
                unsafe_allow_html=True,
            )

            # st.markdown("Modality Types:")
            checkbox_text = st.checkbox("Text", value=True)
            checkbox_vision = st.checkbox("Vision")
            checkbox_speech = st.checkbox("Speech")

            # st.markdown("####")
            # st.divider()

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

            # st.markdown("####")

            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit Selection")

    if submitted:
        filtered_resources = filter_resources(
            RESOURCES,
            sections=section_multiselect,
            text_modality=checkbox_text,
            vision_modality=checkbox_vision,
            speech_modality=checkbox_speech,
            time_range=time_selection,
        )

        def write_resource(row):
            col1, col2, col3, col4 = st.columns([0.4, 1, 5, 1], gap="small")

            modality_icons = []
            for mod_img, col in [
                (LOGOS["text"], "Text_Modality"),
                (LOGOS["vision"], "Vision_Modality"),
                (LOGOS["speech"], "Speech_Modality"),
            ]:
                mod_icon = create_markdown_img(mod_img, None, 20) if row[col] else "  "
                modality_icons.append(mod_icon)
            col1.markdown(" ".join(modality_icons), unsafe_allow_html=True)

            col2.write(row["Name"])
            col3.write(row["Description"])

            logo_links = []
            for logo_img, col in [
                (LOGOS["arxiv"], "Paper Link"),
                (LOGOS["hf"], "HF Link"),
                (LOGOS["github"], "GitHub Link"),
                (LOGOS["web"], "Website Link"),
            ]:
                logo_link = (
                    create_markdown_img(logo_img, row[col], dim=20)
                    if row[col]
                    else "  "
                )  # "<div style='width: 30px; height: auto;'></div>"
                logo_links.append(logo_link)
                # col4.markdown(logo_link, unsafe_allow_html=True)
            col4.markdown(" ".join(logo_links), unsafe_allow_html=True)

        sections = [
            x for x in ORDERED_SECTION_HEADERS if x in set(filtered_resources["Type"])
        ]
        for section in sections:
            st.header(section)
            # TODO: show section introductions
            # st.write(constants.ORDERED_SECTION_HEADERS[section])
            st.divider()
            section_resources = filtered_resources[
                filtered_resources["Type"] == section
            ]
            for i, row in section_resources.iterrows():
                write_resource(row)
                st.divider()
                # if i > 3:
                #     break

    # Please don't edit or remove the content of this footer as we'd like to include these important
    # links on all AI2 applications
    theme.add_footer()


if __name__ == "__main__":
    streamlit_app()
