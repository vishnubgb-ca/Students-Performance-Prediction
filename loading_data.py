import  pandas as pd

def loading_data():
    data = pd.read_csv('./Student_Performance.csv')
    return data

loading_data()
