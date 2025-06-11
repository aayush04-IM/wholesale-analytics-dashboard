import streamlit as st
import psycopg2
import pandas as pd
import os

@st.cache_resource
def get_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        sslmode='require'
    )

st.title("Wholesale Analytics Dashboard")

try:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    st.success(f"Connected to DB: {version[0]}")
except Exception as e:
    st.error(f"Database connection failed: {e}")
