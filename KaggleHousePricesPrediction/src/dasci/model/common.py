import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import mean_squared_error
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score

def rmse_cv(model, X, y, cv=5):
    scores = cross_val_score(estimator=model, X=X, y=y, cv=5, scoring=make_scorer(mean_squared_error, greater_is_better=False))
    print(np.sqrt(-scores))
    return np.mean(np.sqrt(-scores))

def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

def plot_residual(y_train_pred, y_train_exp, y_test_pred, y_test_exp):
    plt.scatter(y_train_pred, y_train_pred - y_train_exp, c = "blue", marker = "s", label = "Training data")
    plt.scatter(y_test_pred, y_test_pred - y_test_exp, c = "lightgreen", marker = "s", label = "Validation data")
    plt.title("Residuals")
    plt.xlabel("Predicted values")
    plt.ylabel("Residuals")
    plt.legend(loc = "upper left")
    plt.hlines(y = 0, xmin = y_train_pred.min(), xmax = y_train_pred.max(), color = "red")
    plt.show()

def plot_predictions(y_train_pred, y_train_exp, y_test_pred, y_test_exp):
    plt.scatter(y_train_pred, y_train_exp, c = "blue", marker = "s", label = "Training data")
    plt.scatter(y_test_pred, y_test_exp, c = "lightgreen", marker = "s", label = "Validation data")
    plt.title("Predictions")
    plt.xlabel("Predicted values")
    plt.ylabel("Real values")
    plt.legend(loc = "upper left")
    plt.plot([y_train_exp.min(), y_train_exp.max()], [y_train_exp.min(), y_train_exp.max()], c = "red")
    plt.show()

def plot_coef(coefs: pd.Series):
    print(f"Regression picked {sum(coefs != 0)} features and eliminated the other {sum(coefs == 0)} features")
    if len(coefs) > 20:
        important_coefs = pd.concat([coefs.sort_values().head(10),
                         coefs.sort_values().tail(10)])
    else:
        important_coefs = coefs
    important_coefs.plot(kind = "barh")
    plt.title("Coefficients")
    plt.show()

def encode(df: pd.DataFrame):
    categorical_features = df.select_dtypes(include = ["object"]).columns
    if categorical_features.empty:
        return df
        
    numerical_features = df.select_dtypes(exclude = ["object"]).columns
    
    return pd.concat([df[numerical_features], pd.get_dummies(df[categorical_features])], axis=1)