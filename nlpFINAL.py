
import pandas as pd
import re
import nltk


from textblob import TextBlob
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from textblob.sentiments import NaiveBayesAnalyzer
from textblob import Blobber


reviews = pd.read_csv('reviews4.csv')

ps = PorterStemmer()

nltk.download('stopwords')

tokwords = []

for i in range(6800):
    review = re.sub('[^a-zA-Z]',' ',reviews['Reviews'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    tokwords.append(review)
    
    
sumscore1 = []
tb=Blobber(analyzer=NaiveBayesAnalyzer())
for i in range(6800):
    a=tb(tokwords[i])
    sumscore1.append(a.sentiment.p_pos)



















