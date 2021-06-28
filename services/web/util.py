import numpy as np
import pandas as pd


def fetch_data(faultNumber, position):
    df1 = pd.read_csv("./data/TEP_CaseStudy_Fault_" + str(faultNumber) + "_Pos_" + str(position) + "%.csv")
    df1.set_index(df1.columns[0])
    df1 = df1.drop(columns=[df1.columns[0]])

    df2 = pd.read_csv("./data/TEP_CaseStudy_Fault_" + str(faultNumber) + "_Pos_" + str(position) + "%_LSTM-AE_Output.csv")
    df2.set_index(df2.columns[0])
    df2 = df2.drop(columns=[df2.columns[0]])

    df1 = df1.join(df2["Loss_mae"])
    df1 = df1.join(df2["Threshold"])

    df1["pointType"] = df1.apply(lambda row: _label_point(row), axis=1)

    df2.join(df1["pointType"])

    return df1


def _label_point(row):
    if np.isnan(row.Threshold):
        return "TR"
    if (row["Loss_mae"] >= row["Threshold"]) and (row["faultNumber"] != 0):
        return "TP"
    if (row["Loss_mae"] < row["Threshold"]) and (row["faultNumber"] != 0):
        return "FN"
    if (row["Loss_mae"] >= row["Threshold"]) and (row["faultNumber"] == 0):
        return "FP"
    if (row["Loss_mae"] < row["Threshold"]) and (row["faultNumber"] == 0):
        return "TN"
