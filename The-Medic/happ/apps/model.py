import streamlit as st
import time
from IPython.display import clear_output
import numpy    as np
import pandas   as pd
import seaborn  as sb
import matplotlib.pyplot as plt
import sklearn  as skl
from IPython import display


from sklearn import pipeline      # Pipeline
from sklearn import preprocessing # OrdinalEncoder, LabelEncoder
from sklearn import impute
from sklearn import compose
from sklearn import model_selection # train_test_split
from sklearn import metrics         # accuracy_score, balanced_accuracy_score, plot_confusion_matrix
from sklearn import set_config
set_config(display='diagram') 

from sklearn.linear_model   import LogisticRegression
from sklearn.linear_model   import RidgeClassifier
from sklearn.svm            import SVC
from sklearn.svm            import NuSVC
from sklearn.svm            import LinearSVC
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors      import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.naive_bayes    import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble       import StackingClassifier


from sklearn.tree          import DecisionTreeClassifier
from sklearn.ensemble      import RandomForestClassifier
from sklearn.ensemble      import ExtraTreesClassifier
from sklearn.ensemble      import AdaBoostClassifier
from sklearn.ensemble      import GradientBoostingClassifier
from sklearn.experimental  import enable_hist_gradient_boosting # Necesary for HistGradientBoostingClassifier
from sklearn.ensemble      import HistGradientBoostingClassifier
from xgboost               import XGBClassifier
from lightgbm              import LGBMClassifier
#from catboost              import CatBoostClassifier

def app():
    
    st.title('Models')

    st.write('Welcome, this is where the Medical Magic happens.')

    st.write('The performances of different models on the Sample dataset is presented below.')

    # Load dataset
    full_df = pd.read_csv('augheart.csv')
    
    #iris = datasets.load_iris()
    #X = iris.data
    #Y = iris.target
    # Prepo
    cat_vars  = ['sex','cp','fbs','restecg','exang','slope','ca','thal']
    num_vars  = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    num_vars_wfe = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak','chol_fbs']
    
    num_4_tree = pipeline.Pipeline(steps=[
    ('imputer', impute.SimpleImputer(strategy='mean', add_indicator=False)),
    ])

    cat_4_tree = pipeline.Pipeline(steps=[
    ('imputer', impute.SimpleImputer(strategy='constant')),
        #('onehot', preprocessing.OneHotEncoder(handle_unknown='ignore'))
    ])


    num_4_mult = pipeline.Pipeline(steps=[
    ('imputer', impute.SimpleImputer(strategy='mean', add_indicator=True)), # mean, median
    ('scaler', preprocessing.StandardScaler())
    ])

    cat_4_mult = pipeline.Pipeline(steps=[
    ('imputer', impute.SimpleImputer(strategy='constant')),
        #('onehot', preprocessing.OneHotEncoder(handle_unknown='ignore'))
    ])

    #Preprocessors WITH engineered feature

    tree_prepro_wfe = compose.ColumnTransformer(transformers=[
        ('num', num_4_tree, num_vars_wfe),
        ('cat', cat_4_tree, cat_vars)
    ], remainder='drop')

    mult_prepro_wfe = compose.ColumnTransformer(transformers=[
        ('num', num_4_mult, num_vars_wfe),
        ('cat', cat_4_mult, cat_vars)
    ], remainder='drop') 

    mult_models = {
    "LogRegr":        LogisticRegression(),
    "Ridge":          RidgeClassifier(),
    "SVM_lin":         SVC(kernel="linear", probability=True), # C=0.025
    "SVM_rbf":         SVC(kernel='rbf', probability=True),
    "NuSVC":           NuSVC(probability=True),
    "LinearSVC":       LinearSVC(),
    "KNN3":            KNeighborsClassifier(3),
    "KNN5":            KNeighborsClassifier(5),
    "GaussianNB":      GaussianNB()
        }

    tree_models = {
    "Decision Tree": DecisionTreeClassifier(),
    "Extra Trees": ExtraTreesClassifier(),
    "Random Forest": RandomForestClassifier(),
    "AdaBoost": AdaBoostClassifier(),
    "Skl GBM": GradientBoostingClassifier(),
    "Skl HistGBM": GradientBoostingClassifier(),
    }

    mult_classifiers_wfe = {name: pipeline.make_pipeline(mult_prepro_wfe, model) for name, model in mult_models.items()}
    tree_classifiers_wfe = {name: pipeline.make_pipeline(tree_prepro_wfe, model) for name, model in tree_models.items()}

    models_wfe = {**mult_classifiers_wfe, **tree_classifiers_wfe}

    x_wfe = full_df[num_vars_wfe + cat_vars]
    y_wfe = full_df.target
    x_train, x_val, y_train, y_val = model_selection.train_test_split(x_wfe,y_wfe,test_size=0.2,stratify=y_wfe,random_state=0)
    results = pd.DataFrame({'Model': [], 'Accuracy': [], 'Bal Acc.': []})


    for model_name, model in models_wfe.items():

        print(model_name)
        start_time = time.time()
        model.fit(x_train, y_train)
        
        
        pred = model.predict(x_val)
        
        results = results.append({"Model":    model_name,
                                "Accuracy": metrics.accuracy_score(y_val, pred)*100,
                                "Bal Acc.": metrics.balanced_accuracy_score(y_val, pred)*100,
                                },
                                ignore_index=True)
        
        results_ord = results.sort_values(by=['Accuracy'], ascending=False, ignore_index=True)
        results_ord.index += 1 
        
        clear_output(wait=True)
    st.write(results_ord.style.bar(subset=['Accuracy', 'Bal Acc.'], vmin=0, vmax=100, color='#5fba7d'))

