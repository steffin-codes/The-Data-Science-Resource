import streamlit as st
import urllib
class Functions():
    @st.cache(show_spinner=False)
    def get_file_content_as_string(path):
        url = 'https://raw.githubusercontent.com/steffincodes/data-scribbles/main/' + path
        response = urllib.request.urlopen(url)
        return response.read().decode("utf-8")