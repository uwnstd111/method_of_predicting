import math
import statistics
import numpy as np
import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm
import scipy.stats as sc
import random
from linest import retPointPrognosis


def ret_multreg_values(df, timeSeries, list_of_dep_var):
    if len(df) > len(timeSeries):
        df = df[:-2]
    y = list(df)

    variables = list_of_dep_var
    keys = random.sample(range(0, 256), len(variables) + 1)
    random.shuffle(keys)
    X0 = df
    X0 = list(np.zeros((len(X0),), dtype=int))

    for index, item in enumerate(X0):
        X0[index] = 1
    list_to_zip = []
    list_to_zip.append(X0)
    for item in variables:
        list_to_zip.append(item)

    list_of_X = []
    list_to_zip_final = []
    for index, item in enumerate(list_to_zip):
        temp_list = []
        list_of_X.append(item)
        for sub_item in list_of_X:
            temp_list.append(np.float_(sub_item))
        temp_list.append(retPointPrognosis(list(np.float_(item))))
        result_list = [*temp_list[0], *temp_list[1]]
        list_to_zip_final.append(result_list)
        list_of_X.clear()
        # result_list.clear()

    print("Lista regmult final")
    print(list_to_zip_final)

    X = dict(zip(keys, list_to_zip))
    Y = {'y': df}
    df = pd.DataFrame(X, columns=keys)
    df_y = pd.DataFrame(Y, columns=['y'])
    X_ = df[keys]
    Y_ = df_y['y']
    regr = linear_model.LinearRegression()
    regr.fit(X_, Y_)
    result = []
    y.append(0.0)
    y.append(0.0)

    for index, item in enumerate(y):
        list_to_inject = []
        for zip_index, obj in enumerate(list_to_zip_final):
            list_to_inject.append(list_to_zip_final[zip_index][index])

        p = regr.predict([list_to_inject])
        result.append(p[0])

    return result[:-2], result[len(y) - 2:]


def ret_coef_of_variation_mult_reg(df, timeSeries, list_of_dep_var):
    multData = list_of_dep_var
    data = df

    print("mutlreg_coef_of_var" + str(data))
    x = ret_multreg_values(data, timeSeries, multData)[0]
    y = data
    ssod = 0
    for index, item in enumerate(y):
        ssod += pow(x[index] - item, 2)

    mean = statistics.mean(df)
    # standardError = sem(df)
    # coef_of_variation = "{:.3%}".format(standardError / mean)
    coef_of_variation = math.sqrt(ssod / (len(df) - (len(list_of_dep_var) + 1))) / 100
    print("S(y)multREG" + str(coef_of_variation / 100))
    prog_error = "{:.3%}".format(coef_of_variation / mean * 100)
    return prog_error

def calculate_correlation(df, list_of_dep_var, colNames):
    y = np.array(df)
    variables = list_of_dep_var
    cols = colNames
    names = []

    list_of_corr_values = []
    for item in cols:
        names.append(item)
    names = names[2:]

    for index, item in enumerate(names):
        x = np.array(variables[index])
        x = list(np.float_(x))
        r, p = sc.pearsonr(x, y)
        list_of_corr_values.append("{:.3%}".format(r / 100).strip('%'))
        # list_of_corr_values.append()

    X = dict(zip(names, list_of_corr_values))
    text = str(X).strip('{}')
    text = text.replace('\'', '')
    # bedzie zwracac slownik np.: {X1 : <wartosc>, X2 :  <wartosc2>}
    return text

def ret_coef_of_determination_mult_reg(df, timeSeries, list_of_dep_var):
    x = df
    x_mean = statistics.mean(df)
    y = ret_multreg_values(x, timeSeries, list_of_dep_var)[0]
    SSE = 0
    SST = 0
    for index, item in enumerate(y):
        SSE += pow(x[index] - item, 2)

    for item in x:
        SST += pow(item - x_mean, 2)

    r_squared = 1 - SSE / SST

    return format(r_squared, '.3f')
