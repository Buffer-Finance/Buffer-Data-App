import pandas as pd
import requests
import streamlit as st
import plotly.express as px
from apps.config import BASE_URL


def app():
    response = requests.get(f"{BASE_URL}/options/stats/")
    data = response.json()
    st.write(
        """
    ## *Buffer Finance*
    # Cumulative Options Sold
    """
    )

    st.subheader(
        f"Current cumulative options size = {round(response.json()['current_cumulative_option_size'],4)} BNB")

    df = pd.DataFrame(data['cumulative_option_size_graph'])

    fig = px.line(
        df,
        x="created_at",
        y="cumulative_option_size",
        title="Cumulative options size"
    )
    fig.update_xaxes(gridcolor='grey')
    fig.update_yaxes(gridcolor='grey')
    fig.update_traces(line_color="red")
    st.plotly_chart(fig)

    st.subheader(
        f"Current cumulative options count = {response.json()['cumulative_option_count']}")

    df = pd.DataFrame(data['cumulative_options_graph'])

    fig = px.line(
        df,
        x="created_at",
        y="option_count",
        title="Cumulative option count"
    )
    fig.update_xaxes(gridcolor='grey')
    fig.update_yaxes(gridcolor='grey')
    fig.update_traces(line_color="red")
    st.plotly_chart(fig)
