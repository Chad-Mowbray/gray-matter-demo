import logging

logger = logging.getLogger(__name__)


class Cleaner:
    """
    Class to clean and transform a dataframe
    """

    def __init__(self, raw_df, fill_strategy):
        self.df = raw_df
        self.fill_strategy = fill_strategy

    def handle_null_rows(self):
        logger.info(f"Applying null fill strategy '{self.fill_strategy}'")
        if self.fill_strategy == "remove":
            self.drop_rows_with_null_values()
        elif self.fill_strategy == "mean":
            self.replace_null_values_with_mean()

    def drop_rows_with_null_values(self):
        # excluding airport_fee since that would remove almost everything
        exclude_airport_fee = [c for c in self.df if c != "airport_fee"]
        self.df = self.df.dropna(subset=exclude_airport_fee)

    def replace_null_values_with_mean(self):
        self.df = self.df.apply(lambda c: c.fillna(c.mean()), axis=0)

    # TODO: Drop rows where sum of costs greater than fare_amount
