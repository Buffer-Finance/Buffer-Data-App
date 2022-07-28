from email.policy import default
from os import environ
import streamlit as st
import pandas as pd
from pipe import select
import requests
from apps.config import BASE_URL, ENVIRONMENT
# import humanize

import plotly.express as px


# def humanize_value(value: int):
#     if value > 1e4:
#         return humanize.intword(value)
#     return value


def app():
    st.write(
        """
    # Buffer Finance
    ## $iBFR Accounting
    """
    )

    d = requests.get(f"{BASE_URL}/ibfr/accounting/")
    data = d.json()

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)

    col1.metric(
        "General User",
        f'{(round(data["user_balance"], 3))} iBFR',
        # "1.2 °F"
    )
    col2.metric(
        "iBFR Staking Contract",
        f'{(round(data["ibfr_staking"], 3))} iBFR',
        # "-8%"
    )
    col3.metric(
        "Swaps",
        f'{(round(data["swaps"], 3))} iBFR',
        # "4%"
    )
    col4.metric(
        "rBFR staking contract",
        f"{(round(data['rbfr_staking'],3))} iBFR",
        # "4%"
    )
    col5.metric(
        "Multisig Wallet",
        f'{(round(data["multisign"], 3))} iBFR',
        # "4%"
    )
    # col6.metric(
    #     "Vesting",
    #     f"{(round(data['vesting']['total_balance_in_vesting'],3))} iBFR",
    #     # "4%"
    # )

    df = pd.DataFrame({
        'Vesting Contract': list(data['vesting']['owner'].keys()),
        'contract_address': list(
            data['vesting']['contract_address'].values()
        ),
        'total_tokens_allocated': list(
            data['vesting']['total_tokens_allocated'].values()
        ),
        'vested_tokens': list(
            data['vesting']['vested_tokens'].values()
        ), 'unclaimed_vested_tokens': list(
            data['vesting']['unclaimed_vested_tokens'].values()
        ), 'claimed_tokens': list(
            data['vesting']['claimed_tokens'].values()
        ),
        'is_contract_short': list(
            data['vesting']['is_contract_short'].values()
        ),
    })

    st.table(df)
    st.write(
        """
    ## Future projection of tokens to vest
    """
    )

    cumulative_vested_tokens = data['vesting']['cumulative_vesting_schedule']
    contracts = list(data['vesting']['owner'].keys())
    tokens = {}
    for c in contracts:
        tokens.update({c: data['vesting']['all_schedules'][c][0]})

    df = pd.DataFrame(
        {
            'Time': cumulative_vested_tokens[1],
            'All Contracts': cumulative_vested_tokens[0],
            **tokens
        },
        columns=['Time', 'All Contracts',  *contracts]
    )

    fig = px.line(
        df,
        x="Time",
        y=['All Contracts',  *contracts],
    )
    fig.update_xaxes(gridcolor='grey')
    fig.update_yaxes(gridcolor='grey')
    st.plotly_chart(fig)
