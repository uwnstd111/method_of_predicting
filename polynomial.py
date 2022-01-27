import math
import statistics
import numpy as np

def ret_poly_values(df):
    x = np.arange(1, len(df) + 1)
    y = np.array(df)
    y_prog = []

    result = np.polyfit(x, y, 2)

    for item in x:
        y_prog.append(result[0] * pow(item, 2) + result[1] * item + result[2])

    return y_prog


def ret_coef_of_variation_poly(df):
    data = df
    x = ret_poly_values(df)
    resid = 0

    # resid ss
    for index, item in enumerate(data):
        resid += pow(x[index] - item, 2)

    mean = statistics.mean(data)
    coef_of_variation = math.sqrt(resid / (len(df) - 2))
    prog_error = "{:.3%}".format(coef_of_variation / mean)
    return prog_error


def ret_poly_points(df):
    x = np.arange(1, len(df) + 1)
    y = np.array(df)
    result_list = []

    result = np.polyfit(x, y, 2)

    length = len(df)
    result_list.append(format(result[0] * pow(length + 1, 2) + result[1] * (length + 1) + result[2], '.3f'))
    result_list.append(format(result[0] * pow(length + 2, 2) + result[1] * (length + 2) + result[2], '.3f'))

    return result_list


def ret_coef_of_determination_poly(df):
    x = df
    x_mean = statistics.mean(df)
    y = ret_poly_values(x)
    SSE = 0
    SST = 0
    for index, item in enumerate(y):
        SSE += pow(x[index] - item, 2)

    for item in x:
        SST += pow(item - x_mean , 2)

    r_squared = 1 - SSE / SST

    return format(r_squared, '.3f')