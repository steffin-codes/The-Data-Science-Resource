import streamlit as st
# preping schema
from Helper import Functions
# TODO: Yeah oops I forgot!
def app():
  st.header("FIVE QUESTIONS FOR SELECTING A STATISTICAL METHOD")
  numberOfVariables = st.radio(
    "How many variables do you have?",
    ('One','More Than One','Too many')
  )

  if numberOfVariables == 'Too many':
    st.success("Conduct a cluster analysis to select representative variables")
