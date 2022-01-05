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
