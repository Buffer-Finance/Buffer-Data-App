import streamlit as st
from apps.config import BASE_URL
import pandas as pd
import requests
import plotly.express as px


def app():
    st.write(
        """
    ## *Buffer Finance*
    # Performance Monitoring - BE
    """
    )
    response = requests.get(
        f"{BASE_URL}/binary/performance/backend/")
    data = response.json()
    df = pd.DataFrame(
        {
            'Time Lag': data['time_lag'],
            'Time': data['time'],
        },
        columns=['Time Lag', 'Time']
    )

    fig = px.line(
        df,
        y='Time Lag',
        x='Time'
    )
    fig.update_xaxes(gridcolor='grey')
    fig.update_yaxes(gridcolor='grey')
    st.plotly_chart(fig)
