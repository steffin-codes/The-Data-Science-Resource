import streamlit as st
from multiapp import MultiApp
from projects.p01 import App
from Helper import Functions
# TODO: Option to choose between writeup/code/app
# Download a single file and make its content available as a string.

def p01_md():
    try:
        text = Functions.get_file_content_as_string("projects/p01/README.md")
        # to check locally
        # with open("projects/p01/README.md") as f:
        #     text = f.read() 
        if text:
            st.markdown(text)
        else: 
            st.info("Looks like it is empty 👀!!")
    except:
        st.error("Whoops there is no writeup for this project!")
        # TODO: Add code to request for writeup?
    pass
def p01_py():
    try:
        code = Functions.get_file_content_as_string("projects/p01/App.py")
        if code:
            st.code(code, language='python')
        else: 
            st.info("How is this possible!!")
    except:
        st.error("Something is definetly messed up!")
        # TODO: Add code to contact me with screenshot?
    pass
def app():
    p01 = MultiApp()
    p01.add_app("Writeup", p01_md)
    p01.add_app("App", App.app)
    p01.add_app("Code", p01_py)
    p01.run_radio()   