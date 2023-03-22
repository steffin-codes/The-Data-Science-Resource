import streamlit as st
from styles import *
st.set_page_config(
    page_title="Data Scribbles | Steffin",
    page_icon="🏠",
    layout="wide",
    # initial_sidebar_state="collapsed"
)
def Header():
    display_highlight(st,type="h1", delim='|',text="🗃️ |Data Scribbles|")
    display_line(st,"0")
    display_highlight(st,type="blockquote", delim='|',text="Contemplative |Coder and analyst|. Inspired by tough problems.")
    display_highlight(st,type="p", delim="|",text="Human 🕴 ! Female 💁‍♀️ ! Panda Lover 🐼 ! |Web Fanatic| 🕸️ ! Tea Drinker 🍵 ! |CSS Hobbyist| 🎨 ! |Data Enthusiast| 🦠 ! |Game Jam Player| 👾 ! |Python Evangelist| 🐍")
    pass
def Description():
    display_highlight(st,type="p", delim='|',text="Hi, My name is |Steffin|, an Indian |Data Scientist| with a background in |Software Engineering|.")
    display_highlight(st,type="p", delim='|',text="I am motivated by the belief that we can use data to make better decisions. I want to be able to make it easier for people to understand code and use data efficiently. I believe in |open data| and |open source software|. I primarily use |Python and Tableau|, but also have experience with |Javascript and R|.")
    display_highlight(st,type="p", delim='|',text="Data science is something that attracts me a lot, I think it is because of my curiosity of data and all the possibilities that are available to gain insights from that data! You don't always have to use hardcore concepts like deep learning to achieve that, my take is that some plots can already give an |'aha' moment|.")
    display_highlight(st,type="p", delim='|',text="I am an |avid reader| and have a passion for |healthy living|. I would love to help you out if you have a project in those areas! On this website you can find some examples of my projects.")
    display_highlight(st,type="p", delim='|',text="Have fun in browsing through the content and thank you for visiting!")
    pass
def AreasOfInterest():
    display_centered_text(st,"h3","📍 |Areas Of Interest| 📍")
    display_centered_text(st,"p","Take a look at some of the things I love working on.")
    aoi_columns = st.columns(3)
    with aoi_columns[0]:
        display_centered_text(st,"h5","💬 |NLP|")
        display_line(st)
        display_centered_text(st,"p","I apply text analytics to some of the hardest questions in business.")
    with aoi_columns[1]:
        display_centered_text(st,"h5","🧠 |ML|")
        display_line(st)
        display_centered_text(st,"p","I am passionate about learning the theory that is pushing the cutting edge of ML.")
    with aoi_columns[2]:
        display_centered_text(st,"h5","📉 |Data Viz|")
        display_line(st)
        display_centered_text(st,"p","I love telling a story. Getting to the heart of a problem and coming up with a solution.")
    pass
def LatestProjects():
    display_centered_text(st,"h3","📂 |My Latest Projects| 📂")
    display_centered_text(st,"p","Take a look at my recent work.")
    project_columns = st.columns(3)
    with project_columns[0]:
        display_centered_text(st,"h5","💬 |NLP|")
        display_line(st)
        # st.info("👔 Date | [Project 1]()")
    with project_columns[1]:
        display_centered_text(st,"h5","🧠 |ML|")
        display_line(st)
        # st.info("👔 Date | [Project 1]()")
    with project_columns[2]:
        display_centered_text(st,"h5","📉 |Data Viz|")
        display_line(st)
        # st.info("👔 Date | [Project 1]()")
    pass
def TechnicalSkills():
    display_centered_text(st,"h3","👩‍💻 |Technical Skills| 👩‍💻")
    display_centered_text(st,"p","Take a look at my recent work.")
    skills_columns = st.columns(3)
    with skills_columns[0]:
        display_centered_text(st,"h5","💬 |Languages|")
        display_line(st)
        st.info("Python", icon="🐍")
        st.info("Javascript", icon="🕷️")
        st.info("R", icon="🚩")
    with skills_columns[1]:
        display_centered_text(st,"h5","🧠 |Software Engineering|")
        display_line(st)
        st.info("WEB | React, Django", icon="🕸️")
        st.info("DB | MySQL, MongoDB", icon="🗄️")
        st.info("VC | Git", icon="🗂️")
    with skills_columns[2]:
        display_centered_text(st,"h5","📉 |Data Viz|")
        display_line(st)
        st.info("Wrangling", icon="🗃️")
        st.info("Visualization", icon="📉")
        st.info("Statistics", icon="📊")
    pass
def HomeApp():
    Header()
    display_line(st,'0')
    Description()
    display_line(st,'4em 20em 4em')
    AreasOfInterest()
    display_line(st,'6em 20em 6em')
    LatestProjects()
    display_line(st,'6em 20em 6em')
    TechnicalSkills()
    display_line(st,'6em 20em 6em')
    pass
HomeApp()
st.success("Browse through the pages listed in the sidebar!",icon="👈🏽")