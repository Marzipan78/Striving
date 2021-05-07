import streamlit as st
import pandas as pd
from PIL import Image

def app():
    st.title('Hippocratia')

    st.write('Welcome to the future of Medical Science.')

    st.write('With our revolutionary AI technology we will help you save lives!.')

    image = st.beta_container()

    with image:
        image = Image.open('ai-medical-stock.jpg')
        st.image(image, caption='')
