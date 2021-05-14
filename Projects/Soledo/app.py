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

    image = Image.open("download.jpg")
    #emo = emoji.emojize(":smiley:")
    st.image(image,caption=f"Sedora making it possible"  ) ;
    













if __name__=='__main__':
    main() 