# Design Spec: Titanic EDA Streamlit App

**Date:** 2026-09-07
**Task:** Lab 4, Task 1 — Streamlit-Based Exploratory Data Analysis Interface
**Repo:** https://github.com/AliHaiderBajwa/titanic-eda-streamlit.git

---

## Goal

Build an interactive EDA GUI using Streamlit. Upload a CSV, inspect metadata, select a column, and visualize its distribution. Deploy to Streamlit Community Cloud.

---

## Architecture

Single-file app (`app.py`). No extra modules, no OOP, no unnecessary abstractions.

```
titanic-eda-streamlit/
├── app.py
├── requirements.txt
└── Titanic-Dataset.csv
```

---

## Components

### 1. Sidebar — Interactive Controls

| Control | Widget | Behavior |
|---------|--------|----------|
| File upload | `st.file_uploader` | Accepts `.csv` only. Validates parseability. |
| Column selector | `st.selectbox` | Populated with all column names after upload. |

### 2. Main Area — Top Section (Metadata Display)

Displayed after a CSV is successfully uploaded:

- **Dataset preview:** First 5 rows via `st.dataframe(df.head(5))`
- **Dimensions:** Row count and column count (text or `st.metric`)
- **Column data types:** Table showing each column name and its dtype
- **Missing values:** Table showing each column name and count of nulls
- **Statistical summary:** For all numerical columns — mean, median, min, max (table format)

### 3. Main Area — Bottom Section (Visualization)

Triggered by column selection in sidebar:

- **Type detection:** `pd.api.types.is_numeric_dtype(df[col])`
  - True → numerical
  - False → categorical
- **Numerical:** Matplotlib histogram with `ax.set_xlabel()`, `ax.set_ylabel()`, `ax.set_title()`
- **Categorical:** Matplotlib bar chart with frequency counts, `ax.set_xlabel()`, `ax.set_ylabel()`, `ax.set_title()`
- Rendered via `st.pyplot(fig)`

### 4. Data Flow

```
User uploads CSV
  → pd.read_csv() to parse
  → Validate: is it a proper CSV?
  → Store in st.session_state["df"]
  → Populate sidebar column selector

User selects a column
  → Detect type (numerical vs categorical)
  → Render appropriate chart
  → Always show metadata in top section
```

### 5. Validation & Error Handling

| Condition | Response |
|-----------|----------|
| No file uploaded | `st.info("Upload a CSV file to begin exploration.")` |
| CSV parsing fails | `st.error("Invalid CSV file. Please upload a properly formatted CSV.")` |
| Empty dataframe | `st.warning("The uploaded file contains no data.")` |

---

## Technology Choices

| Component | Choice | Reason |
|-----------|--------|--------|
| Framework | Streamlit | Required by task |
| Data handling | pandas | Standard, already available |
| Plotting | matplotlib + seaborn | Available, works with `st.pyplot` |
| Deployment | Streamlit Community Cloud | Standard free deployment, connects to GitHub |

---

## What Is NOT Included (Scope Boundary)

- No data filtering or query features
- No correlation matrix or pair plots
- No multi-column analysis
- No file export/download
- No custom color themes
- No caching beyond session_state
- No authentication
- No advanced statistical tests

---

## Deployment

1. Push `app.py`, `requirements.txt`, `Titanic-Dataset.csv` to the GitHub repo
2. Connect repo to Streamlit Community Cloud
3. Set main file path to `app.py`
4. App deploys automatically

### requirements.txt

```
streamlit
pandas
matplotlib
seaborn
```
