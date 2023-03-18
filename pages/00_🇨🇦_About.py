import streamlit as st

st.set_page_config(
    page_title="About me | Steffin",
    page_icon="🇨🇦",
    layout="wide"
)

st.markdown('''
# Hi, I'm Steffin.

A few interesting things about me. I love to read science fiction (*my favorite is John C. McCrae's* **[Worm](https://parahumans.wordpress.com/)**). Sometimes, I like to relax by drawing digital art or creating art using code. I tend to use [Autodesk SketchBook](https://www.sketchbook.com/) when drawing [digital art](https://www.instagram.com/steffin.rayen/). I create Pure CSS images hosted on [Codepen](6) and 3D modelling with Blender hosted on [Sketchfab](7). Lastly, I love learning. Every day I push myself to learn something new, whether that be about machine learning, software engineering, or miscellaneous facts about the universe.

On top of recently getting married and graduating with a masters in Finance & IT from [LIBA](https://liba.edu/), I also recently started working as a Product Engineer at [Smartail](https://smartail.ai/). My work mainly revolves around utilizing Natural Language Processing and Image Processing to build a more intelligent solutions for Learning and Grading in the Educational Sector.

I want to use my expertise to help others to make the right decisions, data-driven decisions

Since I was young, I have always enjoyed to solve puzzles. So that's how I look at data sets: to me it is one big puzzle I want to solve. Finding patterns nobody else sees is the challenge to me.

Do you want to work together? Please feel free to reach out to me using the below links.    
''')
# social icons
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
# st.markdown('''
# ---

# [![alt text][2.1]][2]
# [![alt text][4.1]][4]
# [![alt text][3.1]][3]
# [![alt text][5.1]][5]
# [![alt text][1.1]][1]
# [![alt text][6.1]][6]
# [![alt text][7.1]][7]

# [1.1]: https://img.icons8.com/plasticine/50/linkedin.png (Linkedin | @steffinrayen)
# [2.1]: https://img.icons8.com/plasticine/50/instagram-new--v2.png (Instagram | @steffin.codes)
# [3.1]: https://img.icons8.com/sf-black-filled/50/medium-logo.png (Medium | @steffin.codes)
# [4.1]: https://i.ibb.co/GJ00pgc/kaggle.png (Kaggle | @steffincodes)
# [5.1]: https://i.ibb.co/SKRCHxB/icons8-github.gif (Github | @steffincodes)
# [6.1]: https://img.icons8.com/ios-filled/50/codepen.png (Codepen | @steffincodes)
# [7.1]: https://img.icons8.com/nolan/50/sketchfab.png (Sketchfab | @steffin.codes)

# [1]: https://www.linkedin.com/in/steffinrayen/
# [2]: https://www.instagram.com/steffin.codes/
# [3]: https://medium.com/@steffin.codes
# [4]: https://www.kaggle.com/steffincodes
# [5]: https://github.com/steffincodes
# [6]: https://codepen.io/steffincodes
# [7]: https://sketchfab.com/steffin.codes

# ''')