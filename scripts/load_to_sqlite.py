import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///database/bluestock_mf.db"
)

nav = pd.read_csv(r"C:\Users\chand\Downloads\mutual_fund_analytics\data\processed\clean_nav.csv")
txn = pd.read_csv(r"C:\Users\chand\Downloads\mutual_fund_analytics\data\processed\clean_transactions.csv")
perf = pd.read_csv(r"C:\Users\chand\Downloads\mutual_fund_analytics\data\processed\clean_performance.csv")

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database Created Successfully!")