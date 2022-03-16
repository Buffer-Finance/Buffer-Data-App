import streamlit as st
from apps.config import BASE_URL
import requests
from apps.config import BASE_URL, ENVIRONMENT


def app():

    st.write(
        f"""
    ## *Buffer Finance*
    # Cumulative TVL
    """
    )

    environment = st.selectbox(
        'Choose an environment', [_environment for _environment in ENVIRONMENT])

    response = requests.get(f"{BASE_URL}/tvl/?environment={environment}")
    data = response.json()

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
