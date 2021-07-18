import streamlit as st
from multiapp import MultiApp
from projects.{p0n} import App
from Helper import Functions
#TODO: {tldr}
def {p0n}_md():
    try:
        text = Functions.get_file_content_as_string("projects/{p0n}/README.md")
        # to check locally
        # with open("projects/{p0n}/README.md") as f:
        #     text = f.read() 
        if text:
            st.markdown(text)
        else: 
            st.info("Looks like it is empty 👀!!")
    except:
        st.error("Whoops there is no writeup for this project!")
    pass
def {p0n}_py():
    try:
        code = Functions.get_file_content_as_string("projects/{p0n}/App.py")
        # to check locally
        # with open("projects/{p0n}/App.py") as f:
        #     code = f.read()
        if code:
            st.code(code, language='python')
        else: 
            st.info("How is this possible!!")
    except:
        st.error("Something is definetly messed up!")
        # TODO: Add code to contact me with screenshot?
    pass
def app():
    {p0n} = MultiApp()
    {p0n}.add_app("Writeup", {p0n}_md)
    {p0n}.add_app("App", App.app)
    {p0n}.add_app("Code", {p0n}_py)
    {p0n}.run_radio()   