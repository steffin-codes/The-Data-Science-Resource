import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
#TODO: Fake News Detector
def app():
    #? Project Inputs
    data = pd.read_csv("projects/p08/news.csv")
    x = np.array(data["title"])
    y = np.array(data["label"])
    cv = CountVectorizer()
    x = cv.fit_transform(x)
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.1, random_state=1)
    model = MultinomialNB()
    model.fit(xtrain, ytrain)

    st.title("P08: Fake News Detector")
    newsHeadline = st.text_area("Enter Any News Headline: ")
    if newsHeadline:
        detect = st.button('Classify')
        if detect:
            data = cv.transform([newsHeadline]).toarray()
            a = model.predict(data)
            st.title(a[0])
    