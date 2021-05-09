import streamlit as st 

import pandas as pd
import numpy as np

import os 
import joblib

import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")

def main():
    """Heart Attack Prediction App"""
    st.title("Heart Attack Prediction App")

    menu = ["Home","Login","SignUp"]
    submenu = ["Plot","Prediction"]

    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        st.subheader("Home")
        st.text("What is Cardiac Arrest")
    
    elif choice == "Login":
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password",type = "password")
        if st.sidebar.checkbox("Login"):
            if password == "12345":
                st.success("Welcome {}".format(username))

                activity = st.selectbox("Activity",submenu)
                if activity == "Plot":
                    st.subheader("Data Viz plot")

                elif activity == "Prediction":
                    st.subheader("Predictive Analysis")


            else:
                st.warning("Incorrect username/password")


    elif choice == "SignUp":
        new_username =st.text_input("Username")
        new_password = st.text_input("Password",type = "password")

        confirm_password = st.text_input("Confirm Password", type = "password")
        if new_password == confirm_password:
            st.success("Password Confirmed")
        else:
            st.warning("Passwords do not match")

        if st.button("Submit"):
            pass 




if __name__=='__main__':
    main() 