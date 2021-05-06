import time
from IPython.display import clear_output
import numpy    as np
import pandas   as pd

df      = pd.read_csv("train.csv", index_col='PassengerId')
df.isnull().sum()