import pandas as pd
from pathlib import Path

# Paths relative to project root - works on any machine
raw_path = Path("data/raw/ABS_Unemployment_rates.xlsx")
out_path = Path("data/clean/unemployment_nsw_vic.csv")

# Ensure output folder exists
out_path.parent.mkdir(parents=True, exist_ok=True)

# Load the sheet, using row 10 as the header (0-indexed = 9)
df = pd.read_excel(raw_path, sheet_name="Data1", header=9)

# Helper to convert Excel column letter to 0-indexed integer
def col_letter_to_index(col):
    result = 0
    for char in col.upper():
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result - 1

# Get 0-based indices for columns A (date), BM (NSW), GI (Victoria)
col_a  = col_letter_to_index("A")
col_bm = col_letter_to_index("BM")
col_gi = col_letter_to_index("GI")

# Select only those columns by position
df_clean = df.iloc[:, [col_a, col_bm, col_gi]]

# Rename columns to something readable
df_clean.columns = ["Date", "NSW_Unemployment_Rate", "VIC_Unemployment_Rate"]

# Convert Date column and filter from Feb 2016 onwards
df_clean["Date"] = pd.to_datetime(df_clean["Date"])
df_clean = df_clean[df_clean["Date"] >= "2016-02-01"]

# Drop rows where all three columns are empty
df_clean = df_clean.dropna(how="all")

# Save to CSV
df_clean.to_csv(out_path, index=False)

print(df_clean.head())
print(f"\nSaved {len(df_clean)} rows to {out_path}")