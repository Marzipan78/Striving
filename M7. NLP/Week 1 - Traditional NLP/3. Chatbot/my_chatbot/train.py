import json
import numpy as np
from nltk_utils import tokenize, stem, bag_of_words

with open('3. Chatbot\my_chatbot\intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ["?", "!", ".", ",", ";", ":", "...", "'", "’"]
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))
#print(all_words)
print(tags)

X_train = []
y_train = []
for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)

    label = tags.index(tag) # index of the label       
    y_train.append(label)   # sometimes you may need to use onehot encoding, # CrossEntropyloss to be used 

X_train = np.array(X_train) # convert to numpy arrays
y_train = np.array(y_train)          
