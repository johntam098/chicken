import numpy
import pandas as pd

import app.input.constant as c


def read_file(filepath):
    names = [c.YEAR,c.DRAW_NO,c.NO1,c.NO2,c.NO3,c.NO4,c.NO5,c.NO6,c.SPECIAL_NO]
    dataset = pd.read_csv(filepath, skiprows=[0], header=None, names=names)
    dataset[c.YEAR] = dataset[c.YEAR].astype(numpy.int_)
    dataset[c.DRAW_NO] = dataset[c.DRAW_NO].astype(numpy.int_)
    dataset[c.NO1] = dataset[c.NO1].astype(numpy.int_)
    dataset[c.NO2] = dataset[c.NO2].astype(numpy.int_)
    dataset[c.NO3] = dataset[c.NO3].astype(numpy.int_)
    dataset[c.NO4] = dataset[c.NO4].astype(numpy.int_)
    dataset[c.NO5] = dataset[c.NO5].astype(numpy.int_)
    dataset[c.NO6] = dataset[c.NO6].astype(numpy.int_)
    dataset[c.SPECIAL_NO] = dataset[c.SPECIAL_NO].astype(numpy.int_)
    print("sharp = {}".format(dataset.shape))
    print(dataset.head(50))
    return dataset
