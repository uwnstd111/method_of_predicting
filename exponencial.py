import pandas as pd
import math
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

    return y_pred


