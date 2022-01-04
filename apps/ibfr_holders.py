import pandas as pd
import requests
import streamlit as st
import plotly.express as px
from apps.config import BASE_URL


def app():

    response = requests.get(f"{BASE_URL}/ibfr/holders/")
    data = response.json()

    st.write(
        """
    ## *Buffer Finance*
    # IBFR Holder Stats
    """
    )

    st.subheader(f"Current number of IBFR holders = {data['current_holders']}")

    df = pd.DataFrame(dict(
        Timeline=data['dates'],
        IBFR_holders=data['ibfr_holder_count']
    ))

    fig = px.line(
        df,
        x="Timeline",
        y="IBFR_holders",
        title="Number of IBFR holders vs time"
    )
    fig.update_xaxes(gridcolor='grey')
    fig.update_yaxes(gridcolor='grey')
    fig.update_traces(line_color="red")
    st.plotly_chart(fig)
