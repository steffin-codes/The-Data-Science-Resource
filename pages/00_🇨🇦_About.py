import streamlit as st
from styles import *

st.set_page_config(
    page_title="About me | Steffin",
    page_icon="🇨🇦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def Header():
    display_highlight(st,type="h1", delim='|',text="👋 Hi, I'm |Steffin|.")
    st.info("I am looking for a full-time remote job. Check out my resume [HERE](/Resume)", icon="🕵🏽‍♀️")
    pass
def Description():
    display_highlight(st,type="p", delim='|',text='''
    A few interesting things about me. I love to read science fiction (<i>my favorite is John C. McCrae's</i> <a href='https://parahumans.wordpress.com/'>|Worm|</a>. 
    Sometimes, I like to relax by drawing digital art or creating art using code. 
    I tend to use <a href='https://www.sketchbook.com/'>|Autodesk SketchBook|</a> when drawing <a href='https://www.instagram.com/steffin.rayen/'>|Digital Art|</a>. 
    I create Pure CSS images hosted on <a href="">|Codepen|</a> and 3D modelling with Blender hosted on <a href="">|Sketchfab|</a>. 
    Lastly, I love learning. 
    Every day I push myself to learn something new, whether that be about |machine learning|, |software engineering|, or miscellaneous facts about the universe.
    ''')
    display_highlight(st,type="p", delim='|',text="On top of recently getting married and graduating with a masters in Finance & IT from <a href='https://liba.edu/'>|LIBA|</a>, I also recently started working as a Product Engineer at <a href='https://smartail.ai/'>|Smartail|</a>. My work mainly revolves around utilizing |Natural Language Processing| and |Image Processing| to build a more intelligent solutions for Learning and Grading in the |Educational Sector|.")
    display_highlight(st,type="p", delim='|',text="I want to use my expertise to help others to make the right decisions, data-driven decisions")
    display_highlight(st,type="p", delim='|',text="Since I was young, I have always enjoyed to solve puzzles. So that's how I look at data sets: to me it is one big puzzle I want to solve. Finding patterns nobody else sees is the challenge to me.")
    display_highlight(st,type="p", delim='|',text="Do you want to work together? Please feel free to reach out to me using the below links.    ")
    pass
def SocialLinks():
    # social icons
    display_centered_text(st, text="|Connect with me!|", type="h2")
    display_line(st,'1em 40em 2em')
    social_columns = st.columns(3)
    with social_columns[0]:
        st.info("👔 Linkedin | [@steffinrayen](https://www.linkedin.com/in/steffinrayen/)")
        st.info("📷 Instagram | [@steffin.codes](https://www.instagram.com/steffin.codes/)")
        st.info("📝 Medium | [@steffincodes](https://medium.com/@steffincodes)")
    with social_columns[1]:
        st.info("🧠 Kaggle | [@steffincodes](https://www.kaggle.com/steffincodes)")
        st.info("🐱 Github | [@steffincodes](https://github.com/steffincodes)")
    with social_columns[2]:
        st.info("🎨 Codepen | [@steffincodes](https://codepen.io/steffincodes)")
        st.info("🖼️ Sketchfab | [@steffincodes](https://sketchfab.com/steffincodes)")
    pass
def AboutMe():
    Header()
    display_line(st,'4em 20em 4em')
    Description()
    display_line(st,'4em 20em 4em')
    SocialLinks()
    display_line(st,'4em 20em 0')
    pass
AboutMe()
