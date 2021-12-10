from scipy.stats import *
import numpy as np
import pandas as pd
import math
import statistics
import matplotlib.pyplot as plt

def ret_coef_of_variation(df):
    mean = statistics.mean(df)
    standardError = sem(df)
    coef_of_variation = "{:.3%}".format(standardError / mean)
    return coef_of_variation

def retCriticalTValue(df, alpha):
    cr_v = t.ppf(q = alpha, df = len(df) - 2)
    return cr_v

def linreg(X, Y):
    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in zip(X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x * x
        Syy = Syy + y * y
        Sxy = Sxy + x * y
    det = Sxx * N - Sx * Sx
    return (Sxy * N - Sy * Sx) / det, (Sxx * Sy - Sx * Sxy) / det

def retPointPrognosis(df):
    result = []
    x = df

    a, b = linreg(range(len(x)), x)
    r = a * len(x) + b
    x.append(r)
    result.append(r)

    a, b = linreg(range(len(x)), x)
    r = a * len(x) + b
    x.append(r)
    result.append(r)

    return result

def ret_coef_of_determination(df, timeSeries):
    x_values = df
    y_values = timeSeries

    correlation_matrix = np.corrcoef(x_values, y_values)
    correlation_xy = correlation_matrix[0, 1]
    r_squared = correlation_xy ** 2
    return r_squared
