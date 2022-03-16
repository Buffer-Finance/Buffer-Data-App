import pandas as pd
import requests
import streamlit as st
import plotly.express as px
from apps.config import BASE_URL, ENVIRONMENT


def app():

    st.write(
        """
    ## *Buffer Finance*
    # Cumulative Options Sold
    """
    )

    environment = st.selectbox(
        'Choose an environment', [_environment for _environment in ENVIRONMENT])

    response = requests.get(
        f"{BASE_URL}/options/stats/?environment={environment}")
    data = response.json()

    st.subheader(
        f"Current cumulative options size = {round(data['current_cumulative_option_size'],4)} {data['default_asset']}")

    df = pd.DataFrame(data['cumulative_option_size_graph'])

    fig = px.line(
        df,
        x="creation_date",
        y="cumulative_option_size",
        title="Cumulative options size"
    )
    fig.update_xaxes(gridcolor='grey')
    fig.update_yaxes(gridcolor='grey')
    fig.update_traces(line_color="red")
    st.plotly_chart(fig)

    st.subheader(
        f"Current cumulative options count = {data['cumulative_option_count']}")

    df = pd.DataFrame(data['cumulative_options_graph'])

    fig = px.line(
        df,
        x="creation_date",
        y="option_count",
        title="Cumulative option count"
    )
    fig.update_xaxes(gridcolor='grey')
    fig.update_yaxes(gridcolor='grey')
    fig.update_traces(line_color="red")
    st.plotly_chart(fig)
