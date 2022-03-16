import pandas as pd
import requests
import streamlit as st
from apps.config import BASE_URL, ENVIRONMENT


def app():

    st.write(
        """
    ## *Buffer Finance*
    # Asset IVs
    """
    )

    environment = st.selectbox(
        'Choose an environment', [_environment for _environment in ENVIRONMENT])

    response = requests.get(
        f"{BASE_URL}/options/assets/iv/?environment={environment}")

    data = response.json()

    df = pd.DataFrame(list(zip(data['asset_names'], data['asset_ivs'], data['iv_change_percent'])), columns=[
                      'ASSET NAMES', 'IV', 'IV CHANGE %'])

    st.table(df)
    chosen_asset = st.selectbox(
        'Choose an asset to view the changes in IV', df['ASSET NAMES'])

    if chosen_asset:

        iv_change_response = requests.get(
            f"{BASE_URL}/options/assets/iv/?asset={chosen_asset}&environment={environment}")

        df = pd.DataFrame(iv_change_response.json())
        st.table(df)
