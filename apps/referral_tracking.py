import streamlit as st
from apps.config import BASE_URL, ENVIRONMENT
import requests
import pandas as pd


def app():

    st.write(
        f"""
    ## *Buffer Finance*
    # Referral Tracking
    """
    )

    environment = st.selectbox(
        'Choose an environment', [_environment for _environment in ENVIRONMENT])

    response = requests.get(
        f"{BASE_URL}/referral_tracking/?environment={environment}")
    data = response.json()

    df = pd.DataFrame(data)
    st.table(df)
