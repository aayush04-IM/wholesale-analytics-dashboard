import streamlit as st
import pandas as pd
import psycopg2
import toml

# Load secrets from file-based secret on Render
@st.cache_resource
def get_connection():
    secrets = toml.load("/etc/secrets/streamlit_secrets.toml")["DB"]
    return psycopg2.connect(
        host=secrets["HOST"],
        database=secrets["NAME"],
        user=secrets["USER"],
        password=secrets["PASSWORD"],
        port=secrets["PORT"]
    )

# Run a SQL query and return result as a DataFrame
@st.cache_data(ttl=600)
def load_data(query):
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Example default query for testing (you can remove this if not needed)
if __name__ == "__main__":
    st.title("🔗 Test Database Connection")
    query = "SELECT NOW();"  # Replace with your own
    df = load_data(query)
    st.write(df)
