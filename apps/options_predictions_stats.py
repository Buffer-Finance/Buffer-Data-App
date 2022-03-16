from email.policy import default
from os import environ
import streamlit as st
import pandas as pd
from pipe import select
import requests
from apps.config import BASE_URL, ENVIRONMENT


def app():
    st.write(
        """
    # Buffer Finance
    #### *Overall Options/Predictions Statistics*
    """
    )

    environment = st.selectbox(
        'Choose an environment', [_environment for _environment in ENVIRONMENT])

    r = requests.get(f"{BASE_URL}/stats/?environment={environment}")
    data = r.json()

    default_asset = data["default_asset"]

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)
    col7, col8 = st.columns(2)

    col1.metric(
        "Net LP Gain",
        f'{round(data["net_lp_gain"], 3)} {default_asset}',
        # "1.2 °F"
    )
    col2.metric(
        "Net Admin Gain",
        f'{round(data["net_admin_gain"], 3)} {default_asset}',
        # "-8%"
    )
    col3.metric(
        "Net Referral Gain",
        f'{round(data["net_referral_gain"], 3)} {default_asset}',
        # "4%"
    )
    col4.metric(
        "Total Options Sold",
        f"{data['options']['total_sold'] + data['predictions']['total_sold']}",
        # "4%"
    )
    col5.metric(
        "Realised LP Gain",
        f'{round(data["realised_lp_gain"], 3)} {default_asset}',
    )
    col6.metric(
        "Unrealised LP Gain",
        f'{round(data["unrealised_lp_gain"], 3)} {default_asset}',
    )
    col7.metric(
        "LP Utilization",
        f'{data["lp_utilization"]} %',
    )
    col8.metric(
        "LP Balance",
        f'{round(data["lp_balance"], 3)} {default_asset}',
    )

    total_option_size = [data['option_size']['total_option_size']] if [
        data['option_size']['total_option_size']] != ['-'] else [None]

    df = pd.DataFrame({
        'Assets': list(data['options']['options_sold_per_asset'].keys()) + ['Total'],
        'Options': list(
            data['options']['options_sold_per_asset'].values()
        ) + [data['options']['total_sold']],
        'Predictions': list(
            data['predictions']['predictions_sold_per_asset'].values()
        ) + [data['predictions']['total_sold']],
        'Option Size': list(
            data['option_size']['option_size_per_asset'].values()
            | select(lambda x: round(x, 1))
        ) + total_option_size,
        'Option Default Asset Size': list(
            data['option_default_asset_size']['option_size_per_asset'].values()
            | select(lambda x: round(x, 1))
        ) + [data['option_default_asset_size']['total_option_default_asset_size']],
        'Positive Payout/Asset': list(
            data['positive_payout']['positive_payout_per_asset'].values()
            | select(lambda x: round(x, 1))
        ) + [data['positive_payout']['total_positive_payout']],
        'Positive Net Profit/Asset': list(
            data['positive_net_profit']['positive_net_profit_per_asset'].values()
            | select(lambda x: round(x, 1))
        ) + [data['positive_net_profit']['total_positive_net_profit']]
    })
    st.table(df)
