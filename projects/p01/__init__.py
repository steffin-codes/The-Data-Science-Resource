from typing import final
import streamlit as st
from multiapp import MultiApp
from projects.p01 import PaletteGenerator
# TODO: Option to choose between writeup/code/app
def p01_md():
    try:
        with open("projects\p01\README.md", 'r') as p01_file:
            text = p01_file.read()
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
        with open("projects\p01\PaletteGenerator.py", 'r',encoding="utf8") as p01_file:
            code = p01_file.read()
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
    p01.add_app("App", PaletteGenerator.app)
    p01.add_app("Code", p01_py)
    p01.run_radio()   