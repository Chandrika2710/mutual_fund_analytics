import pandas as pd

df = pd.read_csv(r"C:\Users\chand\Downloads\mutual_fund_analytics\data\raw\01_fund_master.csv")

print("\nColumns:")
print(df.columns)

print("\nUnique Fund Houses")
print(df["fund_house"].unique())

print("\nUnique Categories")
print(df["category"].unique())

print("\nUnique Sub Categories")
print(df["sub_category"].unique())

if "risk_grade" in df.columns:
    print("\nRisk Grades")
    print(df["risk_grade"].unique())