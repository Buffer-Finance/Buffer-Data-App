import streamlit as st
from apps.config import BASE_URL
import pandas as pd
import requests
from apps.config import BASE_URL
import plotly.express as px


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

    data = response.json()['data']

    df = pd.DataFrame(
        {
            'Time': data['timestamp'],
            'Actual Price': data['actual_price'],
            'Twap': data['twap'],
        },
        columns=['Time', 'Actual Price', 'Twap']
    )

    fig = px.line(
        df,
        x="Time",
        y=['Actual Price', 'Twap'],
    )
    fig.update_xaxes(gridcolor='grey')
    fig.update_yaxes(gridcolor='grey')
    st.plotly_chart(fig)
