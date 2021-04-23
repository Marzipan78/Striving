from numpy.core.fromnumeric import size
import streamlit as st
import pandas as pd
from PIL import Image
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import KMeans
import plotly.express as px
from sklearn import model_selection
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.model_selection import KFold, LeaveOneOut, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

galaxies = pd.read_csv('galaxies.csv')
planets = pd.read_csv('planet.csv')
points = galaxies.values

model = KMeans(n_clusters=3)
model = model.fit(points)
labels = model.labels_
def separate_labels(labels, points):
    data_0 = []
    data_1 = []
    data_2 = []

    for i in range(labels.shape[0]):
        if labels[i] == 0:
            data_0.append(points[i])
        elif labels[i] == 1:
            data_1.append(points[i])
        else:
            data_2.append(points[i])    
    return np.array(data_0),np.array(data_1),np.array(data_2)

        

data_0,data_1,data_2 = separate_labels(labels, points)
row = np.where(data_0==max(data_0[:,0]))[0][0]
coordinates = data_0[row]
coordinates = [round(el,2) for el in coordinates]
pca = PCA()

planets_fitted = pca.fit_transform(planets)
pca_df = pd.DataFrame(data = planets_fitted
            )

x_mean=pca_df.iloc[:,0].mean()
y_mean=pca_df.iloc[:,1].mean()
print(x_mean,y_mean)

dist = np.sqrt((pca_df.iloc[:,0]-x_mean)**2 + (pca_df.iloc[:,1]-y_mean)**2)
row_sol = np.where(dist==min(dist))[0][0]

solution = pca_df.iloc[row_sol, :2]