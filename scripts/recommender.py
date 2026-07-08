import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

processed = project_root / "data" / "processed"

performance = pd.read_csv(
    processed / "performance_metrics.csv"
)


def recommend(row):

    if (
        row["Sharpe Ratio"] >= 1
        and row["CAGR (%)"] >= 15
        and row["Max Drawdown (%)"] > -20
    ):
        return "Highly Recommended"

    elif (
        row["Sharpe Ratio"] >= 0.5
        and row["CAGR (%)"] >= 10
    ):
        return "Recommended"

    elif row["Sharpe Ratio"] < 0:
        return "Avoid"

    else:
        return "Moderate"


performance["Recommendation"] = performance.apply(
    recommend,
    axis=1
)

performance.to_csv(
    processed / "fund_recommendations.csv",
    index=False
)

print(
    performance[
        [
            "amfi_code",
            "Recommendation"
        ]
    ].head()
)

print("\nRecommendations generated successfully.")