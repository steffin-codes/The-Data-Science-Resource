import streamlit as st
from projects.p01 import MainApp
from helpers import get_file_content_as_string
st.set_page_config(
    page_title="Project 01 | Steffin",
    page_icon="🐼",
    layout="wide",
    # initial_sidebar_state="collapsed"
)
def App():
    MainApp.App()
def Writeup():
    text_data = get_file_content_as_string(path="projects/p01/README.md")
    st.markdown(text_data)
def Code():
    code_data = get_file_content_as_string(path="projects/p01/MainApp.py")
    st.code(code_data, language='python')
options = st.radio('Choose what you want to see.', ['App', 'Writeup', 'Code'],horizontal=True, label_visibility="hidden")
if options == 'App':
    App()
elif options == 'Writeup':
    Writeup()
elif options == 'Code':
    Code()