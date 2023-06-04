import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import csv
import scipy as sp

def read_data(file_path):

    with open(file_path) as f:
        reader = csv.reader(f)
        data = []
        for column in reader:
            column[0] = column[0].replace('(', '').replace("'" , '')
            column[2] = column[2].replace(')', '').replace("'" , '')
            column[1] = column[1].replace("'" , '')
            column[0] = float(column[0])
            column[1] = float(column[1])
            column[2] = float(column[2])
            data.append(column)
            print(data)
        data = np.array(data)
    return data
