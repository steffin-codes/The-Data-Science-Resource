import streamlit as st
import urllib
import pandas as pd
GIT_REPO = 'https://raw.githubusercontent.com/steffincodes/data-scribbles/main/'
class Functions():
    @st.cache(show_spinner=False)
    def get_file_content_as_string(path):
        url = GIT_REPO + path
        response = urllib.request.urlopen(url)
        return response.read().decode("utf-8")
    
    @st.cache(show_spinner=False)
    def load_csv_as_dataframe(path):
        DATA_URL = GIT_REPO + path
        data = pd.read_csv(DATA_URL,parse_dates=['Date'])
        # to check locally
        # with open(path) as f:
        #     data = pd.read_csv(path,parse_dates=['Date'])
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        return data