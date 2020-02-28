# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import gensim
data = pd.read_csv("movies.csv",encoding="latin-1").to_numpy()
reviews = pd.read_csv('sumscore111FINAL.csv').to_numpy()
temp=np.copy(data)
movies = []
for x in temp:
    x=' '.join(x)
    movies.append(x)


file_docs = []

for line in movies:
    file_docs.append(line)


print("Number of documents:",len(file_docs))

gen_docs = [[w.lower() for w in word_tokenize(text)] 
            for text in file_docs]

dictionary = gensim.corpora.Dictionary(gen_docs)
print(dictionary.token2id)

corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]

tf_idf = gensim.models.TfidfModel(corpus)

#for doc in tf_idf[corpus]:
    #print([[dictionary[id], np.around(freq, decimals=2)] for id, freq in doc])
    
sims = gensim.similarities.Similarity('',tf_idf[corpus],
                                        num_features=len(dictionary))

file2_docs = []

token=["Paramount Pictures	Tony Scott	Action	Top Gun	PG	Tom Cruise	Jim Cash"]
for line in token:
    file2_docs.append(line)


for line in file2_docs:
    query_doc = [w.lower() for w in word_tokenize(line)]
    query_doc_bow = dictionary.doc2bow(query_doc) #update an existing dictionary and create bag of words
    

query_doc_tf_idf = tf_idf[query_doc_bow]
#print(document_number, document_similarity)

array = sims[query_doc_tf_idf]
#val=max(array);
#array=np.delete(array,np.where(array==val))

print('Comparing Result:', array)

ind =np.argpartition(array, -6)[-6:]
#rint(ind)


fr=[]
for x in ind:
    fr.append(reviews[x-2])
    

sortedList = []
sortedList = sorted(zip(fr,ind),reverse=True)[:6]
print("Most similar moveis ranked from best to worst are:")
for x in sortedList:
    print(data[x[1]][3])
    
    










# Python program to find largest value 
# on each level of binary tree. 
  
