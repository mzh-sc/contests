import unittest

import src.dasci.data.explore as expl
import pandas as pd

class TestExplore(unittest.TestCase):
    def test_missing_values_info(self):
        df = pd.DataFrame(data=[['A', 1], ['B', 2]])
        print(expl.missing_values_info(df))
        