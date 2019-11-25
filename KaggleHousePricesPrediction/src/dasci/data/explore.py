import pandas as pd

def missing_values_info(df: pd.DataFrame, max_unique_values_count = 10):
    '''
    Provide information about missing values for each column.
    
    Parameters
    ----------
    df: DataFrame 
    
    Returns
    ----------
    Missing values info.
    '''
    missing_values_count = df.isnull().sum().sort_values(ascending=False)
    missing_values_percentage = (missing_values_count / len(df))
    unique_values_count = df.nunique()
    unique_values = unique_values_count[unique_values_count < max_unique_values_count].index.to_series().map(lambda col: df[col].unique().tolist())

    missing_values = pd.concat([missing_values_count, missing_values_percentage, unique_values_count, unique_values], 
                               axis=1, 
                               keys=['Total', 'Percentage', 'Unique Count', 'Unique values'], 
                               sort=False)
    
    return missing_values[missing_values['Total'] > 0]