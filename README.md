# Taxi Trip Summary Data

## Requirements
- Get mean/median cost, prices, and passenger counts aggregated by payment type, year, and month
- Results are in csv or parquet
- Runnable locally

## A Note on the Data
 In order to make this runnable locally in a reasonable amount of time (a little over a minute on my older Macbook), I've included the 2021 data in the `src_data` folder.  In production, this would obviously be read in from S3 or similar.  It would be fairly easy to modify the internals of the `Reader.read` method to account for many different scenarios without impacting the rest of the code.

## How to Use
- After cloning the repo locally...
- Ensure that you are using a recent version of Python (Github actions is set up to test the build on Python 3.8, 3.9, and 3.10).
- Activate a virtual environment and install from `requirements.txt`: `pip install -r requirements.txt`
- `cd` into `src`
- From there you can run the unit tests: `python -m unittest` as a sanity check.
- Run the application by passing in the required options on the command line as shown below.

EX:
```bash
python main.py -data_source ../src_data -fill_strategy remove -remove_useless_cols -data_dest ../output_data -output_format parquet
```
NOTE: It is assumed that you are running Python 3.8, 3.9, or 3.10 with all the dependencies installed locally.  Here `python` is aliased to `python3`.
### Explanation of options
- `-data_source` is the relative path to the input parquet files.
- `-fill_strategy` handles null numeric values.  There are two options: `remove` and `mean`.  `remove` drops rows with null values and `mean` fills in the average value for the column.
- `-remove_useless_cols` is a boolean option.  When present, numeric columns that are always 0 are removed.  It's more just to suggest some possible options for cleaning the data.
- `-data_dest` is the relative path where the output dataframes will be saved.
- `-output_format` gives you the option to save the resulting dataframes as either `csv` or `parquet`