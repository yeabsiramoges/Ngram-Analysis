import requests
import pandas as pd

#https://storywrangling.org/api/ngrams/your api query
#api/ngrams/<query>?<parameter>=<value>&<parameter>=<value>&<parameter>=<value>

#query is search , no quotations allowed
#metric is lexical fame aka rank or freq
#language can be en,es,ru,fr
#rt is false or true incclude retweets
#src is metada for loogging and debuggging and can be api or ui

phrase="me too"
metric="rank"
lang="en"
rt='false'
src="api"

df=pd.read_csv("output\phrases.csv")
df1=df[::-1]
df1= df1.head(3000)


train2=pd.DataFrame(columns=["phrase","count","count_no_rt","date","freq","freq_no_rt","odds","odds_no_rt","rank","rank_no_rt"])
train2=pd.DataFrame()

for ind,i in df1.iterrows():
    word1=i["word1"] 
    word2=i["word2"]

    if i["word3"]=="n/a" or "nan":
        word3=""
        phrase= word1 + " " +word2
    else:
        word3=i["word3"]
        phrase= str( word1) + " " +str(word2) + ' ' + str(word3)
    
    print(phrase)

    r = requests.get("https://storywrangling.org/api/ngrams/%s?metric=%s&language=%s&rt=%s&src=%s" % (phrase,metric,lang,rt,src))
    print(("https://storywrangling.org/api/ngrams/%s?metric=%s&language=%s&rt=%s&src=%s" % (phrase,metric,lang,rt,src)))
    print(r)
    try:
        cont=r.json()

        train = pd.DataFrame.from_dict(cont["data"])
        train1=pd.DataFrame()

        phrase_=[phrase]*len(train[phrase]["count"])
        train1["phrase"]= pd.Series(phrase_)
        train1["count"]=pd.Series(train[phrase]["count"])
        train1["count_no_rt"]=pd.Series(train[phrase]["count_no_rt"])

        train1["date"]=pd.Series(train[phrase]["date"])

        train1["freq"]=pd.Series(train[phrase]["freq"])
        train1["freq_no_rt"]=pd.Series(train[phrase]["freq_no_rt"])
        train1["odds"]=pd.Series(train[phrase]["odds"])
        train1["odds_no_rt"]=pd.Series(train[phrase]["odds_no_rt"])
        train1["rank"]=pd.Series(train[phrase]["rank"])
        train1["rank_no_rt"]=pd.Series(train[phrase]["rank_no_rt"])
        train2= pd.concat([train2,train1])

        print(train2)
    except:
        continue

filename="data_phrases" + ".csv"
train2.to_csv(filename)





 















































