import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from feature_engineering import feature_engineering

def data_visualization():

    data = feature_engineering()
    col=list(data.columns)
    col.remove("Extracurricular Activities")
    print(col)
    for i in col:
        plt.figure(figsize=(10,8))
        sns.boxplot(y=i,data=data)
        plt.show()
    return data

data_visualization()
