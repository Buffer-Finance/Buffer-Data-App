import pandas as pd
import requests
import streamlit as st
from apps.config import BASE_URL, ENVIRONMENT


def app():

    st.write(
        """
    ## *Buffer Finance*
    # Auto Close Verification
    """
    )

    environment = st.selectbox(
        'Choose an environment', [_environment for _environment in ENVIRONMENT])

    choice = st.radio('Select option status', ['Closed', 'Active'])

    response = requests.get(
        f"{BASE_URL}/options/autoclose/verification/?option_status={choice.lower()}&environment={environment}")
    options = response.json()
    for data in options:
        asset = data.pop('asset')
        data['asset'] = asset['name']
        data.pop('internal_txns')
        auto_task = data.pop('auto_task')
        data['auto_task'] = str(auto_task)

    st.dataframe(options, 2000, 1000)
