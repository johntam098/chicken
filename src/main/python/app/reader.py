import pandas as pd


def read_file(filepath):
    names = ["YEAR","DRAW_NO","NO1","NO2","NO3","NO4","NO5","NO6","SPECIAL_NO"]
    return pd.read_csv(filepath, skiprows=[0], header=None, names=names)
