import pandas as pd
import math
import statistics
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.api import SimpleExpSmoothing

def retOptimumAlpha(df, timeSeries):
    #index = pd.date_range(start=str(timeSeries[0]), end=str(timeSeries[len(timeSeries) - 1] + 1), freq='A')
    data = pd.Series(df, timeSeries)
    brownModel = SimpleExpSmoothing(data).fit()
    model_cast = brownModel.forecast(2).rename('alpha=%s'%brownModel.model.params['smoothing_level'])
    # Plot for alpha=Optimized by statsmodel
    return float(brownModel.model.params['smoothing_level'])
    # ax = data.plot(marker='o', color='black', figsize=(12, 8), legend=True)
    # model_cast.plot(marker='*', ax=ax, color='green', legend=True)
    # brownModel.fittedvalues.plot(marker='*', ax=ax, color='green')


def retCalculatedSumOfSquareDifferences(df, timeSeries):
    opt_alpha = float(retOptimumAlpha(df, timeSeries))
    global y_prognosis, Ft_list, delta_Ft_list
    Ft_list, delta_Ft_list = [], []

    y_prognosis = []
    Ft_list.append(float(df[0]))  #start value
    sosd = 0
    #fill the Ft
    for item in df:
        if item != Ft_list[0]:
            Ft_list.append(float(item) * opt_alpha + (1 - opt_alpha) * float(Ft_list[len(Ft_list) - 1]))

    for item in Ft_list:
        delta_Ft_list.append(float(Ft_list[len(delta_Ft_list) + 1] - float(item)))
        if item == Ft_list[len(Ft_list) - 2]:
            break

    for i in range(0, len(df) - 2):
        y_prognosis.append(float(Ft_list[i + 1]) + float(delta_Ft_list[i]))

    for i in range(0, len(y_prognosis)):
        sosd += (df[i + 2] - y_prognosis[i])**2

    print("Ft: " + str(Ft_list))
    print("deltaFt: " + str(delta_Ft_list))
    print("y_prog: " + str(y_prognosis))

    return sosd

def ret_coef_of_variation(df, timeSeries):
    return math.sqrt(retCalculatedSumOfSquareDifferences(df, timeSeries)) / (len(df) - 3)

def ret_ex_post_error(df, timeSeries):
    return "{:.3%}".format(ret_coef_of_variation(df, timeSeries) / statistics.mean(df))

def retPointPrognosis(df, timeSeries):
    resultList = []

    opt_alpha = float(retOptimumAlpha(df, timeSeries))
    global y_prognosis, Ft_list, delta_Ft_list
    Ft_list, delta_Ft_list = [], []

    y_prognosis = []
    Ft_list[0] = float(df[0])
    for item in df:
        if item != Ft_list[0]:
            Ft_list.append(float(item) * opt_alpha + (1 - opt_alpha) * float(Ft_list[len(Ft_list) - 1]))

    for item in Ft_list:
        delta_Ft_list.append(float(Ft_list[len(delta_Ft_list) + 1] - float(item)))
        if item == Ft_list[len(Ft_list) - 2]:
            break

    for i in range(0, len(df - 2)):
        y_prognosis.append(float(Ft_list[i + 1]) + float(delta_Ft_list[i]))

    resultList.append(Ft_list[len(Ft_list) - 1] + delta_Ft_list[len(delta_Ft_list) - 1])
    resultList.append(Ft_list[len(Ft_list) - 1] + 2 * delta_Ft_list[len(delta_Ft_list) - 1])
    # for ex: [100, 104.5]

    return resultList
