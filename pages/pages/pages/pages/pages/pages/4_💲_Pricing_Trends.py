import streamlit as st
import plotly.express as px
from dashboard import load_data

st.title("💲 Pricing Trends")

query = "SELECT * FROM view_pricing_trends;"
df = load_data(query)

df["price_date"] = pd.to_datetime(df["price_date"])
df.columns = [col.replace("_", " ").title() for col in df.columns]

st.dataframe(df, use_container_width=True)

fig = px.line(df, x="Price Date", y="Price", color="Product Name", title="Pricing Trends Over Time")
st.plotly_chart(fig, use_container_width=True)
