import pandas as pd
import argparse

from classes.Reader import Reader
from classes.Cleaner import Cleaner
from classes.ColumnRemover import ColumnRemover

# airport_fee has no values


class Main:
    def __init__(self, data_loc, remove_useless_cols, fill_strategy):
        self.data_loc = data_loc
        self.remove_useless_cols = remove_useless_cols
        self.fill_strategy = fill_strategy

    def do_read(self):
        r = Reader(self.data_loc)
        df = r.reader()
        return df

    def do_column_removal(self, df):
        cr = ColumnRemover(df, self.remove_useless_cols)
        df = cr.df
        return df

    def do_clean(self, df):
        c = Cleaner(df, self.fill_strategy)
        c.handle_null_rows()
        df = c.df
        return df

    def main(self):
        df = self.do_read()
        df = self.do_column_removal(df)
        df = self.do_clean(df)

        print(df)


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
    parser.add_argument(
        "-remove_useless_cols",
        help="Remove cost-related columns that have no values",
        action="store_true",
    )
    parser.add_argument(
        "-fill_strategy",
        help="How to handle null values in cost-related columns",
        choices=["remove", "mean"],
        required=True,
    )

    args = parser.parse_args()
    data_loc = args.data_source
    remove_useless_cols = args.remove_useless_cols
    fill_strategy = args.fill_strategy

    m = Main(data_loc, remove_useless_cols, fill_strategy)
    m.main()
