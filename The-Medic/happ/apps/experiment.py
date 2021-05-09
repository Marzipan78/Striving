import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import pipeline      # Pipeline
from sklearn import preprocessing # OrdinalEncoder, LabelEncoder
from sklearn import impute
from sklearn import compose
from sklearn import model_selection # train_test_split
from sklearn import metrics         # accuracy_score, balanced_accuracy_score, plot_confusion_matrix
from sklearn import set_config
set_config(display='diagram') 

def app():
    st.title('Try our Model with your own data') 

   
    # Upload CSV data
    with st.header('1. Upload your CSV data'):
        uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
        

    

    # Build lazy model
    #X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size = split_size,random_state = seed_number)

    # Sidebar - Specify parameter settings
    with st.sidebar.header('2. Set Parameters'):
        split_size = st.sidebar.slider('Data split ratio (% for Training Set)', 10, 90, 80, 5)
        seed_number = st.sidebar.slider('Set the random seed number', 1, 100, 42, 1)

    if uploaded_file is not None:
            @st.cache
            def load_csv():
                csv = pd.read_csv(uploaded_file)
                return csv
            df = load_csv()
            #pr = ProfileReport(df, explorative=True)
            st.header('**Input DataFrame**')
            st.write(df)
            st.write('---')
            st.header('**Pandas Profiling Report**')
            #st_profile_report(pr)
                
            
    else:
        st.info('Awaiting for CSV file to be uploaded.')
        if st.button('Press to use Example Dataset'):
            # Example data
            @st.cache
            def load_data():
                a = pd.read_csv('heart.csv')
                
                return a
            df = load_data()
            
            st.header('**Input DataFrame**')
            st.write(df)
            st.write('---')
            
            cat_vars  = ['sex','cp','fbs','restecg','exang','slope','ca','thal']
            num_vars  = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

            num_4_tree = pipeline.Pipeline(steps=[
            ('imputer', impute.SimpleImputer(strategy='mean', add_indicator=False)),])

            cat_4_tree = pipeline.Pipeline(steps=[
                ('imputer', impute.SimpleImputer(strategy='constant',)),
                
            ])

            tree_prepro = compose.ColumnTransformer(transformers=[
                ('num', num_4_tree, num_vars),
                ('cat', cat_4_tree, cat_vars),
            ], remainder='drop')
