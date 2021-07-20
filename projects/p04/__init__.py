import streamlit as st
from multiapp import MultiApp
from projects.p04 import App
from Helper import Functions

def p04_md():
    try:
        text = Functions.get_file_content_as_string("projects/p04/README.md")
        # to check locally
        # with open("projects/p04/README.md") as f:
        #     text = f.read() 
        if text:
            st.markdown(text)
        else: 
            st.info("Looks like it is empty 👀!!")
    except:
        st.error("Whoops there is no writeup for this project!")
    pass
def p04_py():
    try:
        code = Functions.get_file_content_as_string("projects/p04/App.py")
        if code:
            st.code(code, language='python')
        else: 
            st.info("How is this possible!!")
    except:
        st.error("Something is definetly messed up!")
        # TODO: Add code to contact me with screenshot?
    pass
def app():
    p04 = MultiApp()
    p04.add_app("Writeup", p04_md)
    p04.add_app("App", App.app)
    p04.add_app("Code", p04_py)
    p04.run_radio()   