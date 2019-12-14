import unittest

import src.data.explore as expl
import pandas as pd

from tabulate import tabulate

class TestExplore(unittest.TestCase):
    def test_missing_values_info(self):
        df = pd.DataFrame(data=[['A', 1], ['B', 2]], columns=['C1', 'C2'])
        print(tabulate(df, headers=df.columns))
        print(tabulate(expl.missing_values_info(df)))
        