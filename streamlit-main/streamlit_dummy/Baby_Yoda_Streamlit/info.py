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

def app():
    
    st.title(' WELCOME TO THE DARK SIDE')
    st.text('')
    st.text('')
    st.markdown("![Data](https://media.giphy.com/media/DeOUbnXkLU6B2/giphy.gif)")
    st.text('')

    data = st.beta_container()
    media = st.beta_container()

    galaxies = pd.read_csv('galaxies.csv')
    planets = pd.read_csv('planet.csv')
    points = galaxies.values

    
    
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
        st.title("DOOKU'S PLAN TO CATCH THIS THING !!")
        st.text('')
        st.text('')
        st.markdown("![x](https://media.giphy.com/media/WkOAurEV1T42tCq5VF/giphy.gif)")
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        #if st.checkbox('Show Me the Intel!'):
         #   st.subheader('Which Galaxy hmmm.')
         #   st.write(galaxies)
    
    with media:
        st.markdown("# Dooku's Master Plan Deciphered")
        with st.beta_expander("•Find out which Galaxy that tiny thing is hiding in!"):
            st.markdown('## From the intel collected I suspect he is in one of these 3 Galaxies, but which one?')
            st.text('')
            st.text('')
            st.text('The Galaxies')
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
            
            plt.scatter(x=data_0[:,0],y=data_0[:,1])
            plt.scatter(x=data_1[:,0],y=data_1[:,1])
            plt.scatter(x=data_2[:,0],y=data_2[:,1])
            st.pyplot()
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.markdown('## I got it! I can use the Dark side Power to narrow it down')
        st.text('')
        st.text('')
        with st.beta_expander("•The Power of the Dark Side!"):
            
            st.markdown('### Dark Side KMeans will help me find out the right Galaxy! I can group each planet into one of the three Galaxies')
            st.text('')
            st.text('')
            st.markdown("![Quick Math](https://media.giphy.com/media/csXqmaigJhqQU/giphy.gif)")
            
            st.text('')
            st.markdown('### My Storm Troopers found out that Baby Yoda is in a planet on the far right of the topmost Galaxy')
            st.markdown('### I can use the Mean of all Y co-ordinates to determine which Galaxy is the topmost, there I shall find this ugly creature! ')
            st.text('')
            st.text('')
        st.text('')
        st.text('')
               
        with st.beta_expander("• Behold!"):   
            st.markdown('### The Darkside Power has come through, after some Quick Math we have the co-ordinates!')
            st.text('')
            row = np.where(data_0==max(data_0[:,0]))[0][0]
            coordinates = data_0[row]
            coordinates = [round(el,2) for el in coordinates]
            
            st.markdown( "### There! That's the spot ");  c= tuple(coordinates); c  
            
            plt.scatter(data_0[:,0],data_0[:,1],  c= "red", label="0")
            #plot rightmost point in this galaxy
            plt.scatter(coordinates[0], coordinates[1])
            st.pyplot()

            st.markdown("![x](https://media.giphy.com/media/1yMcPZv165u1znx2GG/giphy.gif)")
        
        
        st.text('')
        st.text('')    
        with st.beta_expander("• Bahhh but which planet??"):
            st.markdown('### Planet , planet which planet?')
            st.text('')
            st.markdown(" ### Way too many things to consider, how can I narrow it down? Only Jedis will be lost here!!")
            st.text('')
            st.markdown(" ### The Darkside Library has me covered, I will use the PCA library to narrow down which two components can best indicate where they may have placed him.")
            st.text('')
            i_variance = pca.explained_variance_ratio_
            st.text('')
            st.text('')
            sns.barplot(x=[i for i in range(len(i_variance))], y=i_variance)
            plt.title("PCA")
            st.pyplot()
        st.text('')
        st.text('')
        with st.beta_expander("• Quick Math!"):
            st.markdown('## Now I use the two biggest bar graphs to map out where that little green turd is.')
            st.text('')
            st.text('')
            plt.scatter(pca_df.iloc[:,0], pca_df.iloc[:,1],alpha =0.2)
            plt.scatter(pca_df.iloc[:,0].mean(),pca_df.iloc[:,1].mean())
            st.pyplot()
            st.text('')
            st.text('')
        st.text('')
        st.text('')    
        with st.beta_expander("• THERE HE IS!!!, the Jedi shall fall!"):
            st.markdown(' ## I use the shortest distance from the centre of the new map in order to locate the exact planet: TATOOINE' )
            st.text('')
            st.text('')
            plt.scatter(pca_df.iloc[:,0], pca_df.iloc[:,1],alpha =0.2)
            plt.scatter(pca_df.iloc[:,0].mean(),pca_df.iloc[:,1].mean())
            
            plt.scatter(solution[0], solution[1],c='purple')
            st.pyplot()
        st.markdown("![x]( https://media.giphy.com/media/gYSGoXTuVYASI/giphy.gif)")
           
app()  
    