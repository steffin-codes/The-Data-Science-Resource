import streamlit as st
import pandas as pd
from Helper import Functions
# TODO: Add credits and instructions for navigation
def app():
    st.title('Hello and Welcome to Steffin\'s Data Blog 👋🏼')
    st.warning('Please be informed that besides the effort put in consolidating the application, any data/code/writeup you find here is not my own but rather a brainchild of my google searching capabilities. Care is taken to source to the original authors. But when more than 5 sources are refered to, the most relevant are cited.')
    st.success('👈🏼 Headover to the sidebar to find live demo of the below projects!')
    list_of_projects = Functions.load_csv_as_dataframe("projects.csv") 
    df = pd.DataFrame(list_of_projects)
    df.sort_values(by=['date'],inplace=True,ascending=False)
    for index, project in df.iterrows():
        st.markdown('''
        ***
        >
        > `{}`
        > ## **{}**
        > > {}
        > 
        > *View the accompaning [Google Colab Notebook]({})*
        >
        > **Algorithm used:** `{}`
        '''.format(
            project["date"].strftime("%c").replace(" 00:00:00",","),
            project["name"],
            project["tldr"],
            project["notebook"],
            project["algorithm"]

        ))