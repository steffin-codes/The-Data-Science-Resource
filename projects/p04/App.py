import streamlit as st
import requests
import text2emotion as te
import json
import matplotlib.pyplot as plt

#TODO: Realtime Sentiment Analysis
def app():
    #? Project Inputs
    st.sidebar.subheader("Project Inputs:")
    st.title("P04: Real-Time Sentiment Analysis using Vader from nltk")
    user_input = st.text_input("Let's judge your tone!")
    submit = st.button(label="Judge Me!")

    if submit:
        #Call to the function
        score = te.get_emotion(user_input)
        # need full pies!
        score["Neutral"] = 1-sum(score.values())
        emotion  = max(score, key=score.get)
        # set the apikey and limit
        apikey = st.secrets["TENOR_API"]  # .streamlit/secrets.toml
        limit = 1
        # get the top 8 GIFs for the search term using default locale of EN_US
        fig, ax = plt.subplots()
        ax.pie(score.values(), labels = list(score.keys()))
        req = requests.get(
            "https://g.tenor.com/v1/random?contentfilter=high&q=%s&key=%s&limit=%s" % (emotion, apikey, limit))

        if req.status_code == 200:
            # load the GIFs using the urls for the smaller GIF sizes
            tenorJSON = json.loads(req.content)
            col1,col2 = st.columns([1,1])
            with col1:
                st.image (tenorJSON["results"][0]["media"][0]["gif"]["url"])
            with col2:
                st.pyplot(fig)
                print(score)
        else:
            st.write("Detected to be :",emotion)
