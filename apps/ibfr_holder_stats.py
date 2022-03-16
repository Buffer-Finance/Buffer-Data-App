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
        f"{BASE_URL}/ibfr/balances/")
    data = response.json()['data']

    st.subheader(
        f"Current iBFR holders = {len(data)}")

    st.dataframe(data, 2000, 1000)
