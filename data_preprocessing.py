import pandas as pd
from data_analysis import data_analysis

def data_preprocess():
    data = data_analysis()
    print(data)
    return data

data_preprocess()
