from sklearn.preprocessing import LabelEncoder

import pandas as pd
import numpy as np
from data_preprocessing import data_preprocess

def feature_engineering():

    data = data_preprocess()
    # print(data)
    le=LabelEncoder()
    data['Extracurricular Activities']=le.fit_transform(data['Extracurricular Activities'])
    data.to_csv("students_performance_prediction.csv")
    return data

feature_engineering()
