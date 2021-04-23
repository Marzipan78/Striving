import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

def app():
    image = st.beta_container()
    data = st.beta_container()

    df = pd.read_csv('Books_universe.csv')

    
    
    
    
    st.sidebar.header('User Input Features')
    
    #sorted_title = df.groupby('title').count().index
    #select_title =[]
    #select_title.append(st.sidebar.selectbox('Title',sorted_title))
    sorted_author = df.groupby('author').count().index
    select_author = []
    select_author.append(st.sidebar.selectbox('Author', sorted_author))

    df = df[(df['author'].isin(select_author))]
    fig = px.pie(df, values=df.avg_ratings, names=df.title,color_discrete_sequence=px.colors.sequential.RdBu)    


            
     
app()
    

    
       
    