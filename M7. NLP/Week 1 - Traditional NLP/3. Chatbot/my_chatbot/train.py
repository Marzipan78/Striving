import json
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
print(all_words)
