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
