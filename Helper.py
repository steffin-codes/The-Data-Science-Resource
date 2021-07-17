import streamlit as st
import urllib
import pandas as pd
class Functions():
    @st.cache(show_spinner=False)
    def get_file_content_as_string(path):
        url = 'https://raw.githubusercontent.com/steffincodes/data-scribbles/main/' + path
        response = urllib.request.urlopen(url)
        return response.read().decode("utf-8")
    
    @st.cache(show_spinner=False)
    def load_csv_as_dataframe(path):
        DATA_URL = 'https://raw.githubusercontent.com/steffincodes/data-scribbles/main/' + path
        data = pd.read_csv(DATA_URL,parse_dates=['Date'])
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        return data