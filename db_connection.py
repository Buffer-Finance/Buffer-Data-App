
# # DATABASE
# # def init_connection():
# #     return psycopg2.connect(
# #     host=st.secrets["host"],
# #     database=st.secrets["dbname"],
# #     user=st.secrets["user"],
# #     password=st.secrets["password"])

# # conn = init_connection()

# # def run_query(query):
# #     with conn.cursor() as cur:
# #         cur.execute(query)
# #         return cur.fetchall()

# # user = run_query("SELECT ibfr_token_holders.created_at from ibfr_token_holders;")
# # user = run_query("SELECT ibfr_token_holders.created_at from ibfr_token_holders;")

# # st.title("Graph of Number of holders V time")
# # st.markdown("The dashboard will help a give a better understanding of the  graph f users")

# # fig = go.Figure()

# # for row in rows:
# #   fig.add_trace(go.Scatter(x = row.contract_address, y = row.created_at,
# #                             mode = 'lines',
# #                             name = 'Number of holders V Time'))
