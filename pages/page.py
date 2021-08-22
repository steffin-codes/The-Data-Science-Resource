from multiapp import MultiApp
# import your project modules here
from pages import ChooseStatisticModel
class Page:
    def app():
        page = MultiApp()
        # https://docs.streamlit.io/en/stable/api.html
        # Add all your application here
        page.add_app("🧐 Choose Statistical Model", ChooseStatisticModel.app)
        # The main app
        page.run(group_name = "Choose a Page:")
        pass
    pass
