import numpy as np
import pandas as pd
import statistics
import math


def retHoltValues(df):
    x = df
    index = np.arange(0, len(x))
    csv_dataset = pd.DataFrame(x, index)
    optimal_alpha = None
    optimal_gamma = None
    # best_mse = None
    db = csv_dataset.iloc[:, :].values.astype('float32')
    mean_results_for_all_possible_alpha_gamma_values = np.zeros((9, 9))
    for gamma in range(0, 9):
        for alpha in range(0, 9):
            pt = db[0][0]
            bt = db[1][0] - db[0][0]
            mean_for_alpha_gamma = np.zeros(len(db))
            mean_for_alpha_gamma[0] = np.power(db[0][0] - pt, 2)
            for i in range(1, len(db)):
                temp_pt = ((alpha + 1) * 0.1) * db[i][0] + (1 - ((alpha + 1) * 0.1)) * (pt + bt)
                bt = ((gamma + 1) * 0.1) * (temp_pt - pt) + (1 - ((gamma + 1) * 0.1)) * bt
                pt = temp_pt
                mean_for_alpha_gamma[i] = np.power(db[i][0] - pt, 2)
            mean_results_for_all_possible_alpha_gamma_values[gamma][alpha] = np.mean(mean_for_alpha_gamma)
            optimal_gamma, optimal_alpha = np.unravel_index(
                np.argmin(mean_results_for_all_possible_alpha_gamma_values),
                np.shape(mean_results_for_all_possible_alpha_gamma_values))

    optimal_alpha = (optimal_alpha + 1) * 0.1
    optimal_gamma = (optimal_gamma + 1) * 0.1
    # best_mse = np.min(mean_results_for_all_possible_alpha_gamma_values)
    # print("Best MSE = %s" % best_mse)
    # print("Optimal alpha = %s" % optimal_alpha)
    # print("Optimal gamma = %s" % optimal_gamma)

    pt = db[0][0]
    bt = db[1][0] - db[0][0]
    for i in range(1, len(db)):
        temp_pt = optimal_alpha * db[i][0] + (1 - optimal_alpha) * (pt + bt)
        bt = optimal_gamma * (temp_pt - pt) + (1 - optimal_gamma) * bt
        pt = temp_pt
    # print("P_t = %s" % pt)
    # print("b_t = %s" % bt)
    # print("Next observation = %s" % (pt + (1 * bt)))

    forecast = np.zeros(len(db) + 1)
    pt = db[0][0]
    bt = db[1][0] - db[0][0]

    y_prog = [pt + bt]
    for i in range(1, len(db)):
        temp_pt = optimal_alpha * db[i][0] + (1 - optimal_alpha) * (pt + bt)
        bt = optimal_gamma * (temp_pt - pt) + (1 - optimal_gamma) * bt
        pt = temp_pt
        y_prog.append(pt + bt)

    return y_prog[:-1]

def ret_opt_alpha_Holt(df):
    x = df
    index = np.arange(0, len(x))
    csv_dataset = pd.DataFrame(x, index)
    optimal_alpha = None
    optimal_gamma = None
    # best_mse = None
    db = csv_dataset.iloc[:, :].values.astype('float32')
    mean_results_for_all_possible_alpha_gamma_values = np.zeros((9, 9))
    for gamma in range(0, 9):
        for alpha in range(0, 9):
            pt = db[0][0]
            bt = db[1][0] - db[0][0]
            mean_for_alpha_gamma = np.zeros(len(db))
            mean_for_alpha_gamma[0] = np.power(db[0][0] - pt, 2)
            for i in range(1, len(db)):
                temp_pt = ((alpha + 1) * 0.1) * db[i][0] + (1 - ((alpha + 1) * 0.1)) * (pt + bt)
                bt = ((gamma + 1) * 0.1) * (temp_pt - pt) + (1 - ((gamma + 1) * 0.1)) * bt
                pt = temp_pt
                mean_for_alpha_gamma[i] = np.power(db[i][0] - pt, 2)
            mean_results_for_all_possible_alpha_gamma_values[gamma][alpha] = np.mean(mean_for_alpha_gamma)
            optimal_gamma, optimal_alpha = np.unravel_index(
                np.argmin(mean_results_for_all_possible_alpha_gamma_values),
                np.shape(mean_results_for_all_possible_alpha_gamma_values))

    optimal_alpha = (optimal_alpha + 1) * 0.1
    optimal_gamma = (optimal_gamma + 1) * 0.1

    return optimal_alpha, optimal_gamma


def retCalculatedSumOfSquareDifferences_holt(df):
    x = df
    y = retHoltValues(x)
    print(y)
    ssod = 0
    for index, item in enumerate(y):
        ssod += pow((x[index + 1] - item), 2)
        print(ssod)

    return ssod


def ret_coef_of_variation_holt(df):
    return math.sqrt(retCalculatedSumOfSquareDifferences_holt(df) / (len(df) - 1))


def ret_ex_post_error_holt(df):
    return "{:.3%}".format(ret_coef_of_variation_holt(df) / statistics.mean(df))

def retPointPrognosis_Holt(df):
        x = df
        index = np.arange(0, len(x))
        csv_dataset = pd.DataFrame(x, index)
        optimal_alpha = None
        optimal_gamma = None
        # best_mse = None
        db = csv_dataset.iloc[:, :].values.astype('float32')
        mean_results_for_all_possible_alpha_gamma_values = np.zeros((99, 99))
        for gamma in range(0, 9):
            for alpha in range(0, 9):
                pt = db[0][0]
                bt = db[1][0] - db[0][0]
                mean_for_alpha_gamma = np.zeros(len(db))
                mean_for_alpha_gamma[0] = np.power(db[0][0] - pt, 2)
                for i in range(1, len(db)):
                    temp_pt = ((alpha + 1) * 0.1) * db[i][0] + (1 - ((alpha + 1) * 0.1)) * (pt + bt)
                    bt = ((gamma + 1) * 0.1) * (temp_pt - pt) + (1 - ((gamma + 1) * 0.1)) * bt
                    pt = temp_pt
                    mean_for_alpha_gamma[i] = np.power(db[i][0] - pt, 2)
                mean_results_for_all_possible_alpha_gamma_values[gamma][alpha] = np.mean(mean_for_alpha_gamma)
                optimal_gamma, optimal_alpha = np.unravel_index(
                    np.argmin(mean_results_for_all_possible_alpha_gamma_values),
                    np.shape(mean_results_for_all_possible_alpha_gamma_values))

        optimal_alpha = (optimal_alpha + 1) * 0.1
        optimal_gamma = (optimal_gamma + 1) * 0.1
        # best_mse = np.min(mean_results_for_all_possible_alpha_gamma_values)
        # print("Best MSE = %s" % best_mse)
        # print("Optimal alpha = %s" % optimal_alpha)
        # print("Optimal gamma = %s" % optimal_gamma)

        pt = db[0][0]
        bt = db[1][0] - db[0][0]
        for i in range(1, len(db)):
            temp_pt = optimal_alpha * db[i][0] + (1 - optimal_alpha) * (pt + bt)
            bt = optimal_gamma * (temp_pt - pt) + (1 - optimal_gamma) * bt
            pt = temp_pt

        return [pt + (1 * bt), pt + (2 * bt)]