import logging

logger = logging.getLogger(__name__)


class Analyzer:
    def __init__(self, df):
        self.df = df
        self.default_terms = ["fare_amount", "passenger_count"]

    # avg price and passenger count per payment type
    # avg price and passenger count per year
    # avg price and passenger count per month

    def group_by(self, group, terms=None):
        terms = terms if terms else self.default_terms
        logger.info(f"Grouping {' and '.join(terms)} by {group}")
        df = self.df.groupby(group)[terms].mean()
        return df
