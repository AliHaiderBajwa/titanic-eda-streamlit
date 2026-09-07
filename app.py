import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Titanic EDA", layout="wide")

st.title("Titanic Exploratory Data Analysis")

with st.sidebar:
    st.header("Controls")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        if df.empty:
            st.warning("The uploaded file contains no data.")
        else:
            st.session_state["df"] = df
    except Exception:
        st.error("Invalid CSV file. Please upload a properly formatted CSV.")

if "df" in st.session_state:
    df = st.session_state["df"]
    st.success(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
else:
    st.info("Upload a CSV file to begin exploration.")
