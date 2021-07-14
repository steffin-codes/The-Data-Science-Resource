import streamlit as st
# TODO: give a search functionality to the posts...
def app():
    st.title('Look through my content maybe?')
    icon_col,text_col = st.beta_columns([1,9])
    with icon_col:
        st.title("🔍")
    with text_col:
        search_word = st.text_input("Looking for something specific?", "")
    