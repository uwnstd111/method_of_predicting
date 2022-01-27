from scipy.stats import *
import numpy as np
import pandas as pd
import math
import statistics
import matplotlib.pyplot as plt
import statsmodels.api as sm


def ret_coef_of_variation_linest(df, timeSeries):
    print(len(df))
    if len(df) > len(timeSeries):
        df = df[:-2]
    data = df
    x = ret_model_values(data, timeSeries)

    y = data
    if len(y) > len(timeSeries):
        y = y[:-2]
    print(len(y))
    print(len(x))
    ssod = 0
    for index, item in enumerate(y):
        ssod += pow(x[index] - item, 2)

    mean = statistics.mean(df)
    # standardError = sem(df)
    #coef_of_variation = "{:.3%}".format(standardError / mean)
    coef_of_variation = math.sqrt(ssod / (len(df) - 2)) / 100
    print("S(y)lin" + str(coef_of_variation / 100))
    prog_error = "{:.3%}".format(coef_of_variation / mean * 100)
    return prog_error


def retCriticalTValue(df, alpha, deg_free):
    cr_v = t.ppf(q=alpha / 2, df = len(df) - deg_free)
    return math.fabs(cr_v)


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
    return format(r_squared, '.3f')


def ret_model_values(df, timeSeries):
    if len(df) > len(timeSeries):
        df = df[:-2]
    result = []
    x = df

    a, b = linreg(range(len(x)), x)

    for index, item in enumerate(df):
        result.append(a * index + b)

    return result

