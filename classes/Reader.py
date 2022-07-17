import pandas as pd

class Reader():
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def reader(self):
        return pd.read_parquet(self.data_dir)