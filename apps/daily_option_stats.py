import streamlit as st
from apps.config import BASE_URL
import pandas as pd
import requests
import plotly.express as px


def app():

    response = requests.get(f"{BASE_URL}/options/stats/?timespan=daily")
    data = response.json()

    st.write(
        """
    ## *Buffer Finance*
    # Daily Option Stats
    """
    )
    df = pd.DataFrame(data)
    df.rename(columns={'date': 'DATE',
              'created_count': 'OPTIONS BOUGHT'}, inplace=True)

    fig = px.bar(
        df,
        x="DATE",
        y="OPTIONS BOUGHT",
        title="Options bought per day "
    )
    fig.update_xaxes(gridcolor='grey')
    fig.update_yaxes(gridcolor='grey')
    st.plotly_chart(fig)
