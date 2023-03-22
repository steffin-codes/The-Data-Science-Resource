import streamlit as st
from styles import *
st.set_page_config(
    page_title="Resume | Steffin",
    page_icon="📄",
    layout="wide",
    # initial_sidebar_state="collapsed"
)
def Header():
    display_centered_text(st,type="h1",text='|STEFFIN RAYEN|')
    display_centered_text(st,"p",'💻 Experienced machine learning engineer and Python developer')
    display_highlight(st,"Looking to build and deploy reusable |ML pipelines| that aids converting raw data into |actionable insights| and discover profitable trends","blockquote")
    pass
def Experience():
    display_highlight(st,text="👩🏻‍💻 |Experience|",type="h3")
    exp_data = [
        {
            "right":"Jun 2022 - Present",
            "left":[
                {
                    "type":"h4",
                    "text":"Smartail 📍 Chennai, IN"
                },{
                    "type":"h5",
                    "text":"Product Engineer"
                },{
                    "type":"li",
                    "text":"Responsible for the AI/ML logic of |5 AI-based Grading Services| including student hand-written image processing systems, Objective Grading, Subjective Grading and Equation Grading Systems."
                },{
                    "type":"li",
                    "text":"Implemented an intelligent character recognition (ICR) component to recognize handwritten and machine printed information from student written answer papers and other documents from teachers, as part of the computer vision team."
                },{
                    "type":"li",
                    "text":"Owned |OMR Grading System| built from Scratch with |98(%) accuracy|, in a period of 30 Days with custom analytics that is |Student Improvement Centric| rather than the extensively available Student Performance Centric."
                },{
                    "type":"li",
                    "text":"Designed the |ML framework| that was applied by the solutions team throughout all ML lifecycle which |removed downtime| during new releases."
                },{
                    "type":"li",
                    "text":"Implemented a |customized Natural Language Processing API| to facilitate the data analysis of |qualitative data|."
                },{
                    "type":"li",
                    "text":"|Optimized| the process of |reporting| on client data, conducted |data analysis| on client data using Python scripts."
                },{
                    "type":"li",
                    "text":"Coached and trained a team of 10 analysts' works by providing feedbacks for improvements and general guidance for resources to refer."
                # },{
                #     "type":"li",
                #     "text":"Provided product insights to an employee engagement platform by testing hypothesis about how to improve health, happiness and performance of employees in the workplace."
                # },{
                #     "type":"li",
                #     "text":"Data collection (noSQL, MongoDB, Events APIs), Data Wrangling(Python, Pandas), Data Visualization (Google Sheets, Google Slides, tableau), and reported insights to board members and stakeholders."
                }
            ]
        },{
            "right":"Sep 2021 - Mar 2022",
            "left":[
                {
                    "type":"h4",
                    "text":"AICG 📍 Remote"
                },{
                    "type":"h5",
                    "text":"Full Stack Web Developer (Contractor)"
                },{
                    "type":"li",
                    "text":"Developed |KPI's and actionable report| in PowerBI saving 16 hours of manual work per week using |SSIS and DAX| queries."
                },{
                    "type":"li",
                    "text":"|Built CP model| using Azure pipeline (|ADF, ADB & ADO|) to allocate Surgery schedule with real-time data from a custom  |MERN| webpage."
                }
            ]
        },{
            "right":"Aug 2018 - Mar 2022",
            "left":[
                {
                    "type":"h4",
                    "text":"Maveric Systems 📍 Chennai, IN"
                },{
                    "type":"h5",
                    "text":"T24 Developer"
                },{
                    "type":"li",
                    "text":"Worked closely with a multidisciplinary team by applying an in-house |metrics-driven agile approach|"
                },{
                    "type":"li",
                    "text":"Significantly |decreased resolution time| QoQ and helped Temenos acquire new business clients."
                },{
                    "type":"li",
                    "text":"Managed all |Custom T24 development| for 9+ Australian Banks, 3 US Banks, and 2 Canadian Banks and facilitated day-to-day help desk operations including ticket prioritization, tracking, and timely resolution"
                },{
                    "type":"li",
                    "text":"Increased performance of |SQL queries| that generate daily Tax reports through |INSIGHT, by 35%|."
                }
            ]
        }
    ]
    for data in exp_data:
        exp_cols = st.columns([1,5])
        with exp_cols[0]:
            display_highlight(st,data["right"].upper(),"p",'|',False,'12px 0 16px')
            pass
        with exp_cols[1]:
            for _data in data["left"]:
                display_highlight(st,_data["text"],_data["type"])
            pass
    pass
def Education():
    display_highlight(st,text="👩🏻‍🏫 |Education|",type="h3")
    edu_data = [
        {
            "right":"AUG 2017 - AUG 2018",
            "left":'''
                #### LIBA
                ##### Executive Post Graduate Diploma in Financial Services and IT Assurance
                - Built a Statistical Model to predict the Onion Market Price Fluctuations
                - Course focus includes statistical modeling, theoretical and mathematical statistics, business fundamentals for analytics.
            ''',
        },{
            "right":"MAY 2013 - MAY 2017",
            "left":'''
                #### LICET
                ##### BE in CSE
                - Built a Smart Mirror to display customized components based on facial recognition on a Mirror using Raspberry Pi, SQL,  Python, and NodeJS
            ''',
        }
    ]
    for data in edu_data:
        edu_cols = st.columns([1,5])
        with edu_cols[0]:
            display_highlight(st,data["right"].upper(),"p",'|',False,'12px 0 16px')
            pass
        with edu_cols[1]:
            st.markdown(data["left"])
            pass
    pass
def TechnicalExperience():
    display_highlight(st,text="🃏 |Technical Experience|",type="h3")
    pass
def PersonalProjects():
    display_highlight(st,text="🕳 |Personal Projects|",type="h3")
    '''
    🔗 Data Scribbles  
    A blog on my data journey
    Python | Github | Streamlit
    🔗  CatsWhoCode - https://github.com/steffincodes/catswhocode
    A Cat themed Discord clone
    Django | MySQL | Python
    🔗  Kitchenette - https://kitchenette.vercel.app/
    A minimal CRUD app
    NextJS | Vercel | Tailwind
    🔗 Coronasomnia - https://steffinrayen.itch.io/coronasomnia
    A 2D web/Android game
    Unity2D | C#
    '''
    pass
def ResumeApp():
    Header()
    Experience()
    Education()
    # TechnicalExperience()
    # PersonalProjects()
    pass
ResumeApp()
