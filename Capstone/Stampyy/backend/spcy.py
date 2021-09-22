import numpy as np
import pandas as pd

import spacy
#from spacy.lemmatizer import Lemmatizer
from spacy.lang.en.stop_words import STOP_WORDS
import en_core_web_sm
from spacy.language import Language

from tqdm import tqdm_notebook as tqdm
from pprint import pprint

def tokenize(text):
    nlp = en_core_web_sm.load()
    df = pd.read_csv(text)
    docs = list(df["text"])
    def listToString(s): 
    
        # initialize an empty string
        str1 = " " 
        
        # return string  
        return (str1.join(s))
    listToString(docs)
    doc = nlp(listToString(docs))
    def show_ents(doc):
        if doc.ents:
            named_entity = []
            named_label = []
            for ent in doc.ents:
                named_entity.append(ent.text)
                named_label.append(ent.label_)
            print(f'{named_entity[0]} , {named_label[0]}')
            print(f'{named_entity[1]} , {named_label[1]}')
            print(f'{named_entity[2]} , {named_label[2]}')
            print(f'{named_entity[3]} , {named_label[3]}')
            print(f'{named_entity[4]} , {named_label[4]}')

          
        else:
            print("No entities to show")

    show_ents(doc)

