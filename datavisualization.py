import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocessing import data_preprocess

def data_visualization():

    data = data_preprocess()
    col=list(data.columns)
    col.remove("Extracurricular Activities")
    print(col)
    for i in col:
        plt.figure(figsize=(10,8))
        sns.boxplot(y=i,data=data)
    plt.show()
    for i in col:
        plt.figure(figsize=(10,8))
        sns.distplot(x=data[i])
        plt.title(i)
    plt.show()
    return data

data_visualization()
