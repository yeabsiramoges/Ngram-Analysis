import pandas as pd
from collections import Counter
from nltk import ngrams
import re
import numpy as np

sources = open("sample-data\database\sources.txt","r",encoding='utf-8', errors='replace')
sample_text = open("sample-data/text.txt","r",encoding='utf-8', errors='replace')

lines_source = sources.readlines()
lines_data = sample_text.readlines()

vals = pd.DataFrame(columns=["ID","Date","Country","Website","Data"])
cols = ["ID","Date","Country","Website","Data"]
data = []

for source in lines_source[3:]:
    for text in lines_data[3:]:

        id_s_all=source.split("\t")
        id_s=id_s_all[0] 
        id_t_all=text.split(" ")
        id_t=id_t_all[0].strip("@@")

        if id_s==id_t:
            zipped=zip(cols,[id_s_all[0],id_s_all[2],id_s_all[3],id_s_all[4]," ".join(id_t_all[1:])])
            data.append(dict(zipped))

vals=vals.append(data,True)
print(vals)
data_all=""

for source in vals["Data"]:
    data_all+= " " + str(source)

data_all=data_all.lower()
data_all=re.sub('<[^<]+?>', '', data_all)
data_all=re.sub(r"[^a-zA-Z0-9.?! ]+", "", data_all)
data_all=re.sub(r'[^\w\s]','',data_all)

ngram_counts = Counter(ngrams(data_all.split(), 3))
a=ngram_counts.most_common(5000)

ngram1=Counter(ngrams(data_all.split(), 2))
b=ngram1.most_common(1000)
c= (a+b)
x=[]
y=[]
z=[]
w=[]

for source in sorted( c, key=lambda x: x[1]):
    if len (source[0])==2:
        x.append(source[0][0])
        y.append(source[0][1])
        z.append("n/a")
        w.append(source[1])
    else:
        x.append(source[0][0])
        y.append(source[0][1])
        z.append(source[0][2])
        w.append(source[1])

df=pd.DataFrame(np.column_stack([x,y,z,w]), columns=["word1",'word2','word3','count'])
df.to_csv('phrases.csv')

with open('ngrams.txt', 'w') as sources:
    sources.write(str(a+b))