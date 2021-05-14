import streamlit as st 

import pandas as pd
import numpy as np

import os 
import joblib
import hashlib 
import emoji 
#Dataviz
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
from PIL import Image


def main():
    """Sedora"""
    st.title("Sedora")
    st.subheader("Everything is just a click away! ")

    menu = ["Home","Analysis"]
    #submenu = ["Plot","Prediction"]

    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        st.subheader("Home")
        image = Image.open("download.jpg")
        #emo = emoji.emojize(":smiley:")
        st.image(image,caption=f"Sedora making it possible"  ) 
        st.markdown("### Why Sedora?")
        st.markdown(" We are not just your average E-commerce site! You would like to know who you are getting in bed with, we understand ;)")
        st.markdown(" On the surface we look like any other onlin shopping platform however we implement state of the art Data Analysis and Predictive models. We utilize this in order to identify Sales and to identify trends prior to them actually happening!")
        st.markdown(" We are a powerhouse in Turkey and we would like to help you to help us to make a global impact. Expand into various ventures as our Model: Magic-Ball is very versatile.")

    
    













if __name__=='__main__':
    main() 