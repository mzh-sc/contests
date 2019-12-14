import matplotlib.pyplot as plt
import seaborn as sns

def plot_feature_distribution(values):
    from scipy import stats
    from scipy.stats import norm

    sns.distplot(values, fit=norm)
    
    plt.figure()
    stats.probplot(values, plot=plt)