import pandas as pd
import requests
import streamlit as st
import plotly.express as px
from apps.config import BASE_URL


def app():
    response = requests.get(f"{BASE_URL}/options/stats/?timespan=all")
    data = response.json()['all_options']
    st.write(
        """
    ## *Buffer Finance*
    # All Options Stats
    """
    )

    st.subheader(
        f"Current number of options bought = {response.json()['current_value']}")

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
