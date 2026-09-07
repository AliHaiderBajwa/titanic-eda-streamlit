# Titanic EDA Streamlit App — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a single-file Streamlit EDA app that uploads CSV, shows metadata, and plots distributions.

**Architecture:** Single `app.py` using Streamlit widgets in sidebar, metadata in main top, charts in main bottom. Uses pandas for data, matplotlib for plotting.

**Tech Stack:** Python 3, Streamlit, pandas, matplotlib, seaborn

## Global Constraints

- Single file: `app.py` — no additional modules
- Libraries: streamlit, pandas, matplotlib, seaborn only
- No features beyond what Task 1 spec requires
- CSV-only upload (validate format)
- Plots use matplotlib with axis labels and title
- Deploy to Streamlit Community Cloud via GitHub

---

## File Structure

| File | Responsibility |
|------|---------------|
| `app.py` | Entire application logic |
| `requirements.txt` | Dependencies for deployment |
| `Titanic-Dataset.csv` | Bundled test dataset |

---

### Task 1: Project Scaffolding

**Files:**
- Create: `requirements.txt`
- Create: `app.py` (initial skeleton)

**Interfaces:**
- Produces: runnable `app.py` that launches Streamlit with empty sidebar

- [ ] **Step 1: Create requirements.txt**

```
streamlit
pandas
matplotlib
seaborn
```

- [ ] **Step 2: Create app.py skeleton**

```python
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
```

- [ ] **Step 3: Run and verify app launches**

Run: `streamlit run app.py`
Expected: Browser opens, shows title, sidebar with file uploader, info message when no file uploaded

- [ ] **Step 4: Commit**

```bash
git init && git add requirements.txt app.py Titanic-Dataset.csv
git commit -m "feat: project scaffolding with skeleton app"
```

---

### Task 2: File Upload Validation + Error Handling

**Files:**
- Modify: `app.py`

**Interfaces:**
- Consumes: `uploaded_file` from `st.file_uploader`
- Produces: validated `df` in `st.session_state`, or error/warning messages

- [ ] **Step 1: Add CSV validation and session state**

Replace the app.py content with:

```python
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
```

- [ ] **Step 2: Test with valid CSV**

Run: `streamlit run app.py`, upload `Titanic-Dataset.csv`
Expected: Success message with row/column count

- [ ] **Step 3: Test with invalid file**

Upload a non-CSV file (e.g., .txt)
Expected: Error message "Invalid CSV file..."

- [ ] **Step 4: Commit**

```bash
git add app.py
git commit -m "feat: file upload validation and error handling"
```

---

### Task 3: Metadata Display

**Files:**
- Modify: `app.py`

**Interfaces:**
- Consumes: `df` from `st.session_state`
- Produces: metadata section rendered in main area

- [ ] **Step 1: Add metadata display after the success message**

After `st.success(...)` add:

```python
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
```

- [ ] **Step 2: Run and verify all metadata sections render**

Run: `streamlit run app.py`, upload `Titanic-Dataset.csv`
Expected: Preview table, dimensions, dtypes table, missing values table, stats table all visible

- [ ] **Step 3: Commit**

```bash
git add app.py
git commit -m "feat: metadata display with preview, dtypes, missing values, stats"
```

---

### Task 4: Column Selector + Type Detection

**Files:**
- Modify: `app.py`

**Interfaces:**
- Consumes: `df` columns list
- Produces: selected column name and detected type, passed to visualization

- [ ] **Step 1: Add column selector in sidebar**

Inside the `with st.sidebar:` block, after the file uploader, add:

```python
    if "df" in st.session_state:
        selected_column = st.selectbox(
            "Select a column to visualize",
            st.session_state["df"].columns.tolist()
        )
```

- [ ] **Step 2: Add type detection logic**

After the metadata section, before visualization, add:

```python
    if "selected_column" not in st.session_state:
        st.session_state["selected_column"] = selected_column

    st.subheader(f"Visualization: {selected_column}")

    is_numerical = pd.api.types.is_numeric_dtype(df[selected_column])
    if is_numerical:
        st.write(f"Type: **Numerical**")
    else:
        st.write(f"Type: **Categorical**")
```

Note: `selected_column` is set in sidebar. Move this code to after metadata but inside the `if "df" in st.session_state` block. The sidebar selectbox updates `st.session_state["selected_column"]` on change.

Refined approach — replace the sidebar section and add type display:

```python
with st.sidebar:
    st.header("Controls")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if "df" in st.session_state:
        selected_column = st.selectbox(
            "Select a column to visualize",
            st.session_state["df"].columns.tolist()
        )
```

After metadata section:

```python
    st.subheader("Visualization")

    is_numerical = pd.api.types.is_numeric_dtype(df[selected_column])
    chart_type = "Numerical" if is_numerical else "Categorical"
    st.write(f"**{selected_column}** — Type: {chart_type}")
```

- [ ] **Step 3: Run and verify**

Run: `streamlit run app.py`, upload CSV, select different columns
Expected: Dropdown appears in sidebar, type label updates correctly when switching between numerical and categorical columns

- [ ] **Step 4: Commit**

```bash
git add app.py
git commit -m "feat: column selector with automatic type detection"
```

---

### Task 5: Visualization — Histogram + Bar Chart

**Files:**
- Modify: `app.py`

**Interfaces:**
- Consumes: `df`, `selected_column`, `is_numerical`
- Produces: matplotlib figure rendered via `st.pyplot`

- [ ] **Step 1: Add plotting logic after type detection**

After the type display, add:

```python
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
```

- [ ] **Step 2: Test numerical column**

Run: `streamlit run app.py`, upload CSV, select `Age` (numerical)
Expected: Histogram with labeled axes and title

- [ ] **Step 3: Test categorical column**

Select `Sex` or `Embarked` (categorical)
Expected: Bar chart with labeled axes and title, rotated x-labels

- [ ] **Step 4: Commit**

```bash
git add app.py
git commit -m "feat: histogram and bar chart visualization"
```

---

### Task 6: Final Cleanup + Deploy Prep

**Files:**
- Modify: `app.py` (if needed)
- Verify: `requirements.txt`
- Verify: `Titanic-Dataset.csv`

**Interfaces:**
- None (polish pass)

- [ ] **Step 1: Full test run**

Run: `streamlit run app.py`
Test all paths:
- No file → info message
- Invalid file → error message
- Valid CSV → preview, metadata, column selector, plots update dynamically
- Switch between numerical and categorical columns → chart type changes

- [ ] **Step 2: Verify no extra features**

Check that the app does NOT include: filtering, correlation, multi-column, export, themes — only what's in the spec.

- [ ] **Step 3: Push to GitHub**

```bash
git remote add origin https://github.com/AliHaiderBajwa/titanic-eda-streamlit.git
git push -u origin main
```

- [ ] **Step 4: Deploy to Streamlit Community Cloud**

1. Go to share.streamlit.io
2. Connect GitHub account
3. Select repo `AliHaiderBajwa/titanic-eda-streamlit`
4. Set main file path to `app.py`
5. Deploy

- [ ] **Step 5: Final commit**

```bash
git add -A
git commit -m "chore: final cleanup and deploy prep"
```
