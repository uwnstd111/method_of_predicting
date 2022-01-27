import pandas as pd
import math
import statistics
import numpy as np


def ret_log_values(df):
    x = np.arange(1, len(df) + 1)
    y = np.array(df)
    y_prog = []

    result = np.polyfit(np.log(x), y, 1)

    for item in x:
        y_prog.append(result[0] * np.log(item) + result[1])

    return y_prog


def ret_coef_of_variation_log(df):
    data = df
    x = ret_log_values(data)
    y = data
    ssod = 0
    for index, item in enumerate(y):
        ssod += pow(x[index] - item, 2)

    mean = statistics.mean(df)
    # standardError = sem(df)
    # coef_of_variation = "{:.3%}".format(standardError / mean)
    coef_of_variation = math.sqrt(ssod / (len(df) - 2)) / 100
    print("S(y)log" + str(coef_of_variation / 100))
    prog_error = "{:.3%}".format(coef_of_variation / mean * 100)
    return prog_error


def ret_log_points(df):
    x = np.arange(1, len(df) + 1)
    y = np.array(df)
    result_list = []

    result = np.polyfit(np.log(x), y, 1)

    lenght = len(df)
    result_list.append(format(result[0] * np.log(lenght + 1) + result[1], '.3f'))
    result_list.append(format(result[0] * np.log(lenght + 2) + result[1], '.3f'))

    return result_list


def ret_coef_of_determination_log(df):
    x = df
    t = np.arange(1, len(x) + 1)

    x_values = x
    y_values = np.log(t)

    correlation_matrix = np.corrcoef(x_values, y_values)
    correlation_xy = correlation_matrix[0, 1]
    r_squared = correlation_xy ** 2
    return format(r_squared, '.3f')