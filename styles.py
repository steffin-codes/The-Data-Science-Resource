def display_centered_text(st,type,text):
    return st.markdown(f"<{type} style='text-align: center;'>{text}</{type}>",unsafe_allow_html=True)
def display_line(st,margin=0):
    return st.markdown(f"<hr style='margin:{margin}'>",unsafe_allow_html=True)
def display_book_image(st,img_src,caption=""):
    # return st.markdown(f"<img src={img_src} alt={img_alt} style='height: 300px;'/>",unsafe_allow_html=True)
    return st.image(img_src,width=250,caption=caption)