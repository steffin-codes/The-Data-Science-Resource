import streamlit as st
from multiapp import MultiApp
from projects.p02 import App
from Helper import Functions
# TODO: Option to choose between writeup/code/app
# Download a single file and make its content available as a string.

def p02_md():
    try:
        text = Functions.get_file_content_as_string("projects/p02/README.md")
        if text:
            st.markdown(text)
        else: 
            st.info("Looks like it is empty 👀!!")
    except:
        st.error("Whoops there is no writeup for this project!")
        # TODO: Add code to request for writeup?
    pass
def p02_py():
    try:
        code = Functions.get_file_content_as_string("projects/p02/App.py")
        if code:
            st.code(code, language='python')
        else: 
            st.info("How is this possible!!")
    except:
        st.error("Something is definetly messed up!")
        # TODO: Add code to contact me with screenshot?
    pass
def app():
    p02 = MultiApp()
    p02.add_app("Writeup", p02_md)
    p02.add_app("App", App.app)
    p02.add_app("Code", p02_py)
    p02.run_radio()   