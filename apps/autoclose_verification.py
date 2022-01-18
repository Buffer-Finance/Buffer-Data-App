from random import choice
import pandas as pd
import requests
import streamlit as st
from apps.config import BASE_URL


def app():

    st.write(
        """
    ## *Buffer Finance*
    # Auto Close Verification
    """
    )
    choice = st.radio('Select option status', ['Closed', 'Active'])

    response = requests.get(
        f"{BASE_URL}/options/autoclose/verification/?option_status={choice.lower()}")
    options = response.json()
    for data in options:
        asset = data.pop('asset')
        data['asset'] = asset['name']
        data.pop('internal_txns')
        auto_task = data.pop('auto_task')
        data['auto_task'] = str(auto_task)

    st.dataframe(options, 2000, 1000)

    df = pd.DataFrame(options)

    tooltips_df = pd.DataFrame(options)
    st.dataframe(df.style.set_tooltips(tooltips_df))
