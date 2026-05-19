# ECC3479-Project-Group
Group Members: Pranaav, Malidu, Dulain


Project Overview

This repository investigates the effect of COVID-19 policy stringency on the unemployment rates in Victoria and New South Wales. The project integrates multiple datasets - including government response indices, unemployment rates, and other COVID-related indicators - and processes them into analysis-ready formats using a reproducible raw -> clean data pipeline.

The repository is structured so that all raw data remains untouched, while all cleaned and merged datasets are generated through Python scripts stored in the  directory. Following the instructions in this README allows anyone to reproduce the final datasets exactly.

----------------------------------------------------------------------------------------------------

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
│       └── OxCGRT_compact_subnational_v1.csv
│
├── docs/
│   └── .gitkeep
│
├── jupyter/
│   └── EDA.ipynb
│   └── analysis.ipynb
│   └── robustness.ipynb
│    
├── outputs/
│   └── .gitkeep
│
└── src/
    ├── CleanCode_VIC_NSW_Stringency.py
    ├── CleanCode_VIC_NSW_Unemployment_rates.py
    ├── FormatCode_VIC_NSW_Stringency.py
    └── Unemployment_Stringency_Merge.py

----------------------------------------------------------------------------------------------------

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

----------------------------------------------------------------------------------------------------

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

----------------------------------------------------------------------------------------------------

How to Run the Project From Scratch

1. Install Required Software
This project uses Python 3.11+.
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
- Unemployment_Stringency_Merge.py
- EDA.ipynb 
- analysis.ipynb
- robustness.ipynb

*This was to format our target states into columns rather than rows as given in raw data
We chose to do this separately so that we could keep track of errors easier

----------------------------------------------------------------------------------------------------

Data Codebook

-- Explanation on variables of /clean data sets

merged_stringency_unemployment.csv
- Date
- Vic_Stringency : index out of 100 (Severity of Covid Policies) for Victoria
- NSW_Stringency : index out of 100 (Severity of Covid Policies) for NSW
- VIC_Unemployment : Unemployment Rate - Victoria
- NSW_Unemployment : Unemployment Rate - NSW

unemployment_nsw_vic.csv
- Date
- VIC_Unemployment_Rate : Unemployment Rate - Victoria
- NSW_Unemployment_Rate : Unemployment Rate - Victoria

vic_nsw_state_stringency_monthly_firstday.csv 
- Date 
- RegionCode  : e.g. for Victoria: AUS_VIC
- Jurisdiction :  e.g. for Victoria : Greater Melbourne, Rest of Victoria, State Total
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

----------------------------------------------------------------------------------------------------

Script Descriptions

CleanCode_VIC_NSW_Stringency.py
- Load OxCGRT_compact_subnational_v1.csv for data/raw 
- Only gets data for Victoria, NSW , STATE_TOTAL
- Only gets data for first of every month, for montly data
- Only Keeps Date,RegionCode,Jurisdiction,StringencyIndex_Average
- Output File: vic_nsw_state_stringency_monthly_firstday.csv

FormatCode_VIC_NSW_Stringency.py
- Format vic_nsw_state_stringency_monthly_firstday.csv 
- so its in the form, 3 colums: Date,StringencyIndex_Average_NSW,StringencyIndex_Average_VIC
- this is saved into vic_nsw_stringency_pivot.csv

CleanCode_VIC_NSW_Unemployment_rates.py
- Loads 'ABS_Unemployment_rates.xlsx' from data/raw 
- Only get Victoria Unemployment and NSW unemployment data 
- format in the form: Date,NSW_Unemployment_Rate,VIC_Unemployment_Rate
- saved into csv file: unemployment_nsw_vic.csv

Unemployment_Stringency_Merge.py
- Loads vic_nsw_stringency_pivot.csv 
- Loads unemployment_nsw_vic.csv
- Merges with stringency dataset using a left join.
- Fills missing stringency values with 0.
- Outputs merged_stringency_unemployment.csv


Analysis
- DiD used to estimate impact of Victoria’s stricter COVID lockdowns on unemployment vs NSW
- Pre-COVID and acute 2016–2021 model is main causal estimate
- Treatment effect negative but statistically insignificant
- Parallel trends supported
- Validity limited by industry differences, spillovers, and measurement error
- Full analysis in analysis.ipynb

Robustness
 - All robustness checks keep the DiD estimate negative and insignificant.
 - Results stay similar when changing the sample window.
 - Findings consistently show no reliable evidence of a differential unemployment effect.

Final Cleaned Data: 
Unemployment_Stringency_Merge.py


Reproducibility Guarantee
If the raw datasets are placed correctly and the required Python packages are installed, running the scripts in the order listed will regenerate all cleaned datasets exactly as submitted.

--- 
EDA 
The EDA section contains all exploratory data analysis used to understand the behaviour of unemployment and stringency before modelling. 

 - It provides essential checks on data quality, identifies trends, COVID‑driven spikes, and differences between VIC and NSW. 

 - Through time‑seris plots, rolling correlations, scatter plots, lagged relationships, histograms, and DiD visuals, the EDA helps reveal how the variables move over time, where relationships strengthen or weaken, and whether the data aligns with economic expectations. 

 This step is Important because it guides the modelling approach and ensures the dataset is reliable and suitable for causal analysis. 

----
REPORT SUBMISSION 
Table 1: produce by jupyter/analysis.ipynb 

Table 2: produce by jupyter/analysis.ipynb 
        - derived data from our two regression tables: acute model and full model 
        - didn't use the entire table, only got relevant stats for our report

Table 3: produced by jupyter/robustness.ipynb
