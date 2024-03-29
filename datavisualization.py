from data_preprocessing import data_preprocess
import pandas as pd
import plotly.express as px
from IPython.display import Image
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.io as pio
import io
from PIL import Image
import string

# a =[]
def data_visualization():
    count = 0
    letters = list(string.ascii_lowercase)
    data = data_preprocess()
    col=list(data.columns)
    col.remove("Extracurricular Activities")
    print(col)
    for i in col:
        count += 1
        fig = px.box(data, y=i)
        fig.update_layout(template='plotly_dark')
        #fig.update_layout(plot_bgcolor = "plotly_dark")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        fig.write_image(f"box_{i}.jpg")
        # a.append(fig)
    for i in col:
        count += 1
        fig = ff.create_distplot([data[i].values],group_labels=[i])
        fig.update_layout(template='plotly_dark')
        #fig.update_layout(plot_bgcolor = "plotly_dark")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        fig.write_image(f"dist_{i}.jpg")
        # a.append(fig)
    df=data.drop("Extracurricular Activities",axis=1)
    y=df.corr().columns.tolist()
    z=df.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.update_layout(template='plotly_dark')
    count += 1
    fig.write_image(f"{letters[count]}_heatmap.jpg")
    # a.append(fig)




    # figures = a
    # image_list = [pio.to_image(fig, format='png', width=1440, height=900, scale=1.5) for fig in figures]
    # for index, image in enumerate(image_list):
    #     with io.BytesIO() as tmp:
    #         tmp.write(image)  # write the image bytes to the io.BytesIO() temporary object
    #         image = Image.open(tmp).convert('RGB')  # convert and overwrite 'image' to prevent creating a new variable
    #         image_list[index] = image  # overwrite byte image data in list, replace with PIL converted image data

    # # pop first item from image_list, use that to access .save(). Then refer back to image_list to append the rest
    # image_list.pop(0).save(r'./Student Performance Prediction#587.pdf', 'PDF',
    #                     save_all=True, append_images=image_list, resolution=100.0)  # TODO improve resolution
    
    return data

data_visualization()
