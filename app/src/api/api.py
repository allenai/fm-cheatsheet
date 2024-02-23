#!/usr/bin/env python3

import warnings

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
        warnings.warn(f"Error in date comparison: {e}")
        return False


# Function to apply the date filter
def apply_date_filter(df, release_date):
    return df[df["Date"].apply(lambda x: is_date_match(x, release_date))]


# Function to search for resources
def search_resources(df, search_string):
    return df[
        df.apply(
            lambda row: search_string.lower() in row["Name"].lower()
            or search_string.lower() in row["Description"].lower(),
            axis=1,
        )
    ]


def filter_resources(
    resources_df, sections, text_mod, vision_mod, speech_mod, time_range
) -> pd.DataFrame:
    # breakpoint()

    # Apply sections filter
    if "All" not in sections:
        resources_df = resources_df[
            resources_df["Categories"].apply(
                lambda x: any(item in sections for item in x)
            )
        ]

    # Apply combined modality filter
    allowed_modalities = {
        m
        for m, flag in zip(
            ["Text", "Vision", "Speech"], [text_mod, vision_mod, speech_mod]
        )
        if flag
    }
    resources_df = resources_df[
        resources_df["Modalities"].apply(
            lambda mods: any(mod in allowed_modalities for mod in mods)
        )
    ]

    # Apply date filter
    resources_df = apply_date_filter(resources_df, time_range)

    return resources_df
