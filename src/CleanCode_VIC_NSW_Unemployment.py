import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/ABS_Unemployment_rates.xlsx")
OUTPUT_PATH = Path("data/clean/vic_nsw_unemployment_clean.csv")

def load_abs_unemployment():
    df = pd.read_excel(RAW_PATH, sheet_name="Data1", header=0)
    df.columns = df.columns.astype(str)

    # Identify the date column (first column)
    date_col = df.columns[0]

    # Your actual unemployment rate columns
    VIC_COL = "Victoria ;  Unemployment rate ;  Persons ;"
    NSW_COL = "New South Wales ;  Unemployment rate ;  Persons ;"

    clean_df = pd.DataFrame({
        "date": df[date_col],
        "vic_unemployment": df[VIC_COL],
        "nsw_unemployment": df[NSW_COL]
    })

    clean_df = clean_df.dropna(subset=["vic_unemployment", "nsw_unemployment"])

    return clean_df


def main():
    clean_df = load_abs_unemployment()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    clean_df.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved cleaned unemployment data to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

