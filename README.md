# Taxi Trip Summary Data

## Requirements
- Get mean/median cost, prices, and passenger counts aggregated by payment type, year, and month
- Results are in csv or parquet

## How to Use
- After cloning the repo locally, 
- It should run on Python 3.8 and up.
- Activate a virtual environment and install from requirements.txt
- `cd` into `src`
- From there you can run the unit tests: `python -m unittest`
- Run the application passing in the required options on the command line

EX:
```bash
python main.py -data_source ../src_data -fill_strategy remove -remove_useless_cols -data_dest ../output_data -output_format parquet
```