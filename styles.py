COLORS={
    "Red": "#D32F2F",
    "Pink": "#C2185B",
    "Purple": "#7B1FA2",
    "DeepPurple": "#512DA86",
    "Indigo": "#303F9F",
    "Blue": "#1976D2",
    "LightBlue": "#0288D1",
    "Cyan": "#0097A7",
    "Teal": "#00796B",
    "Green": "#388E3C",
    "LightGreen": "#689F38",
    "Lime": "#AFB42B",
    "Yellow": "#FBC02D",
    "Amber": "#FFA000",
    "Orange": "#F57C00",
    "DeepOrange": "#E64A19",
    "Brown": "#5D4037",
    "Grey": "#616161",
    "BlueGrey": "#455A64"
}
def display_highlight(st,text,type="h1", delim='|',get_str=False):
    text_list = text.split(delim)
    highlight_css_start = f"<span style='background: linear-gradient(180deg,rgba(0,0,0,0) 50%, #7B1FA2 50%); font-weight:700;'>"
    highlight_css_end = "</span>"
    final_text = "<"+type+">"+text_list[0]
    for i, text in enumerate(text_list[1:]):
        if (i+1)%2:
            final_text+=highlight_css_start+text+highlight_css_end
        else:
            final_text+=text
    final_text+="</"+type+">"
    if get_str:
        return final_text
    else:
        return st.markdown(
            f"{final_text}",
            unsafe_allow_html=True
        )
def display_centered_text(st,type,text):
    return st.markdown(f"<{type} style='text-align: center;'>{display_highlight(st,text=text,type='span',get_str=True)}</{type}>",unsafe_allow_html=True)
def display_line(st,margin="0 5em 0"):
    return st.markdown(f"<hr style='margin:{margin}'>",unsafe_allow_html=True)
def display_book_image(st,img_src,img_alt="",caption=""):
    return st.image(img_src,width=250,caption=caption)
