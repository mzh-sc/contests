import pandas as pd
import src.data.pandas_transforms as tr

from sklearn.pipeline import Pipeline

def encode_categorical_features(df: pd.DataFrame):
    categorical_features = df.select_dtypes(include = ["object"]).columns
    if categorical_features.empty:
        return df
        
    numerical_features = df.select_dtypes(exclude = ["object"]).columns
    
    return pd.concat([df[numerical_features], pd.get_dummies(df[categorical_features])], axis=1)

def create_y_pipeline():
    import numpy as np
    from sklearn_pandas import DataFrameMapper

    return Pipeline(steps=[
        ('normalize_sale_price', DataFrameMapper([
            ('SalePrice', tr.SeriesFunctionTransformer(np.log1p))],
        input_df=True,
        df_out=True,
        default=None))
    ])

def create_X_common_pipeline():
    from sklearn.preprocessing import StandardScaler

    def scale_numerical_features(df):
        from sklearn.preprocessing import StandardScaler

        numerical_features = df.select_dtypes(exclude=['object']).columns
        
        scaler = StandardScaler()
        df.loc[:, numerical_features] = scaler.fit_transform(df.loc[:, numerical_features])
        
        print(f"Scaler scales:\n{[(col, scale) for col, scale in zip(numerical_features, scaler.scale_)]}")
        return df

    return Pipeline(steps=[
        ('scale_numerical_features', tr.DataFrameFunctionTransformer(scale_numerical_features)),
        ('encode_categorical_features', tr.DataFrameFunctionTransformer(encode_categorical_features))
    ])

def create_X_pca_pipeline(n_components):
    def pca(df):
        from sklearn.decomposition import PCA

        pca = PCA(n_components=n_components)
        df = pca.fit_transform(df)

        columns = [f"PC{i}" for i in range(df.shape[1])]
        return pd.DataFrame(df, columns=columns)

    return Pipeline(steps=[
        ('pca', tr.DataFrameFunctionTransformer(pca))
    ])