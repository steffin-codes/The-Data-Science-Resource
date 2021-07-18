import streamlit as st

#TODO: {tldr}

def app():
    #? Project Inputs
    st.title("{p0n}: {projectTitle}")
    st.sidebar.subheader("Project Inputs:")
    generate = st.sidebar.button("Generate") 
    st.warning("👈🏼 Head over to the sidebar and upload an image!")    
    pass