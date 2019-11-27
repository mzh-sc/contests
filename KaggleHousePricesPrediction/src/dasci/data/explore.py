import pandas as pd
import os.path as path
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
from scipy.stats import norm

def full_path_name(file_name):
    return path.join(path.abspath(''), file_name)

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

def suspicious_columns_info(df: pd.DataFrame, 
        max_unique_values_count=10, 
        min_unique_value_ratio = 0.95):
    suspicious_value_counts = {}
    for col in df.columns:
        col_value_counts = df[col].value_counts()
        if len(col_value_counts) < max_unique_values_count and (col_value_counts / len(df[col]) > min_unique_value_ratio).any():
            suspicious_value_counts[col] = str(col_value_counts.to_dict())
        
    return suspicious_value_counts

def plot_feature_distribution(values):
    sns.distplot(values, fit=norm)
    
    plt.figure()
    stats.probplot(values, plot=plt)
