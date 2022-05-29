import pandas as pd
from collections import Counter, OrderedDict
from nltk import ngrams
import re
import operator
import numpy as np
f=open("sources.txt","r",encoding='utf-8', errors='replace')
f1=open("text.txt","r",encoding='utf-8', errors='replace')


lines_source= f.readlines()
lines_data=f1.readlines()

#a_string.split("\t")
#a_string.split("")
#a=lines_source[3]
#b=lines_data[3]

#print(lines_source[3])
#print(lines_data[3])


#print(a.split("\t"))

#print(b.split("<p>"))
vals=pd.DataFrame(columns=["ID","Date","Country","Website","Data"])
cols=["ID","Date","Country","Website","Data"]
data=[]
for i in lines_source[3:]:
    for j in lines_data[3:]:

        #print(i.split("\t")[0] )
        #print(j.split(" ")[0].strip("@@"))
        id_s_all=i.split("\t")
        id_s=id_s_all[0] 
        id_t_all=j.split(" ")
        id_t=id_t_all[0].strip("@@")
        if id_s==id_t:
            
           # print(1)
            #vals.append([i[0],i[2],i[3],i[4]," ".join(j[1:])], ignore_index=True)
            #print(vals)
            zipped=zip(cols,[id_s_all[0],id_s_all[2],id_s_all[3],id_s_all[4]," ".join(id_t_all[1:])])
            #data.append([i[0],i[2],i[3],i[4]," ".join(j[1:])])
            data.append(dict(zipped))
vals=vals.append(data,True)
print(vals)
data_all=""
for i in vals["Data"]:
    data_all+= " " + str(i)
data_all=data_all.lower()
data_all=re.sub('<[^<]+?>', '', data_all)
data_all=re.sub(r"[^a-zA-Z0-9.?! ]+", "", data_all)
data_all=re.sub(r'[^\w\s]','',data_all)

#get rid of commass, punctuaation, HTMl code,braacket , etc , p , s, h
#2 and 3
#cleaan it up " I do nt"
# 10 forr 3, 100 for 2
# dataa frram sstructure

#t1,t2,t3, freq, and date

ngram_counts = Counter(ngrams(data_all.split(), 3))
a=ngram_counts.most_common(5000)

ngram1=Counter(ngrams(data_all.split(), 2))
b=ngram1.most_common(1000)
c= (a+b)
x=[]
y=[]
z=[]
w=[]
for i in sorted( c, key=lambda x: x[1]):
    #print(i)
    if len (i[0])==2:
        x.append(i[0][0])
        y.append(i[0][1])
        z.append("n/a")
        w.append(i[1])
    else:
        x.append(i[0][0])
        y.append(i[0][1])
        z.append(i[0][2])
        w.append(i[1])




df=pd.DataFrame(np.column_stack([x,y,z,w]), columns=["word1",'word2','word3','count'])
df.to_csv('phrases.csv')


#print(a+b)
#for i in ((a+b).sort(key=operator.itemgetter(1))):
#    print(i)



with open('ngrams.txt', 'w') as f:
    f.write(str(a+b))


#print(ngram_counts)

#for i in range(len(lines_data[3:])):
#    a=(lines_source[i])
#    b=(lines_data[i])
#    id_s=a.split("\t")[0] 
#    id_t=b.split(" ")[0].strip("@@")
#    if id_s==id_t:
#        print("JI")
   # print(id_s)
   # print(id_t)


#print(vals)
            































