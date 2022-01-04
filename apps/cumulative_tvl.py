import streamlit as st
from apps.config import BASE_URL
import requests


def app():

    response = requests.get(f"{BASE_URL}/tlv/")
    data = response.json()

    st.write(
        f"""
    ## *Buffer Finance*
    # Cumulative TVL
    """
    )
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col1.metric(
        "Liquidity Pool TVL",
        f"${data['write_pool_tvl']} USD",
    )
    col2.metric(
        "Staking Pool TVL",
        f"${data['staking_tvl']}",
    )
    col3.metric(
        "Farm Pool TVL",
        f"${data['farm_tvl']} USD",
    )
    col4.metric(
        "Total TVL",
        f"${data['write_pool_tvl']+data['staking_tvl']+data['farm_tvl']} USD",
    )
