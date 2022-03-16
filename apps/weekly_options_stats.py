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
    # Options Stats for the current week
    """
    )

    environment = st.selectbox(
        'Choose an environment', [_environment for _environment in ENVIRONMENT])

    response = requests.get(
        f"{BASE_URL}/options/stats/?timespan=weekly&environment={environment}")
    data = response.json()
    all_options = data['all_options']

    st.subheader(
        f"Current number of options bought this week = {data['current_count']}")

    df = pd.DataFrame(all_options)

    fig = px.line(
        df,
        x="creation_date",
        y="option_count",
        title="Cumulative number of options bought vs time"
    )
    fig.update_xaxes(gridcolor='grey')
    fig.update_yaxes(gridcolor='grey')
    fig.update_traces(line_color="red")
    st.plotly_chart(fig)
