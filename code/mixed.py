#How about linking the two pieces together? For example, given the popular n-grams from the 
#corpus data, can you automatically feed them to the StoryWrangler API, and see if their 
#popularities on social media and in mainstream media are correlated in some way? You can 
#address other questions of your choice, too.

import pandas as pd
from nltk import ngrams
import string
import collections
import re
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

bigrams = ngrams(tokenized, 2)
trigrams = ngrams(tokenized, 3)

#counting bigrams
bi_grams_freq = collections.Counter(bigrams)
tri_grams_freq = collections.Counter(trigrams)

#try to create file
try:
    bigrams_file = open("bigrams.txt", "x")
    trigrams_file = open("trigrams.txt", "x")
except FileExistsError:
    print("Files already exist")

#overwrite any existing data in file
bigrams_file = open("bigrams.txt", "w")
trigrams_file = open("trigrams.txt", "w")

bigrams_list = list(bi_grams_freq.most_common())
trigrams_list = list(tri_grams_freq.most_common())

bigrams_file.write(str(bigrams_list))
trigrams_file.write(str(trigrams_list))

#ngram plots
bigrams_series = pd.DataFrame(bigrams_list[0:20], columns=["Bigram", "Frequency"])
bigrams_series.plot(kind="bar",
                    x="Bigram",
                    y="Frequency",
                    color="green")
plt.title("Corpus Bigram Frequency Plot")
plt.show()