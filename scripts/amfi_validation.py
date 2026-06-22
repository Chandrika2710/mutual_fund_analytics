import pandas as pd

master = pd.read_csv(
    r"C:\Users\chand\Downloads\mutual_fund_analytics\data\raw\01_fund_master.csv"
)

nav = pd.read_csv(
    r"C:\Users\chand\Downloads\mutual_fund_analytics\data\raw\02_nav_history.csv"
)

print("Fund Master Columns:")
print(master.columns)

print("\nNAV History Columns:")
print(nav.columns)

master_codes = set(master["amfi_code"])
nav_codes = set(nav["amfi_code"])

missing = master_codes - nav_codes

print("\nCodes missing in NAV History:")
print(len(missing))

if missing:
    print(missing)
else:
    print("All scheme codes found.")