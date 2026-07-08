import os
import pandas as pd

# Project root folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Read raw NAV file
df = pd.read_csv(os.path.join(BASE_DIR, "data", "raw", "02_nav_history.csv"))

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.dropna()

# Save cleaned file
output_path = os.path.join(BASE_DIR, "data", "processed", "clean_nav.csv")
df.to_csv(output_path, index=False)

print("NAV data cleaned successfully.")