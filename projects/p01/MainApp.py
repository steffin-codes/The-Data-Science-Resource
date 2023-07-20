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
# data = pd.read_json("Sarcasm.json", lines=True)
# print(data.head())

def App():
    df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

    st.dataframe(df)  # Same as st.write(df)
    pass