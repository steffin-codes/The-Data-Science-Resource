import urllib
import streamlit as st
import joblib


GITHUB_REPO = st.secrets["GITHUB_REPO"]
IS_LOCAL = st.secrets["IS_LOCAL"]

def get_file_content_as_string(path):
    if IS_LOCAL:
        with open(path,'r') as fp:
            return fp.read()
    else:
        url = GITHUB_REPO + path
        response = urllib.request.urlopen(url)
        return response.read().decode("utf-8")
    pass
def get_model(path):
    if IS_LOCAL:
        model = joblib.load(path)
    else:
        url = GITHUB_REPO + path
        response = urllib.request.urlopen(url)
        return response.read().decode("utf-8")
    pass