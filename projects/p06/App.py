import streamlit as st
from gtts import gTTS
#TODO: Text to Speech using gTTS library

def app():
    #? Project Inputs
    st.title("P06: Text to Speech using gTTS library")
    input_text = st.text_input('Enter whatever')
    if st.button('Convert to Voice!'):    
        speech = gTTS(text = input_text, lang = 'en', slow = True)
        speech.save('user_trans.mp3')          
        audio_file = open('user_trans.mp3', 'rb')    
        audio_bytes = audio_file.read()    
        st.audio(audio_bytes, format='audio/ogg',start_time=0)
    pass