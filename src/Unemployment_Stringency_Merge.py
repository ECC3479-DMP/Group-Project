import pandas as pd

# -----------------------------
# File paths
# -----------------------------
stringency_path = "data/clean/merged_stringency_index.csv"
unemployment_path = "data/raw/Victoria_NSW_unemployment_rate.csv"
output_path = "data/clean/merged_stringency_unemployment.csv"

# -----------------------------
# Load datasets
# -----------------------------
stringency = pd.read_csv(stringency_path)
unemp = pd.read_csv(unemployment_path)

# -----------------------------
# Convert unemployment dates
# "Aug-2024" -> "2024-08-01"
# -----------------------------
unemp["Date"] = pd.to_datetime(unemp["Date"], format="%b-%Y")
unemp["Date"] = unemp["Date"].dt.strftime("%Y-%m-%d")

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
merged["Vic_stringency"] = merged["Vic_stringency"].fillna(0)
merged["NSW_stringency"] = merged["NSW_stringency"].fillna(0)

# -----------------------------
# Rename unemployment columns
# -----------------------------
merged = merged.rename(columns={
    "VIC_UnemploymentRate": "Vic_unemployment",
    "NSW_UnemploymentRate": "NSW_unemployment"
})

# -----------------------------
# Reorder columns
# -----------------------------
merged = merged[[
    "Date",
    "Vic_stringency",
    "NSW_stringency",
    "Vic_unemployment",
    "NSW_unemployment"
]]

# -----------------------------
# Save final merged file
# -----------------------------
merged.to_csv(output_path, index=False)

