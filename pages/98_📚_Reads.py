import streamlit as st
from styles import *

st.set_page_config(
    page_title="Reads | Steffin",
    page_icon="📚",
    layout="wide",
    # initial_sidebar_state="collapsed"
)

BOOKS = [
    {
        "book_name":"Worm",
        "author":"Wildbow (John C. McCrae)",
        "book_img":"https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1519662877l/18713259.jpg",
        "book_one_liner":"Trauma induced unconventional superpowers in teenage students."
    # },{
    #     "book_name":"",
    #     "author":"",
    #     "book_img":"",
    #     "book_one_liner":""
    }
]
def Header():
    display_line(st)
    display_centered_text(st,"h1","My Reading List")
    display_line(st)
    display_centered_text(st,"p","Was a voracious reader in my teens. Looking to use this page to hold myself Accountable and get back into the habit.")
    pass
def ListBooks():
    n_columns = 3
    book_columns = st.columns(n_columns)
    for i, book_data in enumerate(BOOKS):
        with book_columns[i%n_columns]:
            _col=st.columns([1,5,1])
            display_book_image(
                _col[1],
                img_src=book_data["book_img"],
                caption=book_data["book_one_liner"])
    pass
def BooksApp():
    Header()
    display_line(st,"5em")
    ListBooks()
    pass
BooksApp()