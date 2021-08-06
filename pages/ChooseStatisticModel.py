import streamlit as st

st.header("FIVE QUESTIONS FOR SELECTING A STATISTICAL METHOD")

# preping schema

numberOfVariables = st.radio(
  "How many variables do you have?",
  ('One','More Than One','Too many')
)

if numberOfVariables == 'Too many':
  st.success("Conduct a cluster analysis to select representative variables")
