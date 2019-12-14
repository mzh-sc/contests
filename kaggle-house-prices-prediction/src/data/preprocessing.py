from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin

class DropColumns(BaseEstimator, TransformerMixin):
    import pandas as pd

    def __init__(self, columns_to_drop: list):
        self.columns_to_drop =columns_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X: pd.DataFrame, y=None):
        if not self.columns_to_drop:
            return
        print(f"Drop {self.columns_to_drop} from the dataset.")
        return X.drop(self.columns_to_drop, axis=1)

class SeriesFunctionTransformer(BaseEstimator, TransformerMixin):
    import pandas as pd

    def __init__(self, func):
        self.__func = func

    def fit(self, X, y=None):
        return self

    def transform(self, X: pd.Series, y=None):
        return self.__func(X)

class DataFrameFunctionTransformer(BaseEstimator, TransformerMixin):
    import pandas as pd

    def __init__(self, func):
        self.__func = func

    def fit(self, X, y=None):
        return self

    def transform(self, X: pd.DataFrame, y=None):
        return self.__func(X)