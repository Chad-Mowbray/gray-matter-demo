import pandas as pd
import logging

logger = logging.getLogger(__name__)


class Reader:
    """
    Class to produce a DF from an input source
    """

    def __init__(self, data_dir):
        self.data_dir = data_dir

    def reader(self):
        logger.info("Reading in source file")
        return pd.read_parquet(self.data_dir)
