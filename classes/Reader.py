import pandas as pd


class Reader:
    """
    Class to produce a DF from an input source
    """

    def __init__(self, data_dir):
        self.data_dir = data_dir

    def reader(self):
        print(pd.read_parquet(self.data_dir).columns)
        return pd.read_parquet(self.data_dir)
