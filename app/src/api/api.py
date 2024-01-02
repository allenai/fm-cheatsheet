#!/usr/bin/env python3

import pandas as pd


def is_date_match(release_date, filter_start, filter_end="2030"):
    def convert_to_dt(x):
        if isinstance(x, str):
            return (
                pd.to_datetime(x, format="%m-%Y")
                if "-" in x
                else pd.to_datetime(x, format="%Y")
            )
        return x

    if not release_date or release_date.lower() == "frequently updated":
        return True

    try:
        release_datetime = convert_to_dt(release_date)
        filter_start_dt = convert_to_dt(filter_start)
        filter_end_dt = convert_to_dt(filter_end)

        return filter_start_dt <= release_datetime <= filter_end_dt
    except Exception as e:
        raise ValueError(f"Incorrect date format: {e}")


# Function to apply the date filter
def apply_date_filter(df, release_date):
    return df[df["Release MM-YY"].apply(lambda x: is_date_match(x, release_date))]


# Function to search for resources
def search_resources(df, search_string):
    return df[
        df.apply(
            lambda row: search_string.lower() in row["Name"].lower()
            or search_string.lower() in row["Description"].lower(),
            axis=1,
        )
    ]


def preprocess_modalities(df):
    df["Text_Modality"] = df["Modalities"].str.contains("Text") | (
        df["Modalities"] == "All"
    )
    df["Vision_Modality"] = df["Modalities"].str.contains("Vision") | (
        df["Modalities"] == "All"
    )
    df["Speech_Modality"] = df["Modalities"].str.contains("Speech") | (
        df["Modalities"] == "All"
    )
    return df


def filter_resources(
    resources_df, sections, text_modality, vision_modality, speech_modality, time_range
):
    # Preprocess the DataFrame to add modality columns
    filtered_df = preprocess_modalities(resources_df)

    # Apply sections filter
    if "All" not in sections:
        filtered_df = filtered_df[filtered_df["Type"].isin(sections)]

    # Apply combined modality filter using any
    modality_conditions = [
        filtered_df["Text_Modality"]
        if text_modality
        else pd.Series([False] * len(filtered_df)),
        filtered_df["Vision_Modality"]
        if vision_modality
        else pd.Series([False] * len(filtered_df)),
        filtered_df["Speech_Modality"]
        if speech_modality
        else pd.Series([False] * len(filtered_df)),
    ]
    if any([text_modality, vision_modality, speech_modality]):
        filtered_df = filtered_df[pd.concat(modality_conditions, axis=1).any(axis=1)]

    # Apply date filter
    filtered_df = apply_date_filter(filtered_df, time_range)

    return filtered_df
