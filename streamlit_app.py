import inspect
import textwrap
import streamlit as st
from pathlib import Path

import data_sources
from data_sources import big_query, snowflake, aws_s3_boto, google_sheet

from utils import ui, intro

DATA_SOURCES = {
    intro.INTRO_IDENTIFIER: {
        "module": intro,
        "secret_key": None,
        "docs_url": None,
        "get_connector": None,
    },
    "🔎  BigQuery": {
        "module": data_sources.big_query,
        "secret_key": "bigquery",
        "docs_url": "https://docs.streamlit.io/knowledge-base/tutorials/databases/bigquery",
        "get_connector": data_sources.big_query.get_connector,
        "tutorial": data_sources.big_query.tutorial,
        "tutorial_anchor": "#tutorial-connecting-to-bigquery",
    },
    "❄️ Snowflake": {
        "module": data_sources.snowflake,
        "secret_key": "snowflake",
        "docs_url": "https://docs.streamlit.io/knowledge-base/tutorials/databases/snowflake",
        "get_connector": data_sources.snowflake.get_connector,
        "tutorial": data_sources.snowflake.tutorial,
        "tutorial_anchor": "#tutorial-connecting-to-snowflake",
    },
    "📦 AWS S3": {
        "module": data_sources.aws_s3_boto,
        "secret_key": "aws_s3",
        "docs_url": "https://docs.streamlit.io/knowledge-base/tutorials/databases/aws-s3",
        "get_connector": data_sources.aws_s3_boto.get_connector,
        "tutorial": data_sources.aws_s3_boto.tutorial,
        "tutorial_anchor": "#tutorial-connecting-to-aws-s3",
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
