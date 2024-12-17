import  pandas as pd
import os
def loading_data():
    data = pd.read_csv('./Student_Performance.csv')
    os.system("printenv")
    return data

loading_data()
