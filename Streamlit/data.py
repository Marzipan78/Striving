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

    st.plotly_chart(fig)


    #min_v = df.min_max.min()
    #max_v=df.min_max.max()

    #avg_ratings = st.sidebar.slider('Average ratings',min_v,max_v)
    #num_reviews = st.sidebar.slider('Number of Reviews', 0,10000000,2000)
    #num_ratings = st.sidebar.slider('Number of Ratings', 0,1000000,2000) 
    
    # filter data
    #with data:
    #    st.title('Data')
    #    st.markdown("![Data](https://media4.giphy.com/media/xT9C25UNTwfZuk85WP/200.webp?cid=ecf05e47844brv5239cczg9hqo5ernebyirvx4xaua7k2dk8&rid=200.webp&ct=g)")
    #    if st.checkbox('View Data'):
    #        st.subheader('Raw Data')
            
            

    #        st.write(df)
            
     
app()
    

    
       
    