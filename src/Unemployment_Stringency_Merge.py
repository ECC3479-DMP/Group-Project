import pandas as pd

# -----------------------------
# File paths
# -----------------------------
unemployment_path = "data/clean/unemployment_nsw_vic.csv"
stringency_path = "data/clean/vic_nsw_stringency_pivot.csv"
output_path = "data/clean/merged_stringency_unemployment.csv"

# -----------------------------
# Load datasets
# -----------------------------
unemp = pd.read_csv(unemployment_path)
stringency = pd.read_csv(stringency_path)

# -----------------------------
# Ensure Date is parsed
# -----------------------------
unemp["Date"] = pd.to_datetime(unemp["Date"])
stringency["Date"] = pd.to_datetime(stringency["Date"])

# -----------------------------
# Merge unemployment (full timeline)
# with stringency (shorter timeline)
# -----------------------------
merged = pd.merge(
    unemp,
    stringency,
    on="Date",
    how="left"   # keep all unemployment rows
)

# -----------------------------
# Fill missing stringency values with 0
# -----------------------------
merged["StringencyIndex_Average_VIC"] = merged["StringencyIndex_Average_VIC"].fillna(0)
merged["StringencyIndex_Average_NSW"] = merged["StringencyIndex_Average_NSW"].fillna(0)

# -----------------------------
# Rename columns to final format
# -----------------------------
merged = merged.rename(columns={
    "StringencyIndex_Average_VIC": "VIC_Stringency",
    "StringencyIndex_Average_NSW": "NSW_Stringency",
    "VIC_Unemployment_Rate": "VIC_Unemployment",
    "NSW_Unemployment_Rate": "NSW_Unemployment"
})

# -----------------------------
# Reorder columns
# -----------------------------
merged = merged[[
    "Date",
    "VIC_Stringency",
    "NSW_Stringency",
    "VIC_Unemployment",
    "NSW_Unemployment"
]]

# -----------------------------
# Save final merged file
# -----------------------------
merged.to_csv(output_path, index=False)
