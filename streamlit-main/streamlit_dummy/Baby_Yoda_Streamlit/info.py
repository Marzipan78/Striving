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

def app():
    
    st.title(' Dooku Welcomes you to the DARK SIDE')
    st.text('')
    st.text('')
    st.text('')

    data = st.beta_container()
    media = st.beta_container()

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

    with data:
        st.title('Terminate Baby Yoda!!')
        st.markdown("![Data](https://media.giphy.com/media/DeOUbnXkLU6B2/giphy.gif)")
        if st.checkbox('Show Me the Intel!'):
            st.subheader('Which Galaxy hmmm.')
            st.write(galaxies)

    with media:
        with st.beta_expander("• Need to see the map!"):
            st.text('Galaxies')
        
            plt.scatter(x=data_0[:,0],y=data_0[:,1])
            plt.scatter(x=data_1[:,0],y=data_1[:,1])
            plt.scatter(x=data_2[:,0],y=data_2[:,1])
            st.pyplot()
            st.set_option('deprecation.showPyplotGlobalUse', False)

        with st.beta_expander("• Need to narrow i down!"):
            st.text("Get those coordinates")
            st.markdown("![Quick Math](https://media.giphy.com/media/csXqmaigJhqQU/giphy.gif)")
            row = np.where(data_0==max(data_0[:,0]))[0][0]
            coordinates = data_0[row]
            coordinates = [round(el,2) for el in coordinates]
            
        
        #plot galaxy in top
            st.text("There! That's the spot ")
            plt.scatter(data_0[:,0],data_0[:,1],  c= "red", label="0")
            #plot rightmost point in this galaxy
            plt.scatter(coordinates[0], coordinates[1])
            st.pyplot()
            
        with st.beta_expander("• Need to see the map!"):
            st.text('Planet , planet which planet?')
            i_variance = pca.explained_variance_ratio_

            sns.barplot(x=[i for i in range(len(i_variance))], y=i_variance)
            plt.title("PCA")
            st.pyplot()

        with st.beta_expander("• Double Quick Math!"):
            plt.scatter(pca_df.iloc[:,0], pca_df.iloc[:,1],alpha =0.2)
            plt.scatter(pca_df.iloc[:,0].mean(),pca_df.iloc[:,1].mean())
            st.pyplot()

            plt.scatter(pca_df.iloc[:,0], pca_df.iloc[:,1],alpha =0.2)
            plt.scatter(pca_df.iloc[:,0].mean(),pca_df.iloc[:,1].mean())
            
            plt.scatter(solution[0], solution[1],c='purple')
            st.pyplot()
app()  
    