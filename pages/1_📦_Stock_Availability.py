import streamlit as st
from dashboard import load_data

st.title("📦 Stock Availability")

query = "SELECT * FROM view_stock_availability;"
df = load_data(query)
df.columns = [col.replace("_", " ").title() for col in df.columns]

st.dataframe(df, use_container_width=True)
