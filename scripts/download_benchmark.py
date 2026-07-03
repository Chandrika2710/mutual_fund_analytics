from pathlib import Path
import yfinance as yf

# Get project root
project_root = Path(__file__).resolve().parent.parent

# Create data/raw folder if it doesn't exist
raw_folder = project_root / "data" / "raw"
raw_folder.mkdir(parents=True, exist_ok=True)

print("Saving files to:", raw_folder)

# Download Nifty 50
nifty50 = yf.download("^NSEI", start="2022-01-01", end="2026-06-01")
nifty50.to_csv(raw_folder / "nifty50.csv")

# Download Nifty 100
nifty100 = yf.download("^CNX100", start="2022-01-01", end="2026-06-01")
nifty100.to_csv(raw_folder / "nifty100.csv")

print("Benchmark data downloaded successfully!")