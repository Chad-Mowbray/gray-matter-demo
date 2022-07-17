class InteractiveReporter:

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

    def __init__(self, df):
        self.df = df[self.ALL_COST_COLS]
        self.useless_columns = []

    def check_for_useless_numeric_columns(self):
        view = self.df.sum(numeric_only=True, axis=0).where(lambda x: x <= 1).dropna()
        self.useless_columns = list(view.to_dict().keys())

    def report_meaningless_columns(self, means=input):
        if self.useless_columns:
            resp = means(
                f"The following numeric columns are useless: {self.useless_columns}  Would you like to delete them? (y,n)? "
            )
            if resp == "y":
                self.df = self.df.drop(columns=self.useless_columns)
