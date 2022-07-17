import pandas as pd


class TimeFormatterMixin:
    TIME_COLS_DICT = {
        "pickup_ts": "tpep_pickup_datetime",
        "dropoff_ts": "tpep_dropoff_datetime",
    }
    TIME_COLS = list(TIME_COLS_DICT.values())

    @staticmethod
    def add_exracted_month_col(df):
        df["month"] = pd.DatetimeIndex(
            df[TimeFormatterMixin.TIME_COLS_DICT["pickup_ts"]]
        ).month
        return df

    @staticmethod
    def add_extracted_year_col(df):
        df["year"] = pd.DatetimeIndex(
            df[TimeFormatterMixin.TIME_COLS_DICT["pickup_ts"]]
        ).year
        return df

    @staticmethod
    def remove_original_timestamps(df):
        df = df.drop(columns=TimeFormatterMixin.TIME_COLS)
        return df
