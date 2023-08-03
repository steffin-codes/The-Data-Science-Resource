import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
'''
Sarcasm Detector
    - Get text from User
    - Classify if Sarcastic or not
'''
cv = CountVectorizer()
def load_data():
    SARCASM_DATASET_URL = "https://raw.githubusercontent.com/steffincodes/data-scribbles/working/projects/p01/sarcasm.json"
    data = pd.read_json(SARCASM_DATASET_URL, lines=True)
    SARCASM_DATASET_URL = "/Users/steffin/Documents/data-scribbles/projects/p01/sarcasm_scraping.csv"
    df = pd.read_csv(SARCASM_DATASET_URL)

    return df
def load_model(df):
    data = df[["is_sarcastic","text"]]
    x = np.array(data["text"])
    y = np.array(data["is_sarcastic"])
    X = cv.fit_transform(x)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=42)
    model = BernoulliNB()
    model.fit(X_train, y_train)
    # model.fit(X, y)
    return model
def App():
    df = load_data()
    model = load_model(df)
    input_data = st.text_input('Detect Sarcasm', 'I found your nose it was in my business.')
    input_data_transformed = cv.transform([input_data]).toarray()
    is_sarcastic = model.predict(input_data_transformed)[0]
    is_sarcastic_text = "🙃 Sarcasm Detected" if is_sarcastic else "🙂 Seems to be factual"
    st.write(is_sarcastic_text)
    pass