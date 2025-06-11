import streamlit as st
import psycopg2
import pandas as pd

st.set_page_config(page_title="Mega Wholesale Dashboard", layout="wide")

st.title("📦 Mega Wholesale Dashboard")
st.subheader("📊 Stock Availability Across 20 Cities")

# 🔐 Use Render secret environment variables (set these in Render settings)
db_host = st.secrets["DB_HOST"]
db_name = st.secrets["DB_NAME"]
db_user = st.secrets["DB_USER"]
db_pass = st.secrets["DB_PASSWORD"]
db_port = st.secrets["DB_PORT"]

# 🔌 Connect to Supabase
conn = psycopg2.connect(
    host=db_host,
    dbname=db_name,
    user=db_user,
    password=db_pass,
    port=db_port
)

# 🧠 SQL Query from your view
query = "SELECT * FROM view_stock_availability;"
df = pd.read_sql(query, conn)

# 📊 Show data
st.dataframe(df)

# ✅ Clean up
conn.close()
