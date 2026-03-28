import pandas as pd
import streamlit as st


def fix_text_encoding(text):
    """
    Try to repair mojibake text caused by an incorrect UTF-8 / Latin-1 decoding.

    Example:
    'RamÃ³n SÃ¡nchez-PizjuÃ¡n' -> 'Ramón Sánchez-Pizjuán'
    """
    if not isinstance(text, str):
        return text

    try:
        return text.encode("latin1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        # Return the original value if the text cannot be repaired
        return text


@st.cache_data
def load_matches_data():
    """
    Load the La Liga dataset and automatically fix text encoding issues
    in all string columns.
    """
    df = pd.read_csv("data/la-liga-2024.csv")

    # Detect all text-based columns in the dataset
    text_columns = df.select_dtypes(include=["object"]).columns

    # Apply encoding repair to every text column
    for column in text_columns:
        df[column] = df[column].apply(fix_text_encoding)

    return df