import streamlit as st
import numpy as np
import pandas as pd


def app():
    st.title('Data')

    st.write("The Data that we built our revolutionary drug!")

    data = st.beta_container()

    st.write(" We have a whole host of variables")

    with data:
        if st.checkbox('Explore Data'):
            df = pd.read_csv('augheart.csv')
            df =df.drop(['Unnamed: 0'], axis = 1 )
            
            st.subheader('People Studied')

    

            st.write(df)
