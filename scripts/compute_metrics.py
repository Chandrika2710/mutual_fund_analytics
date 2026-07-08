import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

processed = project_root / "data" / "processed"

files = [
    "cagr_report.csv",
    "sharpe_ratio.csv",
    "sortino_ratio.csv",
    "alpha_beta.csv",
    "max_drawdown.csv"
]

dataframes = []

for file in files:
    path = processed / file

    if path.exists():
        df = pd.read_csv(path)
        dataframes.append(df)
    else:
        print(f"{file} not found.")

performance = dataframes[0]

for df in dataframes[1:]:
    performance = performance.merge(df, on="amfi_code")

performance.to_csv(
    processed / "performance_metrics.csv",
    index=False
)

print("performance_metrics.csv created successfully.")
print(performance.head())