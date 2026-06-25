import pandas as pd

df = pd.read_csv(r"C:\Users\chand\Downloads\mutual_fund_analytics\data\raw\07_scheme_performance.csv")

print("Before:", len(df))

df.drop_duplicates(inplace=True)

df = df[
    (df["expense_ratio_pct"] >= 0.1)
    &
    (df["expense_ratio_pct"] <= 2.5)
]

print("After:", len(df))

df.to_csv(
    r"C:\Users\chand\Downloads\mutual_fund_analytics\data\processed\clean_performance.csv",
    index=False
)

print("clean_performance.csv created")