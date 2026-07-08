# 📊 Bluestock Mutual Fund Analytics Capstone

## Project Overview

The Bluestock Mutual Fund Analytics Capstone is an end-to-end data analytics project that analyzes mutual fund performance using Python, SQLite, SQL, and Power BI. The project performs data ingestion, cleaning, exploratory data analysis (EDA), performance metric calculations, and interactive dashboard visualization to provide meaningful insights into mutual fund investments.

---

## Objectives

- Collect and organize mutual fund datasets.
- Clean and preprocess raw financial data.
- Store processed data in SQLite.
- Perform exploratory data analysis.
- Calculate key mutual fund performance metrics.
- Build an interactive Power BI dashboard.
- Generate investment recommendations using analytical metrics.

---

## Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- SQL
- Jupyter Notebook
- Power BI
- Matplotlib
- Requests API

---

# Project Structure

```
bluestock_mf_capstone/

│── README.md
│── requirements.txt

├── dashboard/
│     bluestock_mf_dashboard.pbix

├── data/
│     ├── raw/
│     ├── processed/
│
├── database/
│     bluestock_mf.db

├── notebooks/
│     01_data_ingestion.ipynb
│     02_data_cleaning.ipynb
│     03_eda_analysis.ipynb
│     04_performance_analytics.ipynb
│     05_advanced_analytics.ipynb

├── reports/

├── scripts/
│     etl_pipeline.py
│     compute_metrics.py
│     recommender.py
│     live_nav_fetch.py
│     load_to_sqlite.py
│     clean_nav.py
│     clean_performance.py
│     clean_transaction.py

├── sql/
│     schema.sql
│     queries.sql
```

---

# Dataset

The project uses the following datasets:

- Fund Master
- NAV History
- AUM by Fund House
- Monthly SIP Inflows
- Category Inflows
- Industry Folio Count
- Scheme Performance
- Investor Transactions
- Portfolio Holdings
- Benchmark Indices
- Live NAV Data

---

# Project Workflow

```
Raw Data
      │
      ▼
Data Ingestion
      │
      ▼
Data Cleaning
      │
      ▼
SQLite Database
      │
      ▼
EDA
      │
      ▼
Performance Metrics
      │
      ▼
Advanced Analytics
      │
      ▼
Power BI Dashboard
      │
      ▼
Investment Recommendations
```

---

# Performance Metrics

The following financial metrics are calculated:

- CAGR (Compound Annual Growth Rate)
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
- Risk-Adjusted Performance

---

# Dashboard Features

The Power BI dashboard includes:

- Executive Summary
- Fund Performance Analysis
- Investor & SIP Analysis
- Risk Analytics Dashboard

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
```

Go to the project directory:

```bash
cd bluestock_mf_capstone
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Execute the ETL pipeline:

```bash
python scripts/etl_pipeline.py
```

Generate performance metrics:

```bash
python scripts/compute_metrics.py
```

Generate recommendations:

```bash
python scripts/recommender.py
```

---

# Outputs

The project generates:

- Cleaned datasets
- SQLite Database
- Performance metrics
- Recommendation dataset
- Power BI Dashboard

---

# Key Insights

- Mutual fund performance was evaluated using standard financial metrics.
- Risk-adjusted returns were analyzed using Sharpe and Sortino Ratios.
- Alpha and Beta were used to compare funds against benchmark performance.
- Maximum Drawdown highlighted downside risk.
- Interactive Power BI dashboards provide comprehensive visualization and insights.

---

# Future Enhancements

- Real-time NAV updates
- Machine Learning-based fund recommendation
- Portfolio optimization
- Web dashboard deployment
- Automated data refresh

---

# Author

**Chandrika Katakam**

B.Tech Computer Science and Engineering

Bluestock Mutual Fund Analytics Capstone Project

2026

---

# License

This project is developed for educational and academic purposes.