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

    def scale_numerical_features(X):
        from sklearn.preprocessing import StandardScaler

        numerical_features = X.select_dtypes(exclude=['object']).columns
        
        scaler = StandardScaler()
        X.loc[:, numerical_features] = scaler.fit_transform(X.loc[:, numerical_features])
        
        print(f"Scaler scales:\n{[(col, scale) for col, scale in zip(numerical_features, scaler.scale_)]}")
        return X

    return Pipeline(steps=[
        ('scale_numerical_features', tr.DataFrameFunctionTransformer(lambda X, y: scale_numerical_features(X))),
        ('encode_categorical_features', tr.DataFrameFunctionTransformer(lambda X, y: encode_categorical_features(X)))
    ])

def create_X_pca_pipeline(n_components):
    def pca(X, y):
        from sklearn.decomposition import PCA

        pca = PCA(n_components=n_components)
        X = pca.fit_transform(X)

        columns = [f"PC{i}" for i in range(X.shape[1])]
        return pd.DataFrame(X, columns=columns)

    return Pipeline(steps=[
        ('pca', tr.DataFrameFunctionTransformer(pca))
    ])

def create_X_correlation_pipeline(target_correlation_threshold, pair_correlation_threshold):
    def correlation(X, y):
        target_col = y.columns[0]

        Xy = pd.concat([X, y], axis=1)
        corr_matrix = Xy.corr()

        potential_features = corr_matrix[corr_matrix[target_col].abs() > target_correlation_threshold]\
            .sort_values(by=[target_col]).index.tolist()
        corr_matrix = corr_matrix.loc[potential_features, potential_features]

        cols_to_remove = set()
        for i, col in enumerate(reversed(potential_features[:-1])):
            col_corr = corr_matrix.iloc[0:len(potential_features)-i-2][col]
            to_remove = col_corr[col_corr.abs() > 0.6].index.tolist()
            if to_remove:
                print(f"{col}: {to_remove}")
                cols_to_remove.update(to_remove)
        print(f"The following columns have a high pairwise correlation and will be removed: {cols_to_remove}")

        potential_features = [e for e in potential_features if e not in cols_to_remove and e != target_col]
        print(f"Selected columns: {potential_features}")
        return X[potential_features]

    return Pipeline(steps=[
        ('correlation', tr.DataFrameFunctionTransformer(correlation))
    ])