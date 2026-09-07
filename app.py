import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Titanic EDA", layout="wide")

st.title("Titanic Exploratory Data Analysis")

with st.sidebar:
    st.header("Controls")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if "df" in st.session_state:
        selected_column = st.selectbox(
            "Select a column to visualize",
            st.session_state["df"].columns.tolist()
        )
        st.session_state["selected_column"] = selected_column

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        if df.empty:
            st.warning("The uploaded file contains no data.")
        else:
            if "df" not in st.session_state:
                st.session_state["df"] = df
                st.rerun()
            st.session_state["df"] = df
    except Exception:
        st.error("Invalid CSV file. Please upload a properly formatted CSV.")

if "df" in st.session_state:
    df = st.session_state["df"]
    st.success(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

    st.subheader("Dataset Preview")
    st.dataframe(df.head(5))

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Dimensions:**")
        st.write(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")

    st.markdown("**Column Data Types:**")
    dtypes_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": [str(df[col].dtype) for col in df.columns]
    })
    st.dataframe(dtypes_df, use_container_width=True)

    st.markdown("**Missing Values:**")
    missing_df = pd.DataFrame({
        "Column": df.columns,
        "Missing Count": [df[col].isnull().sum() for col in df.columns]
    })
    st.dataframe(missing_df, use_container_width=True)

    st.markdown("**Statistical Summary (Numerical Columns):**")
    num_cols = df.select_dtypes(include="number").columns.tolist()
    if num_cols:
        stats_df = pd.DataFrame({
            "Column": num_cols,
            "Mean": [df[col].mean() for col in num_cols],
            "Median": [df[col].median() for col in num_cols],
            "Min": [df[col].min() for col in num_cols],
            "Max": [df[col].max() for col in num_cols]
        })
        st.dataframe(stats_df, use_container_width=True)
    else:
        st.write("No numerical columns found.")

    if "selected_column" in st.session_state:
        selected_column = st.session_state["selected_column"]
        st.subheader("Visualization")

        is_numerical = pd.api.types.is_numeric_dtype(df[selected_column])
        chart_type = "Numerical" if is_numerical else "Categorical"
        st.write(f"**{selected_column}** — Type: {chart_type}")

        fig, ax = plt.subplots(figsize=(10, 5))

        if is_numerical:
            ax.hist(df[selected_column].dropna(), bins=30, edgecolor="black")
            ax.set_xlabel(selected_column)
            ax.set_ylabel("Frequency")
            ax.set_title(f"Distribution of {selected_column}")
        else:
            value_counts = df[selected_column].value_counts()
            ax.bar(value_counts.index.astype(str), value_counts.values)
            ax.set_xlabel(selected_column)
            ax.set_ylabel("Count")
            ax.set_title(f"Frequency of {selected_column}")
            plt.xticks(rotation=45, ha="right")

        st.pyplot(fig)
        plt.close(fig)

else:
    st.info("Upload a CSV file to begin exploration.")
