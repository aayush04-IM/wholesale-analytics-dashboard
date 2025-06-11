import os
import psycopg2
import streamlit as st

# Title
st.set_page_config(page_title="Wholesale Analytics Dashboard", layout="wide")
st.title("📊 Wholesale Analytics Dashboard")

# Get database connection
@st.cache_resource
def get_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        sslmode="require"
    )

# Run a test query and display result
try:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    st.success(f"Connected to: {version[0]}")
except Exception as e:
    st.error("❌ Failed to connect to database.")
    st.exception(e)
