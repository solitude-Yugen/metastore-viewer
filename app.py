import streamlit as st
import pandas as pd

# Title
st.title("Metastore Viewer Prototype")

# File uploader
uploaded_file = st.file_uploader("Upload a Parquet file", type=["parquet"])

if uploaded_file:
    # Read Parquet file
    df = pd.read_parquet(uploaded_file, engine="pyarrow")

    # Display metadata
    st.subheader("Table Schema")
    st.write(df.dtypes)  # Show column names & data types

    st.subheader("Table Preview")
    st.write(df.head())  # Show first few rows

    st.subheader("Key Metrics")
    st.write(f"📌 Total Rows: {df.shape[0]}")
    st.write(f"📌 Total Columns: {df.shape[1]}")
