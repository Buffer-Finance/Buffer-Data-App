import pandas as pd
import requests
import streamlit as st
from apps.config import BASE_URL


def app():

    response = requests.get(f"{BASE_URL}/options/?environment=mainnet")
    data = response.json()['data']['options']

    st.write(
        """
    ## *Buffer Finance*
    # All Option Details
    """
    )

    df = pd.DataFrame(data)
    del df['internal_txns']
    st.table(df)
