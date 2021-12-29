# -*- coding: utf-8 -*-
"""text_classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mGXsDbwM5ZUpanR5teeeJW-d4gQUynOZ
"""

import nltk

nltk.download('all')

import numpy as np
import pandas as pd

dataset = pd.read_csv('https://raw.githubusercontent.com/futurexskill/ml-model-deployment/main/Restaurant_Reviews.tsv.txt', delimiter= '\t', quoting = 3)

dataset.head()

from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

dataset.info()

corpus = []

import re

for i in range(0, 1000):

  customer_review = re.sub('[^a-zA-Z]', ' ',dataset['Review'][i])
  customer_review = customer_review.lower()
  customer_review = customer_review.split()
  clean_review = [ps.stem(word) for word in customer_review if not word in set(stopwords.words('english'))]
  clean_review = ' '.join(clean_review)
  corpus.append(clean_review)

corpus[0]

corpus[6]

corpus[12]

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features = 1500, min_df = 3, max_df = 0.6)

X = vectorizer.fit_transform(corpus).toarray()

X

X[0]

y = dataset.iloc[:, 1].values

y

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

from sklearn.neighbors import KNeighborsClassifier
classifierKNN = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifierKNN.fit(X_train, y_train)

y_pred_knn = classifierKNN.predict(X_test)

from sklearn.metrics import classification_report, accuracy_score,confusion_matrix

cmknn = confusion_matrix(y_test, y_pred_knn)

cmknn

print("KNN accuracy \n", accuracy_score(y_test,y_pred_knn))

sample = ["Good batting by England"]

sample = vectorizer.transform(sample).toarray()

sample

sentiment = classifierKNN.predict(sample)

sentiment

sample2 = ["bad performance by India in the match"]

sample2 = vectorizer.transform(sample2).toarray()

sentiment2 = classifierKNN.predict(sample2)

sentiment2

import pickle

with open('textclassifier.pickle','wb') as file:
    pickle.dump(classifierKNN,file)

with open('tfidfmodel.pickle','wb') as file:
    pickle.dump(vectorizer,file)

!ls

from google.colab import files

files.download('textclassifier.pickle')

files.download('tfidfmodel.pickle')

