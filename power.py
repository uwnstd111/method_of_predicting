import pandas as pd
import math
import statistics
import numpy as np


def linregPower(X, Y):
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


def ret_model_values_Power(x, y):
    result = []
    a, b = linregPower(y, x)
    for index, item in enumerate(x):
         result.append(a * np.log(index + 1) + b)
    return result


def ret_power_parameters(x, y):
    a, b = linregPower(y, x)
    return a, b


def ret_power_values(df):
    x = df
    t = np.arange(1, len(x) + 1)
    ln_y = []
    ln_t = []
    y_prog = []
    for item in x:
        ln_y.append(np.log(item))
    for item in t:
        ln_t.append(np.log(item))

    ln_y_pred = ret_model_values_Power(ln_y, ln_t)
    for item in ln_y_pred:
        y_prog.append(np.exp(item))

    return y_prog


def ret_coef_of_variation_power(df):
    data = np.log(df)
    x = np.log(ret_power_values(df))
    resid = 0

    # resid ss
    for index, item in enumerate(data):
        resid += pow(x[index] - item, 2)

    mean = statistics.mean(data)
    coef_of_variation = math.sqrt(resid / (len(df) - 2))
    print("S(y)power" + str(coef_of_variation / 100))
    prog_error = "{:.3%}".format(coef_of_variation / mean)
    return prog_error


def retPointPrognosis_Power(df):
    x = df
    t = np.arange(1, len(x) + 1)
    ln_y = []
    ln_t = []
    for item in x:
        ln_y.append(np.log(item))
    for item in t:
        ln_t.append(np.log(item))

    a, b = ret_power_parameters(ln_y, ln_t)
    result = []
    lenght = len(x)
    result.append(a * np.log(lenght + 1) + b)
    result.append(a * np.log(lenght + 2) + b)
    r = list(np.exp(result))
    res = []
    for item in r:
        text = format(item, '.3f')
        res.append(text)
    return res


def ret_coef_of_determination_power(df, timeSeries):
    x_values = np.log(df)
    t = np.arange(1, len(timeSeries) + 1)
    y_values = np.log(t)

    correlation_matrix = np.corrcoef(x_values, y_values)
    correlation_xy = correlation_matrix[0, 1]
    r_squared = correlation_xy ** 2
    return format(r_squared, '.3f')