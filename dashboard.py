# dashboard.py (main file)

import streamlit as st
import psycopg2
import pandas as pd

st.set_page_config(page_title="📊 Mega Wholesale Dashboard", layout="wide")

st.title("📊 Mega Wholesale Dashboard")
st.markdown("Welcome to your central analytics hub for your 20-city wholesale business.")

@st.cache_resource
def get_connection():
    return psycopg2.connect(
        host=st.secrets["DB_HOST"],
        dbname=st.secrets["DB_NAME"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"],
        port=st.secrets["DB_PORT"]
    )

def load_data(query):
    conn = get_connection()
    return pd.read_sql(query, conn)
