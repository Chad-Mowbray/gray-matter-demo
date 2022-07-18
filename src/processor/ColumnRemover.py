from .mixins.TimeFormatterMixin import TimeFormatterMixin
from .resources.constants import REQUIRED_COLS
import logging

logger = logging.getLogger(__name__)


class ColumnRemover(TimeFormatterMixin):
    """
    Class to exclude unnecessary columns from the dataframe
    """

    def __init__(self, df, remove_useless_cols):
        self.df = df
        self.useless_columns = []
        self.process()
        if remove_useless_cols:
            self.check_for_useless_numeric_columns()
            self.drop_meaningless_columns()

    def check_for_useless_numeric_columns(self):
        view = self.df.sum(numeric_only=True, axis=0).where(lambda c: c <= 1).dropna()
        self.useless_columns = list(view.to_dict().keys())
        logger.info(
            f"Found {len(self.useless_columns)} useless numeric columns: {self.useless_columns}"
        )

    def drop_meaningless_columns(self):
        if self.useless_columns:
            self.df = self.df.drop(columns=self.useless_columns)

    def process(self):
        df = self.df[REQUIRED_COLS]
        df = self.add_exracted_month_col(df)
        df = self.add_extracted_year_col(df)
        df = self.remove_original_timestamps(df)

        self.df = df
