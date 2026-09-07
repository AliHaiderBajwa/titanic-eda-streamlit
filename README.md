# Titanic EDA — Streamlit Application

An interactive GUI for Exploratory Data Analysis (EDA) built with Streamlit. Upload any CSV dataset, inspect metadata, and visualize column distributions dynamically.

**Live Demo:** [Streamlit App](https://titanic-eda-streamlit.streamlit.app)

## Features

- **CSV Upload** — Drag-and-drop file upload with format validation
- **Dataset Overview** — Row/column count, column data types, missing values per attribute
- **Statistical Summary** — Mean, median, min, max for all numerical columns
- **Column Selector** — Dropdown to pick any column for analysis
- **Auto Type Detection** — Automatically detects numerical vs categorical columns
- **Dynamic Visualization** — Histograms for numerical data, bar charts for categorical data
- **Responsive Layout** — Sidebar controls with a clean main content area

## Tech Stack

| Component | Library |
|-----------|---------|
| Framework | Streamlit |
| Data Handling | Pandas |
| Plotting | Matplotlib |
| Styling | Seaborn |

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/AliHaiderBajwa/titanic-eda-streamlit.git
cd titanic-eda-streamlit
pip install -r requirements.txt
```

### Run Locally

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

## Usage

1. Launch the app
2. Use the sidebar to upload a CSV file
3. View the dataset preview and metadata in the main area
4. Select a column from the dropdown to visualize its distribution
5. The chart updates automatically based on column type (numerical → histogram, categorical → bar chart)

## Project Structure

```
titanic-eda-streamlit/
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── Titanic-Dataset.csv  # Sample dataset for testing
└── README.md
```

## Deployment

This app is deployed on [Streamlit Community Cloud](https://share.streamlit.io).

To deploy your own instance:

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repository
5. Set the main file path to `app.py`
6. Click Deploy

## Sample Dataset

The bundled `Titanic-Dataset.csv` contains 891 passenger records with 12 columns including:

| Column | Type | Description |
|--------|------|-------------|
| Survived | Numerical | Survival (0 = No, 1 = Yes) |
| Pclass | Numerical | Ticket class (1st, 2nd, 3rd) |
| Sex | Categorical | Gender |
| Age | Numerical | Age in years |
| Fare | Numerical | Passenger fare |
| Embarked | Categorical | Port of embarkation |

## License

Academic use — Lab 4, Task 1
