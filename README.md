# ECC3479-Project-Group
Group Members: Pranaav, Malidu, Dulain


Project Overview

This repository investigates the effect of COVID-19 policy stringency on the unemployment rates in Victoria and New South Wales. The project integrates multiple datasets - including government response indices, unemployment rates, and other COVID-related indicators - and processes them into analysis-ready formats using a reproducible raw -> clean data pipeline.

The repository is structured so that all raw data remains untouched, while all cleaned and merged datasets are generated through Python scripts stored in the  directory. Following the instructions in this README allows anyone to reproduce the final datasets exactly.



Repository Structure 

ECC3479-PROJECT-GROUP/
│
├── README.md
│
├── data/
│   ├── clean/
│   │   ├── .gitkeep
│   │   ├── merged_stringency_unemployment.csv
│   │   ├── unemployment_nsw_vic.csv
│   │   ├── vic_nsw_state_stringency_monthly_firstday.csv
│   │   └── vic_nsw_stringency_pivot.csv
│   │
│   └── raw/
│       ├── .gitkeep
│       ├── ABS_Unemployment_rates.csv
│       ├── OxCGRT_compact_subnational_v1.csv
│      
│
└── src/
    ├── CleanCode_VIC_NSW_Stringency.py
    ├── CleanCode_VIC_NSW_Unemployment_rates.py
    ├── FormatCode_VIC_NSW_Stringency.py
    └── Unemployment_Stringency_Merge.py



Folder Purpose

• 	data/raw/
Contains all original datasets as obtained from original sources (ABS and Oxford)
These files are never modified.

• 	data/clean/
Contains all cleaned, transformed, and merged datasets produced by the scripts in.
These files are fully reproducible.

• 	src/
Contains Python scripts that transform raw data into cleaned datasets.
Running these scripts in order will regenerate all files in.

-------------------------------------------------------

Manual steps outside of the code

Raw Data: 
  - OxCGRT_compact_subnational_v1.csv 
    - Got from Oxford Covid-19 Government Response Tracker (OxCGRT) github. 
    - https://github.com/OxCGRT/covid-policy-dataset/tree/main/data
    - After accessing this link, download file through this navigation: data/timeseries_indicies/OxCGRT_compact_subnational_v1.csv

  - ABS_unemployment_rates.xlsv
    - Got from ABS, Downloaded excel file with detailed Labour Force Stats for all of australia and its states. 
    - https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia-detailed/latest-release
    - After accessing the above link, scroll until 'Labour force status Monthly (February)' and then download Table 02. Labour force status by state, territory, greater capital city and rest of state (ASGS) and sex



How to Run the Project From Scratch

1. Install Required Software
This project uses Python 3.10+.
Install required packages:
pip install pandas 
pip install openpyxl
(use pip3 for Mac)


2. Ensure Raw Data Is in Place

Place the following files in data/raw/:
- OxCGRT_compact_subnational_v1.csv
- ABS_unemployment_rates.xlsx


Raw data must remain unchanged.


3. Run the Scripts in Order

The scripts must be executed in the following sequence:
- CleanCode_VIC_NSW_Stringency.py
- FormatCode_VIC_ Stringency.py *
- CleanCode_VIC_NSW_Unemployment.py

*This was to format our target states into columns rather than rows as given in raw data
We chose to do this separately so that we could keep track of errors easier

Data Codebook

-- Explanation on variables of /clean data sets

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
- RegionCode  : e.g for victoria: AUS_VIC
- Jurisdiction :  e.g for victoria : Greater Melbourne, Rest of Victoria, State Total
- Date 
- StringencyIndex_Average : index out of 100 (Severity of Covid Policies)

// StringencyIndex_Average is a measure calculated by the Oxford COVID-19 Government Response Tracker (OxCGRT) which summarises how strict government COVID-19 policies were on a given day. 

Although OxCGRT collects many more policy indicators, the Stringency Index is calculated from nine core containment and public-information indicators:

C1: School closing

C2: Workplace closing

C3: Cancel public events

C4: Restrictions on gatherings

C5: Close public transport

C6: Stay-at-home requirements

C7: Restrictions on internal movement

C8: International travel controls

H1: Public information campaigns

Each indicator is converted to a normalised score, and the index is computed as the average of these nine values. This produces the StringencyIndex_Average used in our dataset.

In our project, we convert the daily index into a monthly measure by grouping by year and month and taking the first available value for each month.



Script Descriptions



CleanCode_VIC_NSW_STRINGENCY.py
- Only gets data for Victoria, NSW , STATE_TOTAL
- Only gets data for first of every month, for montly data
- Only Keeps CountryName,CountryCode,RegionName,RegionCode,Jurisdiction,Date,StringencyIndex_Average
- Output File: vic_nsw_state

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


Final Cleaned Data: 
merged_stringency_index.csv

Reproducibility Guarantee
If the raw datasets are placed correctly and the required Python packages are installed, running the scripts in the order listed will regenerate all cleaned datasets exactly as submitted.
