from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn_pandas import DataFrameMapper, FunctionTransformer, gen_features
from functools import partial

import src.data.pandas_transforms as tr
import pandas as pd

def create_preprocessing_pipeline() -> Pipeline:
    def impute_garage_yr_blt(X, y):
        X.loc[X['GarageYrBlt'].isnull(), ['GarageYrBlt']] = X.loc[X['GarageYrBlt'].isnull(), 'YearBuilt']
        return X

    pipeline = Pipeline(steps=[
            ('drop_id', tr.DropColumns(columns_to_drop=['Id'])), 
            
            ('drop_cols_with_missing_values', tr.DropColumns(
                columns_to_drop=['PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu', 'LotFrontage'])),
            
            ('drop_electrical_rows', tr.DataFrameFunctionTransformer(
                lambda X, y: X.drop(X.loc[X['Electrical'].isnull()].index)
            )),

            ('impute_garage_columns', DataFrameMapper(gen_features(
                columns=[['GarageType'], ['GarageFinish'], ['GarageQual'], ['GarageCond']],
                classes=[{'class': SimpleImputer, 'strategy': 'constant', 'fill_value': 'No'}]),
                input_df=True,
                df_out=True,
                default=None
            )),

            ('impute_garage_yr_blt', tr.DataFrameFunctionTransformer(impute_garage_yr_blt)),

            ('impute_bsmt_columns', DataFrameMapper(gen_features(
                columns=[['BsmtCond'], ['BsmtQual'], ['BsmtExposure'], ['BsmtFinType1'], ['BsmtFinType2']],
                classes=[{'class': SimpleImputer, 'strategy': 'constant', 'fill_value': 'No'}]),
                input_df=True,
                df_out=True,
                default=None
            )),

            ('impute_mas_vnr_type', DataFrameMapper(
                [(['MasVnrType'], SimpleImputer(strategy='constant', fill_value='None'))],
                input_df=True,
                df_out=True,
                default=None
            )),

            ('impute_mas_vnr_area', DataFrameMapper(
                [(['MasVnrArea'], SimpleImputer(strategy='constant', fill_value=0))],
                input_df=True,
                df_out=True,
                default=None
            )),

            # partial == (lambda y: (lambda x: y * x))(i) 
            ('replace_values', DataFrameMapper(
                [(key, tr.SeriesFunctionTransformer(
                    partial(lambda value, col: col.replace(value), value))) for (key, value) in 
                {"MSSubClass" : {20 : "SC20", 30 : "SC30", 40 : "SC40", 45 : "SC45", 
                                 50 : "SC50", 60 : "SC60", 70 : "SC70", 75 : "SC75", 
                                 80 : "SC80", 85 : "SC85", 90 : "SC90", 120 : "SC120", 
                                 150 : "SC150", 160 : "SC160", 180 : "SC180", 190 : "SC190"},
                 "MoSold" : {1 : "Jan", 2 : "Feb", 3 : "Mar", 4 : "Apr", 5 : "May", 6 : "Jun",
                             7 : "Jul", 8 : "Aug", 9 : "Sep", 10 : "Oct", 11 : "Nov", 12 : "Dec"},
                 "BsmtCond" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                 "BsmtExposure" : {"No" : 0, "Mn" : 1, "Av": 2, "Gd" : 3},
                 "BsmtFinType1" : {"No" : 0, "Unf" : 1, "LwQ": 2, "Rec" : 3, "BLQ" : 4, 
                                   "ALQ" : 5, "GLQ" : 6},
                 "BsmtFinType2" : {"No" : 0, "Unf" : 1, "LwQ": 2, "Rec" : 3, "BLQ" : 4, 
                                   "ALQ" : 5, "GLQ" : 6},
                 "BsmtQual" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA": 3, "Gd" : 4, "Ex" : 5},
                 "ExterCond" : {"Po" : 1, "Fa" : 2, "TA": 3, "Gd": 4, "Ex" : 5},
                 "ExterQual" : {"Po" : 1, "Fa" : 2, "TA": 3, "Gd": 4, "Ex" : 5},
                 "Functional" : {"Sal" : 1, "Sev" : 2, "Maj2" : 3, "Maj1" : 4, "Mod": 5, 
                                 "Min2" : 6, "Min1" : 7, "Typ" : 8},
                 "GarageCond" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                 "GarageQual" : {"No" : 0, "Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                 "HeatingQC" : {"Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                 "KitchenQual" : {"Po" : 1, "Fa" : 2, "TA" : 3, "Gd" : 4, "Ex" : 5},
                 "LandSlope" : {"Sev" : 1, "Mod" : 2, "Gtl" : 3},
                 "LotShape" : {"IR3" : 1, "IR2" : 2, "IR1" : 3, "Reg" : 4},
                 "PavedDrive" : {"N" : 0, "P" : 1, "Y" : 2},
                 "Street" : {"Grvl" : 1, "Pave" : 2},
                 "Utilities" : {"ELO" : 1, "NoSeWa" : 2, "NoSewr" : 3, "AllPub" : 4}}.items()],
                input_df=True,
                df_out=True,
                default=None
            )),

            ('drop_suspicious_columns', tr.DropColumns(
                columns_to_drop=['Utilities', 'Street', 'Condition2', 'RoofMatl', 'Heating', 'KitchenAbvGr', 'PoolArea']))
        ])
    return pipeline
