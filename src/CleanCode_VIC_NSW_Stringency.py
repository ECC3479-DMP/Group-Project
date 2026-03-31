import pandas as pd
from pathlib import Path

# Paths
raw_path = Path("data/raw/OxCGRT_compact_subnational_v1.csv")
out_path = Path("data/clean/vic_nsw_state_stringency_monthly_firstday.csv")

# Load raw data
df = pd.read_csv(raw_path)

# --- 1. Filter to VIC + NSW STATE_TOTAL ---
state_df = df[
    (df["Jurisdiction"] == "STATE_TOTAL") &
    (df["RegionName"].isin(["Victoria", "New South Wales"]))
].copy()

# --- 2. Convert Date column to datetime ---
state_df["Date"] = pd.to_datetime(state_df["Date"], format="%Y%m%d")

# --- 3. Keep only the first day of each month ---
monthly_df = state_df[state_df["Date"].dt.day == 1]

# --- 4. Keep only required columns ---
keep_cols = [
    "Date",
    "RegionCode",              # AUS_VIC or AUS_NSW
    "Jurisdiction",            # STATE_TOTAL
    "StringencyIndex_Average"
]

clean_df = monthly_df[keep_cols].copy()

# --- 5. Save output ---
clean_df.to_csv(out_path, index=False)

print("Saved:", out_path)
