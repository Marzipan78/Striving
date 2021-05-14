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
import seaborn as sns
matplotlib.use("Agg")
from PIL import Image

## DS
import time
from IPython.display import display, clear_output

import sklearn
from sklearn import pipeline      # Pipeline
from sklearn import preprocessing # OrdinalEncoder, LabelEncoder
from sklearn import impute
from sklearn import compose
from sklearn import model_selection # train_test_split
from sklearn import metrics         # accuracy_score, balanced_accuracy_score, plot_confusion_matrix
from sklearn import set_config

set_config(display='diagram') # Useful for display the pipeline

# Tree models
from sklearn.ensemble       import RandomForestClassifier
from sklearn.ensemble       import ExtraTreesClassifier
from sklearn.ensemble       import AdaBoostClassifier
from sklearn.ensemble       import GradientBoostingClassifier
from sklearn.experimental   import enable_hist_gradient_boosting # Necesary for HistGradientBoostingClassifier
from sklearn.ensemble       import HistGradientBoostingClassifier
from xgboost                import XGBClassifier
from lightgbm               import LGBMClassifier
#from catboost               import CatBoostClassifier

# Multiplicative models
from sklearn.svm            import SVC
from sklearn.neighbors      import KNeighborsClassifier
from sklearn.linear_model   import LogisticRegression





def main():
    """Sedora"""
    st.title("Sedora")
    st.subheader("Everything is just a click away! ")

    menu = ["Home","Data"]
    submenu = ["Analysis","Magic-Ball"]

    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        st.subheader("Home")
        image = Image.open("download.jpg")
        #emo = emoji.emojize(":smiley:")
        st.image(image,caption=f"Sedora making it possible"  ) 
        st.markdown("### Why Sedora?")
        st.markdown(" We are not just your average E-commerce site! You would like to know who you are getting in bed with, we understand ;)")
        st.markdown(" On the surface we look like any other onlin shopping platform however we implement state of the art Data Analysis and Predictive model. We utilize this in order to identify Sales and to identify trends prior to them actually happening!")
        st.markdown(" We are a powerhouse in Turkey and we would like to help you to help us to make a global impact. Expand into various ventures as our Model: Magic-Ball is very versatile.")

        
    
    elif choice == "Data":

        st.success("Welcome Aboard You Curious Cat")
        activity = st.selectbox("Activity",submenu)
        if activity == "Analysis":
            st.subheader("Data Viz plot")
            df = pd.read_csv("online_shoppers_intention.csv")
            
            #st.dataframe(df)

            st.set_option('deprecation.showPyplotGlobalUse', False)
            df['Revenue'].value_counts().plot(kind = 'bar')
            st.pyplot()

            df.corr()['Revenue'].abs().sort_values().plot.barh()
            st.pyplot()

            st.markdown("Just pulling your leg! As informative these graphs, there are not very intuitive. I would have to come up with code every other time to make a decision. Our partner Graphext has us covered.")
            st.markdown("We are using the state of the Art indepth Analysis in order to Identify key trends over our time in Turkey, we plan to implement the same for every market we enter into. The POWER OF DATA!")
            # INSERT LINK 
            link = '[Deep-Insight](https://public.graphext.com/889ca3f52441c367/index.html?section=insights&id=)'
            st.markdown(link, unsafe_allow_html=True)

        elif activity == "Magic-Ball":
            st.subheader("The Magic")
            df = pd.read_csv("online_shoppers_intention.csv")
            df['VisitorType'] = df['VisitorType'].map({'Other': 0, 'New_Visitor': 1, 'Returning_Visitor': 2})

            df['Month'] = df['Month'].map({'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'June': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12})

            df['SpecialDay'] = df['SpecialDay'] * 10

            df['SpecialDay'] = df['SpecialDay'].astype(int)

            df['Month'] = df['Month'].astype(int)

            df['Weekend'] = df['Weekend'].astype(int)

            df['Revenue'] = df['Revenue'].astype(int)

            cat_vars = ['Administrative', 'Informational', 'ProductRelated', 'Month', 'VisitorType', 'SpecialDay']

            num_vars = ['PageValues', 'ExitRates', 'ProductRelated_Duration', 'BounceRates', 'Administrative_Duration']

            X = df[cat_vars + num_vars]

            y = df['Revenue']
           
            from numpy import mean
            from numpy import std
            from sklearn.datasets import make_classification
            from sklearn.model_selection import cross_val_score
            from sklearn.model_selection import RepeatedStratifiedKFold
            from sklearn.feature_selection import RFECV
            from sklearn.tree import DecisionTreeClassifier
            from sklearn.pipeline import Pipeline
            # define dataset
            # create pipeline
            rfe = RFECV(estimator=DecisionTreeClassifier())
            model = DecisionTreeClassifier()
            pipeline = Pipeline(steps=[('s',rfe),('m',model)])
            # evaluate model
            cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
            n_scores = cross_val_score(pipeline, X, y, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
            # report performance
            st.write('Accuracy: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))
            









if __name__=='__main__':
    main() 