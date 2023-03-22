import streamlit as st
from styles import *
st.set_page_config(
    page_title="Credits | Steffin",
    page_icon="✒️",
    layout="wide",
    # initial_sidebar_state="collapsed"
)
CREDITS = [
    {"title":"Streamlit","link":"https://docs.streamlit.io/"}
   ,{"title":"Markdown","link":"https://www.markdownguide.org/basic-syntax/"}
   ,{"title":"Streamlit Extras","link":"https://extras.streamlit.app/"}
#    ,{"title":"","link":""}
]
st.title("✒️ Credits | Resources")
display_line(st,"2em 5em 4em")
for credit in CREDITS:
    st.markdown(f'🔗 [{credit["title"]}]({credit["link"]})')
