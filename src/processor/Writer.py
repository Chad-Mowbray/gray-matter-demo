import logging
from datetime import datetime
from re import sub
from pathlib import Path


logger = logging.getLogger(__name__)


class Writer:
    """
    Handles writing the final dataframes to either csv or parquet
    """
    
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.path = Path.cwd() / self.output_dir

    @staticmethod
    def generate_filename(by_group, fmt):
        now = datetime.now()
        return sub(r"\s", "_", str(now)) + f"__{by_group}.{fmt}"

    def write(self, df, by_group, fmt):
        filename = self.generate_filename(by_group, fmt)
        logger.info(f"Writing {filename} to {self.output_dir}")

        if fmt == "csv":
            df.to_csv(self.path / filename)
        elif fmt == "parquet":
            df.to_parquet(self.path / filename)
