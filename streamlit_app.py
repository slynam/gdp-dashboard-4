import inspect
import textwrap
import streamlit as st
from pathlib import Path

import data_sources
from data_sources import google_sheet

from utils import ui, intro

DATA_SOURCES = {
    intro.INTRO_IDENTIFIER: {
        "module": intro,
        "secret_key": None,
        "docs_url": None,
        "get_connector": None,
    },
    "📝 Google Sheet": {
        "module": data_sources.google_sheet,
        "secret_key": "gsheets",
        "docs_url": "https://docs.streamlit.io/en/latest/tutorial/public_gsheet.html#connect-streamlit-to-a-public-google-sheet",
        "get_connector": data_sources.google_sheet.get_connector,
        "tutorial": data_sources.google_sheet.tutorial,
        "tutorial_anchor": "#tutorial-connecting-to-google-sheet",
    },
}
