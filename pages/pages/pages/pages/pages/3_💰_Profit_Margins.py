import streamlit as st
import plotly.express as px
from dashboard import load_data

st.title("💰 Profit Margins")

query = "SELECT * FROM view_product_margins;"
df = load_data(query)

df["margin_date"] = pd.to_datetime(df["margin_date"])
df.columns = [col.replace("_", " ").title() for col in df.columns]

st.dataframe(df, use_container_width=True)

fig = px.line(df, x="Margin Date", y="Margin Percentage", color="Product Name", title="Profit Margins Over Time")
st.plotly_chart(fig, use_container_width=True)
