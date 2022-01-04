import streamlit as st
from apps.config import BASE_URL
import pandas as pd
import requests
import plotly.express as px


def app():

    response = requests.get(f"{BASE_URL}/options/stats/?timespan=weekly")
    data = response.json()['all_options']

    st.write(
        """
    ## *Buffer Finance*
    # Options Stats for the current week
    """
    )

    st.subheader(
        f"Current number of options bought this week = {response.json()['current_count']}")

    df = pd.DataFrame(data)

    fig = px.line(
        df,
        x="created_at",
        y="option_count",
        title="Cumulative number of options bought vs time"
    )
    fig.update_xaxes(gridcolor='grey')
    fig.update_yaxes(gridcolor='grey')
    fig.update_traces(line_color="red")
    st.plotly_chart(fig)
