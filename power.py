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
