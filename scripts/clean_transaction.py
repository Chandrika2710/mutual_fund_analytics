import pandas as pd

df = pd.read_csv(r"C:\Users\chand\Downloads\mutual_fund_analytics\data\raw\08_investor_transactions.csv")

print("Before:", len(df))

df.drop_duplicates(inplace=True)

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

df = df[df["amount_inr"] > 0]

df["transaction_type"] = (
    df["transaction_type"]
    .str.upper()
    .str.strip()
)

print("After:", len(df))

df.to_csv(
    r"C:\Users\chand\Downloads\mutual_fund_analytics\data\processed\clean_transactions.csv",
    index=False
)

print("clean_transactions.csv created")