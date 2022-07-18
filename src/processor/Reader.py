import pandas as pd
import logging

logger = logging.getLogger(__name__)


class Reader:
    """
    Class to read in a parquet file and output a dataframe
    """

    def __init__(self, data_dir):
        self.data_dir = data_dir

    def reader(self):
        logger.info("Reading in source file")
        return pd.read_parquet(self.data_dir)
