import pandas as pd


class Cleaner:
    def __init__(self, raw_df):
        self.raw_df = raw_df

    def remove_null_rows(self):
        self.raw_df = self.raw_df.dropna()
        return self.raw_df
