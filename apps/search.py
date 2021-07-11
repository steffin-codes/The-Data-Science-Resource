import streamlit as st
# TODO: give a search functionality to the posts...
def app():
    st.title('Look through my content maybe?')
    icon_col,text_col,button_col = st.beta_columns([1,9,1])
    with icon_col:
        st.title("🔍")
    with text_col:
        search_word = st.text_input("Looking for something specific?", "")
    with button_col:
        if(st.button("search")):
            st.write('You are trying to search for: ',search_word)
    st.write('list of all posts sorted by date.')
    st.write('With auto search functionality?')
