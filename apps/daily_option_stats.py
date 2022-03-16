import streamlit as st
from apps.config import BASE_URL
import pandas as pd
import requests
import plotly.express as px
from apps.config import BASE_URL, ENVIRONMENT


def app():

    st.write(
        """
    ## *Buffer Finance*
    # Daily Option Stats
    """
    )
    environment = st.selectbox(
        'Choose an environment', [_environment for _environment in ENVIRONMENT])

    response = requests.get(
        f"{BASE_URL}/options/stats/?timespan=daily&environment={environment}")
    data = response.json()

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
