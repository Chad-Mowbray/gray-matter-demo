import pandas as pd
import argparse
from processor.Analyzer import Analyzer
from processor.Reader import Reader
from processor.Cleaner import Cleaner
from processor.ColumnRemover import ColumnRemover
from processor.Writer import Writer
import logging

logging.basicConfig(
    level=logging.DEBUG, format="'%(asctime)s - %(levelname)s - %(message)s"
)


class Main:
    def __init__(
        self, data_loc, remove_useless_cols, fill_strategy, output_dir, output_fmt
    ):
        self.data_loc = data_loc
        self.remove_useless_cols = remove_useless_cols
        self.fill_strategy = fill_strategy
        self.output_dir = output_dir
        self.output_fmt = output_fmt
        self.writer = Writer(self.output_dir)
        self.groups = ["payment_type", "year", "month"]

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

    def analyze(self, analyzer, group):
        df = analyzer.group_by(group)
        return df

    def main(self):
        df = self.initial_processing()
        a = Analyzer(df)
        for group in self.groups:
            output_df = self.analyze(a, group)
            self.writer.write(output_df, group, self.output_fmt)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Presents summary statistics")
    parser.add_argument("-data_source", help="path to source data", required=True)
    parser.add_argument("-data_dest", help="path to output data dir", required=True)
    parser.add_argument(
        "-output_format",
        help="Format of output dataframes (csv, parquet)",
        choices=["csv", "parquet"],
        required=True,
    )
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
    data_dest = args.data_dest
    output_format = args.output_format
    remove_useless_cols = args.remove_useless_cols
    fill_strategy = args.fill_strategy
    logging.info(
        f"Running with -data_source {data_source} -data_dest {data_dest} -output_format {output_format} -remove_useless_cols {remove_useless_cols} -fill_strategy {fill_strategy}"
    )

    m = Main(data_source, remove_useless_cols, fill_strategy, data_dest, output_format)
    m.main()
