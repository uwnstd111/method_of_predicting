import pandas as pd
import math
from scipy.stats import *
import statistics
import numpy as np

def linregEXP(X, Y):
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

def ret_model_values_EXP(x):
    result = []
    a, b = linregEXP(range(len(x)), x)
    for index, item in enumerate(x):
         result.append(a * index + b)
    return result

def ret_EXP_parameters(x):
    a, b = linregEXP(range(len(x)), x)
    return a, b

def ret_transfromed_exp_model_to_linear(df):
    x = df
    ln_array = []
    y_pred = []

    series = np.arange(1, len(x) + 1)

    for item in x:
        ln_array.append(np.log(item))

    ln_y_pred = ret_model_values_EXP(ln_array)

    for item in ln_y_pred:
        y_pred.append(np.exp(item))
    print(y_pred)
    return y_pred


def ret_coef_of_variation_exp(df):
    data = np.log(df)
    x = np.log(ret_transfromed_exp_model_to_linear(df))
    resid = 0

    # resid ss
    for index, item in enumerate(data):
        resid += pow(x[index] - item, 2)

    mean = statistics.mean(data)
    coef_of_variation = math.sqrt(resid / (len(df) - 2))
    print("S(y)exp" + str(coef_of_variation / 100))
    prog_error = "{:.3%}".format(coef_of_variation / mean)
    return prog_error


def ret_coef_of_determination_exp(df, timeSeries):
    x_values = np.log(df)
    y_values = timeSeries

    correlation_matrix = np.corrcoef(x_values, y_values)
    correlation_xy = correlation_matrix[0, 1]
    r_squared = correlation_xy ** 2
    return format(r_squared, '.3f')


def retPointPrognosis_EXP(df):
    x = df
    ln_array = []
    for item in x:
        ln_array.append(np.log(item))

    a, b = ret_EXP_parameters(ln_array)
    l = len(x)
    result = []
    result.append(format(np.exp(a * l + b), '.3f'))
    result.append(format(np.exp(a * (l + 1) + b), '.3f'))

    return result
