import pandas as pd
from pathlib import Path

# Paths
in_path = Path("data/clean/vic_nsw_state_stringency_monthly_firstday.csv")
out_path = Path("data/clean/vic_nsw_stringency_pivot.csv")

# Load the monthly first-day dataset
df = pd.read_csv(in_path)

# Ensure Date is datetime
df["Date"] = pd.to_datetime(df["Date"])

# Pivot so VIC and NSW become separate columns
pivot_df = df.pivot_table(
    index="Date",
    columns="RegionCode",
    values="StringencyIndex_Average"
).reset_index()

# Rename columns to match your required format
pivot_df = pivot_df.rename(columns={
    "AUS_VIC": "StringencyIndex_Average_VIC",
    "AUS_NSW": "StringencyIndex_Average_NSW"
})

# Save output
pivot_df.to_csv(out_path, index=False)

print("Saved:", out_path)

