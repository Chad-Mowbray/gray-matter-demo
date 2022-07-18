import unittest
import pandas as pd
import sys
from pathlib import Path

# sys.path.append("../")
from processor.Analyzer import Analyzer


class TestMain(unittest.TestCase):
    def test_analyzer_groups_properly(self):
        d = {
            "category": ["a", "b", "c", "c"],
            "price": [3, 4, 50, 100],
            "owner": [6, 7, 8, 8],
        }
        df = pd.DataFrame(data=d)

        a = Analyzer(df)
        a.default_terms = ["category", "price"]
        actual = a.group_by("owner")

        e = {
            "price": [3.0, 4.0, 75.0],
            "owner": [6, 7, 8],
        }
        expected = pd.DataFrame(data=e)
        expected.set_index("owner", inplace=True)
        pd.testing.assert_frame_equal(expected, actual)


if __name__ == "__main__":
    unittest.main()
