import requests
import pandas as pd
import os

scheme_code = 125497

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

data = response.json()

print("Scheme Name:")
print(data["meta"]["scheme_name"])

nav_df = pd.DataFrame(data["data"])

output_path = "../data/raw/hdfc_top100_live_nav.csv"

nav_df.to_csv(output_path, index=False)

print(f"Saved to {output_path}")

schemes = {
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    filename = f"../data/raw/{name}_nav.csv"

    nav_df.to_csv(filename, index=False)

    print(f"Saved {filename}")