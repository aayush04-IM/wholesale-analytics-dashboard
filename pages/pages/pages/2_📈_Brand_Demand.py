import streamlit as st
import plotly.express as px
from dashboard import load_data

st.title("📈 Brand Demand")

query = "SELECT * FROM view_brand_demand;"
df = load_data(query)

st.dataframe(df, use_container_width=True)

if "brand" in df.columns and "demand_score" in df.columns:
    fig = px.bar(df, x="brand", y="demand_score", color="brand", title="Brand Demand Scores")
    st.plotly_chart(fig, use_container_width=True)
