from multiapp import MultiApp
# import your project modules here
from projects import p01
class Project:
    def app():
        project = MultiApp()
        # https://docs.streamlit.io/en/stable/api.html
        # Add all your application here
        project.add_app("P01: Palatte Generator using K-Means", p01.app)
        # The main app
        project.run(group_name = "Choose a project:")
