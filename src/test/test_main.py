import unittest
import pandas as pd
import sys
from pathlib import Path

sys.path.append("../")
from main import Main


class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        output_path = Path.cwd() / "test_output_data"
        if not output_path.exists():
            output_path.mkdir()

    @classmethod
    def tearDownClass(cls):
        output_path = Path.cwd() / "test_output_data"
        if output_path.exists():
            output_path.rmdir()

    def tearDown(self):
        path = Path.cwd() / "test_output_data"
        for child in path.iterdir():
            if child.is_file():
                child.unlink()
        return super().tearDown()

    def test_by_payment_type_output(self):
        expected = pd.read_parquet("test_input_data/payment_output.parquet")

        m = Main(
            "test_input_data/testDF.parquet",
            True,
            "remove",
            "test_output_data",
            "parquet",
        )
        m.groups = ["payment_type"]
        m.main()

        actual = pd.read_parquet("test_output_data")
        pd.testing.assert_frame_equal(expected, actual)

    def test_by_year_output(self):
        expected = pd.read_parquet("test_input_data/year_output.parquet")

        m = Main(
            "test_input_data/testDF.parquet",
            True,
            "remove",
            "test_output_data",
            "parquet",
        )
        m.groups = ["year"]
        m.main()

        actual = pd.read_parquet("test_output_data")
        pd.testing.assert_frame_equal(expected, actual)

    def test_by_month_output(self):
        expected = pd.read_parquet("test_input_data/month_output.parquet")

        m = Main(
            "test_input_data/testDF.parquet",
            True,
            "remove",
            "test_output_data",
            "parquet",
        )
        m.groups = ["month"]
        m.main()

        actual = pd.read_parquet("test_output_data")
        pd.testing.assert_frame_equal(expected, actual)


if __name__ == "__main__":
    unittest.main()
