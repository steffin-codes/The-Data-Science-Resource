import streamlit as st
from styles import *

st.set_page_config(
    page_title="Reads | Steffin",
    page_icon="📚",
    layout="wide"
)


display_line(st)
display_centered_text(st,"h1","Books I have Read")
display_line(st)
display_centered_text(st,"p","There's a lot of knowledge and content everywhere, but books remain the most condensed form of wisdom that I rely on. I thought I would maintain an eclectic set of books that I have been educated by. This list is a constant work in progress.")
display_line(st,"5em")
book_list = [
    # {
    #     "book_name":"",
    #     "author":"",
    #     "book_img":"",
    #     "book_one_liner":""
    # }
]
n_columns = 3
book_columns = st.columns(n_columns)
for i, book_data in enumerate(book_list):
    with book_columns[i%n_columns]:
        _col=st.columns([1,5,1])
        display_book_image(
            _col[1],
            img_src=book_data["book_img"],
            caption=book_data["book_one_liner"])
    # display_centered_text(
    #     book_columns[i%n_columns],
    #     "p",
    #     f'{book_data["book_name"]} | {book_data["author"]}'
    #     )