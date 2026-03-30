# ECC3479-Project-Group
Group Members: Pranaav, Malidu, Dulain


Project Overview

This repository investigates how COVID‑19 policy stringency relates to labour‑market outcomes in Victoria and New South Wales. The project integrates multiple datasets—including government response indices, unemployment rates, and other COVID‑related indicators—and processes them into analysis‑ready formats using a reproducible raw → clean data pipeline.

The repository is structured so that all raw data remains untouched, while all cleaned and merged datasets are generated through Python scripts stored in the  directory. Following the instructions in this README allows anyone to reproduce the final datasets exactly.



Repository Structure 

ECC3479-PROJECT/
│
├── README.md
│
├── data/
│   ├── raw/
│   │   ├── .gitkeep
│   │   ├── NSW_Covid.csv
│   │   ├── Vic_covid.csv
│   │   ├── Victoria_NSW_unemployment_rate.csv
│   │
│   └── clean/
│       ├── .gitkeep
│       ├── oxcgrt_nsw_state_stringency_monthly.csv
│       ├── oxcgrt_vic_state_stringency_monthly.csv
│       ├── merged_stringency_index.csv
│       └── merged_stringency_unemployment.csv
│
└── code/
    ├── merge_stringency.py
    └── merge_stringency_unemployment.py

Folder Purpose
• 	data/raw/
Contains all original datasets exactly as obtained.
These files are never modified.
If a dataset cannot be included due to licensing or size limits, instructions for obtaining it are provided.

• 	data/clean/
Contains all cleaned, transformed, and merged datasets produced by the scripts in .
These files are fully reproducible.
• 	code/
Contains Python scripts that transform raw data into cleaned datasets.
Running these scripts in order will regenerate all files in .

-------------------------------------------------------

How to Run the Project From Scratch
1. Install Required Software
This project uses Python 3.10+.
Install required packages:
pip install pandas


2. Ensure Raw Data Is in Place
Place the following files in data/raw/:
- Victoria_NSW_unemployment_rate.csv
- NSW_Covid.csv
- Vic_covid.csv


Raw data must remain unchanged.


3. Run the Scripts in Order
The scripts must be executed in the following sequence:
- CleanCode_NSW_Lockdown.py
- CleanCode_Vic_Lockdown.py
- NSW,VIC,Lockdown_Merge.py
- Unemployment_Stringency_Merge.py


Data Codebook
merged_stringency_index.csv
- Date
- Vic_stringency : index out of 100 (Severity of Covid Policies) for Victoria
- NSW_stringency : index out of 100 (Severity of Covid Policies) for NSW

merged_stringency_unemployment.csv
- Date
- Vic_stringency : index out of 100 (Severity of Covid Policies) for Victoria
- NSW_stringency : index out of 100 (Severity of Covid Policies) for NSW
- Vic_unemployment : Unemployment Rate - Victoria
- NSW_unemployment : Unemployment Rate - Victoria

oxcgrt_vic_state_stringency_monthly.csv 
oxcgrt_nsw_state_stringency_monthly.csv 
- CountryName
- CountryCode : Australia becomes 'AUS' 
- RegionName  : States 
- RegionCode  : e.g for victoria : Greater_Melbourne, Victoria_rest, Victoria
- Jurisdiction
- Date
- StringencyIndex_Average



Script Descriptions
CleanCode_NSW_Lockdown.py
- Only gets data for Victoria, STATE_TOTAL
- Only gets data for first of every month, for montly data
- Only Keeps CountryName,CountryCode,RegionName,RegionCode,Jurisdiction,Date,StringencyIndex_Average

CleanCode_Vic_Lockdown.py
- Only gets data for Victoria, STATE_TOTAL
- Only gets data for first of every month, for montly data
- Only Keeps CountryName,CountryCode,RegionName,RegionCode,Jurisdiction,Date,StringencyIndex_Average

merge_stringency.py
- Loads VIC and NSW stringency datasets.
- Merges them on the Date column.
- Outputs merged_stringency_index.csv.

merge_stringency_unemployment.py
- Loads unemployment dataset from data/raw/.
- Converts dates from "Aug-2024" to "2024-08-01".
- Merges with stringency dataset using a left join.
- Fills missing stringency values with 0.
- Outputs merged_stringency_unemployment.csv.

Reproducibility Guarantee
If the raw datasets are placed correctly and the required Python packages are installed, running the scripts in the order listed will regenerate all cleaned datasets exactly as submitted.
