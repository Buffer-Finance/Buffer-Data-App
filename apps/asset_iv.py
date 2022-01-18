import pandas as pd
import requests
import streamlit as st
from apps.config import BASE_URL


def app():

    response = requests.get(f"{BASE_URL}/options/assets/iv/")

    data = response.json()

    st.write(
        """
    ## *Buffer Finance*
    # Asset IVs
    """
    )
    df = pd.DataFrame(list(zip(data['asset_names'], data['asset_ivs'], data['iv_change_percent'])), columns=[
                      'ASSET NAMES', 'IV (in %)', 'IV CHANGE %'])

    st.table(df)
    chosen_asset = st.selectbox(
        'Choose an asset to view the changes in IV', df['ASSET NAMES'])

    if chosen_asset:

        iv_change_response = requests.get(
            f"{BASE_URL}/options/assets/iv/?asset={chosen_asset}")

        df = pd.DataFrame(iv_change_response.json())
        st.table(df)

