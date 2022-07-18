import pandas as pd
from ..resources.constants import TIME_COLS, PICKUP_TS


class TimeFormatterMixin:
    """
    A mixin used by ColumnRemover to transform
    timestamps into year and month
    """
    
    @staticmethod
    def add_exracted_month_col(df):
        df = df.copy()
        df.loc[:, ["month"]] = pd.DatetimeIndex(df[PICKUP_TS]).month
        return df

    @staticmethod
    def add_extracted_year_col(df):
        df = df.copy()
        df.loc[:, ["year"]] = pd.DatetimeIndex(df[PICKUP_TS]).year
        return df

    @staticmethod
    def remove_original_timestamps(df):
        df = df.drop(columns=TIME_COLS)
        return df
