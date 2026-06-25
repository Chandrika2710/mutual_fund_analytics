import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Before:", len(df))

df["date"] = pd.to_datetime(df["date"])

df.drop_duplicates(inplace=True)

df.sort_values("date", inplace=True)

df["nav"] = df["nav"].fillna(method="ffill")

print("After:", len(df))

df.to_csv(
    "data/processed/clean_nav.csv",
    index=False
)

print("clean_nav.csv created")