import streamlit as st
from multiapp import MultiApp
# import your app modules here
from projects import p01_palGen,p02_faceDetect
class Project:
    def app():
        project = MultiApp()

        # https://docs.streamlit.io/en/stable/api.html

        # Add all your application here
        project.add_app("P01: Palatte generator using K-Means", p01_palGen.app)
        # project.add_app("P02: Hello", p02_faceDetect.app)

        # The main app
        project.run()
