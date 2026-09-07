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
    df = pd.read_csv(uploaded_file)
    st.write("Dataset loaded successfully.")
else:
    st.info("Upload a CSV file to begin exploration.")
