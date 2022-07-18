import logging

logger = logging.getLogger(__name__)


class Analyzer:
    """
    Handles analytical operations on a dataframe.
    In this case, grouping the mean of two columns by a third
    """
    
    def __init__(self, df):
        self.df = df
        self.default_terms = ["total_amount", "passenger_count"]

    def group_by(self, group, terms=None):
        terms = terms if terms else self.default_terms
        logger.info(f"Grouping {' and '.join(terms)} by {group}")
        df = self.df.groupby(group)[terms].mean()
        return df
