import pandas as pd
from loading_data import loading_data

def data_preprocess():
    data = loading_data()
    print(data)
    return data

data_preprocess()
