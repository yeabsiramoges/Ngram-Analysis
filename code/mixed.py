#How about linking the two pieces together? For example, given the popular n-grams from the 
#corpus data, can you automatically feed them to the StoryWrangler API, and see if their 
#popularities on social media and in mainstream media are correlated in some way? You can 
#address other questions of your choice, too.

import requests
import pandas as pd
from collections import Counter
from nltk import ngrams
import string
import collections
import re
import numpy as np
import matplotlib.pyplot as plt

#open corpus text file
with open("sample-data/text.txt","r",encoding='utf-8', errors='replace') as file:
    corpus_text = file.read()


#text cleanup
regex = "[" + re.sub("\.", "",string.punctuation) + "]"

corpus_text = re.sub('<.*>','', corpus_text)
corpus_text = re.sub(regex, "", corpus_text)

#getting words
tokenized = corpus_text.split()

bi_grams = ngrams(tokenized, 2)
tri_grams = ngrams(tokenized, 3)

#counting bigrams
bi_grams_freq = collections.Counter(bi_grams)
tri_grams_freq = collections.Counter(tri_grams)

print(bi_grams_freq.most_common(20))
print(tri_grams_freq.most_common(20))

#ngram plots
bigrams_series = pd.Series(bi_grams_freq)[:20]

bigrams_series.sort_values().plot.barh(color='black', width=1, figsize=(12, 8))
plt.title('Most Frequent Bigrams')
plt.ylabel('Bigram')
plt.xlabel('Occurances')

plt.show()
