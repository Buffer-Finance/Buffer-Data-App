from multiapp import MultiApp
from apps import ibfr_holder_stats, cumulative_options_sold, ibfr_holders, autoclose_verification, asset_iv, option_details, daily_option_stats, options_predictions_stats, referral_tracking, weekly_options_stats, cumulative_tvl, ibfr_moving_price_average
app = MultiApp()

app.add_app("Overall Options/Predictions Statistics",
            options_predictions_stats.app)
app.add_app("Cumulative Options Sold", cumulative_options_sold.app)
app.add_app("Daily Option Stats", daily_option_stats.app)
app.add_app("Weekly Option Stats", weekly_options_stats.app)
app.add_app("Cumulative TVL", cumulative_tvl.app)
app.add_app("Asset IVs", asset_iv.app)
app.add_app("All Option Details", option_details.app)
app.add_app("Referral Tracking", referral_tracking.app)
app.add_app("Auto Close Verification", autoclose_verification.app)
app.add_app("IBFR Holder Stats", ibfr_holder_stats.app)
# app.add_app("IBFR Moving Price Average", ibfr_moving_price_average.app)
# app.add_app("IBFR Holder Stats", ibfr_holders.app)
app.run()