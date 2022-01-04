import streamlit as st
import pandas as pd
from pipe import select
import requests


def app():
    st.write(
        """
    # Buffer Finance
    #### *Overall Options/Predictions Statistics*
    """
    )

    r = requests.get("https://api.buffer.finance/stats/json")
    data = r.json()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(
        "Net LP Gain",
        f'{round(data["net_lp_gain"], 3)} BNB',
        # "1.2 °F"
    )
    col2.metric(
        "Net Admin Gain",
        f'{round(data["net_admin_gain"], 3)} BNB',
        # "-8%"
    )
    col3.metric(
        "Net Referral Gain",
        f'{round(data["net_referral_gain"], 3)} BNB',
        # "4%"
    )
    col4.metric(
        "Total Options Sold",
        f"{data['options']['total_sold'] + data['predictions']['total_sold']}",
        # "4%"
    )

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
        ) + [data['option_size']['total_option_size']],
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
