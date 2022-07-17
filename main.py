import pandas as pd
import argparse

from classes.Reader import Reader
from classes.Cleaner import Cleaner
from classes.InteractiveReporter import InteractiveReporter

# airport_fee has no values


class Main:
    def __init__(self, data_loc):
        self.data_loc = data_loc

    def main(self):
        r = Reader(data_loc)
        df = r.reader()

        ir = InteractiveReporter(df)
        ir.check_for_useless_numeric_columns()
        ir.report_meaningless_columns()
        df_good_cols = ir.df

        c = Cleaner(df_good_cols)
        clean_df = c.remove_null_rows()
        print(clean_df)


money_cols_excluding_total = [
    "fare_amount",
    "extra",
    "mta_tax",
    "tip_amount",
    "tolls_amount",
    "improvement_surcharge",
    "congestion_surcharge",
    # "airport_fee",
]
total_amount = ["total_amount"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Presents summary statistics")
    parser.add_argument("-data_source", help="path to source data", required=True)
    args = parser.parse_args()

    data_loc = args.data_source
    m = Main(data_loc)
    m.main()
