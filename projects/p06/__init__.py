import streamlit as st
from multiapp import MultiApp
from projects.p06 import App
from Helper import Functions
#TODO: Text to Speech using gTTS library
def p06_md():
    try:
        text = Functions.get_file_content_as_string("projects/p06/README.md")
        if text:
            st.markdown(text)
        else: 
            st.info("Looks like it is empty 👀!!")
    except:
        st.error("Whoops there is no writeup for this project!")
    pass
def p06_py():
    try:
        code = Functions.get_file_content_as_string("projects/p06/App.py")
        if code:
            st.code(code, language='python')
        else: 
            st.info("How is this possible!!")
    except:
        st.error("Something is definetly messed up!")
        # TODO: Add code to contact me with screenshot?
    pass
def app():
    p06 = MultiApp()
    p06.add_app("Writeup", p06_md)
    p06.add_app("App", App.app)
    p06.add_app("Code", p06_py)
    p06.run_radio()   