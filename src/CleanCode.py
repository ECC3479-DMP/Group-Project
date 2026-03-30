import pandas as pd
from pathlib import Path

# Paths relative to project root (NOT src/)
raw_path = Path("data/raw/Vic_covid.csv")
clean_path = Path("data/clean/oxcgrt_vic_state_stringency_monthly.csv")

df = pd.read_csv(raw_path)

df = df[
    (df["RegionName"] == "Victoria") &
    (df["Jurisdiction"] == "STATE_TOTAL")
]

df["Date"] = pd.to_datetime(df["Date"], format="%Y%m%d")

df = df[
    [
        "CountryName",
        "CountryCode",
        "RegionName",
        "RegionCode",
        "Jurisdiction",
        "Date",
        "StringencyIndex_Average"
    ]
]

df_monthly = (
    df.sort_values("Date")
      .groupby([df["Date"].dt.year, df["Date"].dt.month])
      .first()
      .reset_index(drop=True)
)

df_monthly.to_csv(clean_path, index=False)

print("Saved:", clean_path)
