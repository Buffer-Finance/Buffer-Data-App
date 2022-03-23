import pandas as pd
import requests
import streamlit as st
import plotly.express as px
from apps.config import BASE_URL, ENVIRONMENT


def app():

    st.write(
        """
    ## *Buffer Finance*
    # IBFR Holder Stats
    """
    )

    response = requests.get(
        f"{BASE_URL}/ibfr/holding/stats/")
    data = response.json()
    col1, col2 = st.columns(2)

    col1.metric(
        "BSC Mainnet",
        f'{data["mainnet"]} Holders',
        # "1.2 °F"
    )
    col2.metric(
        "Avalanche Mainnet",
        f'{data["avalanche-mainnet"]} Holders',
        # "-8%"
    )
