import streamlit as st
from apps.config import BASE_URL
import pandas as pd
import requests
from apps.config import BASE_URL
import numpy as np
def app():
    st.write(
        """
    ## *Buffer Finance*
    # $iBFR Moving Price Average
    """
    )
    environment = st.selectbox(
        'Choose an environment', ['mainnet'])
    token = "iBFR"
    response = requests.get(
        f"{BASE_URL}/token/price/all_time/?token={token}&environment={environment}")
    data = response.json()
    chart_data = pd.DataFrame(
        np.array(data['data']),
        columns=['Actual Price', 'Twap'])
    st.line_chart(chart_data)