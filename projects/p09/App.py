import streamlit as st

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

#TODO: Language Detector

def app():
    #? Project Inputs
    data = pd.read_csv("projects/p09/language.csv")
    x = np.array(data["Text"])
    y = np.array(data["language"])

    cv = CountVectorizer()
    X = cv.fit_transform(x)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    model = MultinomialNB()
    model.fit(X_train,y_train)
    model.score(X_test,y_test)


    st.title("P09: Language Detector")
    languageText = st.text_area("Enter text: ")
    if languageText:
        detect = st.button('Detect Language')
        if detect:
            data = cv.transform([languageText]).toarray()
            output = model.predict(data)
            st.title('The detected language is : ',output[0])
    