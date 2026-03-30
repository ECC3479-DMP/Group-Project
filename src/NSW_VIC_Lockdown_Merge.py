import pandas as pd

# Input file paths
vic_path = "data/clean/oxcgrt_vic_state_stringency_monthly.csv"
nsw_path = "data/clean/oxcgrt_nsw_state_stringency_monthly.csv"

# Output file path
output_path = "data/clean/merged_stringency_index.csv"

# Load datasets
vic = pd.read_csv(vic_path)
nsw = pd.read_csv(nsw_path)

# Select and rename columns
vic = vic[["Date", "StringencyIndex_Average"]].rename(
    columns={"StringencyIndex_Average": "Vic_stringency"}
)
nsw = nsw[["Date", "StringencyIndex_Average"]].rename(
    columns={"StringencyIndex_Average": "NSW_stringency"}
)

# Merge on Date
merged = pd.merge(vic, nsw, on="Date", how="inner")

# Write to file without printing
merged.to_csv(output_path, index=False)
