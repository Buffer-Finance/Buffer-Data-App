from multiapp import MultiApp
from apps import ibfr_holders, all_options_stats, asset_iv, option_details, daily_option_stats, options_predictions_stats, weekly_options_stats, cumulative_tvl

app = MultiApp()

app.add_app("All Option Stats", all_options_stats.app)

app.add_app("IBFR Holder Stats", ibfr_holders.app)

app.add_app("Asset IVs", asset_iv.app)

app.add_app("All Option Details", option_details.app)

app.add_app("Daily Option Stats", daily_option_stats.app)

app.add_app("Weekly Option Stats", weekly_options_stats.app)

app.add_app("Cumulative TVL", cumulative_tvl.app)

app.add_app("Overall Options/Predictions Statistics",
            options_predictions_stats.app)


app.run()
