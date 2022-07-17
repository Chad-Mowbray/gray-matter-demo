import pandas as pd
import argparse
from processor.Analyzer import Analyzer
from processor.Reader import Reader
from processor.Cleaner import Cleaner
from processor.ColumnRemover import ColumnRemover
import logging

logging.basicConfig(
    level=logging.DEBUG, format="'%(asctime)s - %(levelname)s - %(message)s"
)


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

    def initial_processing(self):
        df = self.do_read()
        df = self.do_column_removal(df)
        df = self.do_clean(df)
        return df

    def analyze(self, df):
        a = Analyzer(df)
        df = a.group_by("payment_type")
        print(df)
        df = a.group_by("year")
        print(df)
        df = a.group_by("month")
        print(df)

    def main(self):
        df = self.initial_processing()
        # print(df.dtypes)
        self.analyze(df)


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
        help="How to handle null values in cost-related columns (remove, mean)",
        choices=["remove", "mean"],
        required=True,
    )

    args = parser.parse_args()
    data_source = args.data_source
    remove_useless_cols = args.remove_useless_cols
    fill_strategy = args.fill_strategy
    logging.info(
        f"Running with -data_source {data_source} -remove_useless_cols {remove_useless_cols} -fill_strategy {fill_strategy}"
    )

    m = Main(data_source, remove_useless_cols, fill_strategy)
    m.main()
