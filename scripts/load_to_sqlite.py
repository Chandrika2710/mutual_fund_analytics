import os
import pandas as pd
from sqlalchemy import create_engine

# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database path
db_path = os.path.join(BASE_DIR, "database", "bluestock_mf.db")

engine = create_engine(f"sqlite:///{db_path}")

# Load processed files
nav = pd.read_csv(os.path.join(BASE_DIR, "data", "processed", "clean_nav.csv"))
txn = pd.read_csv(os.path.join(BASE_DIR, "data", "processed", "clean_transactions.csv"))
perf = pd.read_csv(os.path.join(BASE_DIR, "data", "processed", "clean_performance.csv"))

# Store into SQLite
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
txn.to_sql("fact_transactions", engine, if_exists="replace", index=False)
perf.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("Database Created Successfully!")