import base64
import gzip
import os
from pathlib import Path

import jsonlines
import pandas as pd
import streamlit as st

from .constants import BASE_DIR


def read_jsonl(inpath: Path):
    if inpath.suffix in (".gz", ".gzip"):
        with gzip.open(inpath, "rb") as fp:
            j_reader = jsonlines.Reader(fp)
            return [l for l in j_reader]
    else:
        with open(inpath, "rb") as fp:
            j_reader = jsonlines.Reader(fp)
            return [l for l in j_reader]


@st.cache_data
def load_data():
    df = pd.DataFrame(read_jsonl(BASE_DIR / "resources" / "resources.jsonl")).fillna("")
    logos = load_logos()

    def add_links(row):
        links = []
        if row["Paper Link"]:
            links.append(create_markdown_img(logos["arxiv"], row["Paper Link"], 20))
        if row["HuggingFace Link"]:
            links.append(create_markdown_img(logos["hf"], row["HuggingFace Link"], 20))
        if row["GitHub Link"]:
            links.append(create_markdown_img(logos["github"], row["GitHub Link"], 20))
        if row["Website Link"]:
            links.append(create_markdown_img(logos["web"], row["Website Link"], 20))

        return "  ".join(links)

    df["Links"] = df.apply(add_links, axis=1)

    def add_modality(row):
        return " ".join(
            [
                create_markdown_img(logos[modality.lower()], None, 20)
                for modality in row["Modalities"]
            ]
        )

    df["Modality"] = df.apply(add_modality, axis=1)

    return df


def load_logos():
    def get_image_base64(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()

    return {
        "hf": get_image_base64(BASE_DIR / "resources" / "logos/hf.png"),
        "web": get_image_base64(BASE_DIR / "resources" / "logos/web.png"),
        "arxiv": get_image_base64(BASE_DIR / "resources" / "logos/arxiv.png"),
        "github": get_image_base64(BASE_DIR / "resources" / "logos/github.png"),
        "text": get_image_base64(BASE_DIR / "resources" / "logos/text.png"),
        "vision": get_image_base64(BASE_DIR / "resources" / "logos/vision.png"),
        "speech": get_image_base64(BASE_DIR / "resources" / "logos/speech.png"),
    }


def create_markdown_img(base64_string, link_url=None, dim=15):
    img_tag = f'<img src="data:image/png;base64,{base64_string}" width="{dim}px" height="{dim}px" alt="Image">'
    if link_url:
        return f'<a href="{link_url}" target="_blank">{img_tag}</a>'
    else:
        return img_tag


def get_environment():
    return os.getenv("STREAMLIT_ENV", "dev")
