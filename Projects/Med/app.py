import streamlit as st 

import pandas as pd
import numpy as np

import os 
import joblib
import hashlib 

#Dataviz
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")

#DB
from managed_db import *

#Password
def generate_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def verify_hashes(password,hashed_text):
    if generate_hashes(password) == hashed_text:
        return hashed_text
    return False

cat_vars  = ['sex','cp','fbs','restecg','exang','slope','ca','thal']
#num_vars  = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
num_vars_wfe = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak','chol_fbs']

gender_dict = {"male":1,"female":0}
feature_dict = {"No":1,"Yes":2}
cp_dict = {"Angina (0)": 0, "Atypical Angina (1)": 1, "Non-Angina (2)":2, "Asympotmatic (3)": 3}
rest_ecg_dict = {"Normal (0)":0, "ST-T (1)": 1, "Hypertrophy (2)": 2}
slope_dict = {"Unsloping (1)":1, "Flat (2)": 2, "Downsloping (3)": 3}
thal_dict = {"Unknown (0)": 0, "Normal (1)":1 , "Defect (2)": 2, "Reversable Defect (3)": 3}

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value 

def get_key(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return key 

def get_feature_value(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value 


#load model
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
    return loaded_model








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
            create_usertable()
            hashed_pswd = generate_hashes(password)
            result = login_user(username,verify_hashes(password,hashed_pswd))
            
            if result:
                st.success("Welcome {}".format(username))

                activity = st.selectbox("Activity",submenu)
                if activity == "Plot":
                    st.subheader("Data Viz plot")
                    df = pd.read_csv("data/augheart.csv")
                    df.drop("Unnamed: 0",axis=1, inplace=True)
                    st.dataframe(df)

                    df['target'].value_counts().plot(kind = 'bar')
                    st.pyplot()

                    if st.checkbox("Area Chart"):
                        all_columns = df.columns.to_list()
                        feat_choices =st.multiselect("Choose a feature",all_columns)
                        new_df = df[feat_choices]
                        st.area_chart(new_df)

                elif activity == "Prediction":
                    st.subheader("Predictive Analysis")

                    age = st.number_input("Age",10,90)
                    sex = st.radio("Sex",tuple(gender_dict.keys()))
                    angina = st.radio("Do You Have Exercise Induced Angina?",tuple(feature_dict.keys()))
                    fbs = st.radio("Is Your Fasting Blood Sugar More Than 120?",tuple(feature_dict.keys()))
                    cp = st.radio("Type Of Chest Pain?",tuple(cp_dict.keys()))
                    rest_ecg = st.radio("What Is Your Resting ECG?",tuple(rest_ecg_dict.keys()))
                    slope = st.radio("What Is Your Heart Rate Slope?",tuple(slope_dict.keys()))
                    thal = st.radio("Status Of Thalasemmia?",tuple(thal_dict.keys()))


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
            create_usertable()
            hashed_new_password = generate_hashes(new_password)
            add_userdata(new_username, hashed_new_password)
            st.success("You have successfully created a new account")
            st.info("Login to get started")





if __name__=='__main__':
    main() 