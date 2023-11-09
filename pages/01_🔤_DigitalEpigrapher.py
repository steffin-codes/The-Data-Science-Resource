
import streamlit as st
from projects.p01 import MainApp
from helpers import get_file_content_as_string
from styles import *
st.set_page_config(
    page_title=MainApp.CONSTANTS["name"] + "| Steffin",
    page_icon=MainApp.CONSTANTS["icon"],
    layout="wide",
    # initial_sidebar_state="collapsed"
)
display_highlight(st,f"{MainApp.CONSTANTS['icon']} |{MainApp.CONSTANTS['name']}|") 
st.text(MainApp.CONSTANTS["caption"])

def App():
    MainApp.App()
    pass
def Writeup():
    text_data = get_file_content_as_string(path="projects/p01/README.md")
    st.markdown(text_data)
def Code():
    code_data = get_file_content_as_string(path="projects/p01/MainApp.py")
    st.code(code_data, language='python')


options = st.radio('Choose what you want to see.', ['Writeup', 'Code', 'Demo'],horizontal=True, label_visibility="hidden")
if options == 'Demo':
    App()
elif options == 'Writeup':
    Writeup()
elif options == 'Code':
    Code()