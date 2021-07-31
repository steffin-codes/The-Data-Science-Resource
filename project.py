from multiapp import MultiApp
# import your project modules here
from projects import p01,p02,p03,p04,p05,p06
class Project:
    def app():
        project = MultiApp()
        # https://docs.streamlit.io/en/stable/api.html
        # Add all your application here
        project.add_app("P01: Palette Generator using K-Means", p01.app)
        project.add_app("P02: Cartoonify Image using K-Means", p02.app)
        project.add_app("P03: Handwritten Digit Recognition", p03.app)
        project.add_app("P04: Real-Time Sentiment Analysis", p04.app)
        project.add_app("P05: Face Detection using OpenCV", p05.app)
        project.add_app("P06: Text to Speech using gtts", p06.app)
        # The main app
        project.run(group_name = "Choose a project:")
