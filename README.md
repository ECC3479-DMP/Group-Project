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
│   │   ├── Hours worked COVID.csv
│   │   ├── Mortality Jan 2020-Jul 2021.csv
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


If any file is missing, download it from the source listed in your assignment instructions or LMS.
Raw data must remain unchanged.
3. Run the Scripts in Order
The scripts must be executed in the following sequence:
- merge_stringency.py
- Reads VIC and NSW stringency files from data/clean/
- Produces merged_stringency_index.csv
- merge_stringency_unemployment.py
- Reads unemployment data from data/raw/
- Reads merged stringency from data/clean/
- Produces merged_stringency_unemployment.csv
After running both scripts, the data/clean/ folder will contain all analysis‑ready datasets.

Manual Steps Required
Some steps occur outside the code:
- Download raw datasets from their official sources (ABS, OxCGRT, etc.).
- Place them into data/raw/ before running any scripts.
- Ensure the OxCGRT monthly stringency files for VIC and NSW are placed in data/clean/ before running the first script.
These steps are necessary because some datasets cannot be redistributed due to licensing restrictions.

Data Codebook
merged_stringency_index.csv
|  |  | 
|  |  | 
|  |  | 
|  |  | 


merged_stringency_unemployment.csv
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 



Script Descriptions
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
