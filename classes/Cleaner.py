import pandas as pd


class Cleaner:
    """
    Class to produce a clean DF
    """

    def __init__(self, raw_df, fill_strategy):
        self.df = raw_df
        self.fill_strategy = fill_strategy

    def handle_null_rows(self):
        if self.fill_strategy == "remove":
            self.drop_rows_with_null_values()
        elif self.fill_strategy == "mean":
            self.replace_null_values_with_mean()

    def drop_rows_with_null_values(self):
        # excluding airport_fee since that would remove almost everything
        exclude_airport_fee = [n for n in self.df if n != "airport_fee"]
        self.df = self.df.dropna(subset=exclude_airport_fee)

    def replace_null_values_with_mean(self):
        self.df = self.df.apply(lambda x: x.fillna(x.mean()), axis=0)
