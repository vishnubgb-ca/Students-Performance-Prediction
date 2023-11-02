import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocessing import data_preprocess
import plotly.figure_factory as ff
import plotly.express as px

def data_visualization():

    data = data_preprocess()
    col=list(data.columns)
    col.remove("Extracurricular Activities")
    print(col)
    for i in col:
        fig = px.box(data, y=i)
        fig.update_layout(plot_bgcolor = "black")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        fig.show()
    for i in col:
        fig = ff.create_distplot([data[i].values],group_labels=[i])
        fig.update_layout(plot_bgcolor = "black")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        fig.show()
    df=data.drop("Extracurricular Activities",axis=1)
    y=df.corr().columns.tolist()
    z=df.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.show()
    return data

data_visualization()
