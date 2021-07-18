import streamlit as st
from multiapp import MultiApp
from projects.p03 import App
from Helper import Functions
#TODO: A simple Handwritten Digit Recognition using CNN on the MINST dataset that accepts data from canvas
def p03_md():
    try:
        text = Functions.get_file_content_as_string("projects/p03/README.md")
        if text:
            st.markdown(text)
        else: 
            st.info("Looks like it is empty 👀!!")
    except:
        st.error("Whoops there is no writeup for this project!")
    pass
def p03_py():
    try:
        code = Functions.get_file_content_as_string("projects/p03/App.py")
        if code:
            st.code(code, language='python')
        else: 
            st.info("How is this possible!!")
    except:
        st.error("Something is definetly messed up!")
        import sys
        st.error(sys.exc_info())
        # TODO: Add code to contact me with screenshot?
    pass
def app():
    p03 = MultiApp()
    p03.add_app("App", App.app)
    p03.add_app("Writeup", p03_md)
    p03.add_app("Code", p03_py)
    p03.run_radio()   