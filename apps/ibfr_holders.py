import pandas as pd
import requests
import streamlit as st
import plotly.express as px
from apps.config import BASE_URL, ENVIRONMENT


def app():

    st.write(
        """
    ## *Buffer Finance*
    # IBFR Holder Stats
    """
    )

    environment = st.selectbox(
        'Choose an environment', [_environment for _environment in ENVIRONMENT])

    response = requests.get(
        f"{BASE_URL}/ibfr/holders/?environment={environment}")
    data = response.json()

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
