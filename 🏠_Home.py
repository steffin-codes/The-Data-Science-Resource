import streamlit as st
# st.write("Hello World")
from styles import *
st.set_page_config(
    page_title="Data Scribbles | Steffin",
    page_icon="🏠",
    layout="wide"
)
st.markdown('''
# 🗃️ Data Scribbles
> Contemplative coder and analyst. Inspired by tough problems.

Hello, I'm **Steffin**, and Welcome to my Portfolio.
''')
display_line(st,'8em')
# st.markdown(f"<h3 style='text-align: center;'>Areas of Interest</h3>",unsafe_allow_html=True)
display_centered_text(st,"h3","Areas Of Interest")
display_centered_text(st,"p","Take a look at some of the things I love working on.")
aoi_columns = st.columns(3)
with aoi_columns[0]:
    display_centered_text(st,"h5","💬 NLP")
    display_line(st)
    display_centered_text(st,"p","I apply text analytics to some of the hardest questions in business.")
with aoi_columns[1]:
    display_centered_text(st,"h5","🧠 ML")
    display_line(st)
    display_centered_text(st,"p","I am passionate about learning the theory that is pushing the cutting edge of ML.")
with aoi_columns[2]:
    display_centered_text(st,"h5","📉 Data Viz")
    display_line(st)
    display_centered_text(st,"p","I love telling a story. Getting to the heart of a problem and coming up with a solution.")
display_line(st,'8em')
display_centered_text(st,"h3","My Latest Projects")
display_centered_text(st,"p","Take a look at my recent work.")
project_columns = st.columns(3)
with project_columns[0]:
    display_centered_text(st,"h5","💬 NLP")
    display_line(st)
    st.info("👔 Date | [Project 1]()")

with project_columns[1]:
    display_centered_text(st,"h5","🧠 ML")
    display_line(st)
    st.info("👔 Date | [Project 1]()")
with project_columns[2]:
    display_centered_text(st,"h5","📉 Data Viz")
    display_line(st)
    st.info("👔 Date | [Project 1]()")


display_line(st)


st.markdown('''
## Skills Expertise
**Version control** GitHub | GitLab
**Devops** Azure Data Bricks
**DataBase** mySQL | MongoDB
''')
# st.sidebar.success("Select a project above.")