import streamlit as st
import urllib
import pandas as pd
GIT_REPO = 'https://raw.githubusercontent.com/steffincodes/data-scribbles/main/'
IS_LOCAL = False # commit with False
DO_DEBUG = True
class Functions():
    @st.cache(show_spinner=False)
    def get_file_content_as_string(path):
        if IS_LOCAL:
            with open(path,'r') as fp:
                return fp.read()
        else:
            url = GIT_REPO + path
            response = urllib.request.urlopen(url)
            return response.read().decode("utf-8")
    
    @st.cache(show_spinner=False)
    def load_csv_as_dataframe(path):
        # to check locally
        if IS_LOCAL:
            with open(path) as f:
                data = pd.read_csv(path,parse_dates=['Date'])
        else:
            DATA_URL = GIT_REPO + path
            data = pd.read_csv(DATA_URL,parse_dates=['Date'])
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        return data