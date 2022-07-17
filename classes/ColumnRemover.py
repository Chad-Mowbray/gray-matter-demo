from .TimeFormatterMixin import TimeFormatterMixin


class ColumnRemover(TimeFormatterMixin):
    """
    Class to produce a DF with only the necessary columns
    """

    ALL_COST_COLS = [
        "fare_amount",
        "extra",
        "mta_tax",
        "tip_amount",
        "tolls_amount",
        "improvement_surcharge",
        "congestion_surcharge",
        "airport_fee",
        "total_amount",
    ]

    TIME_COLS = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]

    PASSENGER_COUNT = ["passenger_count"]

    PAYMENT_TYPE = ["payment_type"]

    REQUIRED_COLS = ALL_COST_COLS + TIME_COLS + PASSENGER_COUNT + PAYMENT_TYPE

    def __init__(self, df, remove_useless_cols):
        self.df = df
        self.useless_columns = []
        self.process()
        if remove_useless_cols:
            self.check_for_useless_numeric_columns()
            self.drop_meaningless_columns()

    def check_for_useless_numeric_columns(self):
        view = self.df.sum(numeric_only=True, axis=0).where(lambda x: x <= 1).dropna()
        self.useless_columns = list(view.to_dict().keys())

    def drop_meaningless_columns(self):
        if self.useless_columns:
            self.df = self.df.drop(columns=self.useless_columns)

    def process(self):
        df = self.df[self.REQUIRED_COLS]
        df = self.add_exracted_month_col(df)
        df = self.add_extracted_year_col(df)
        df = self.remove_original_timestamps(df)

        self.df = df
