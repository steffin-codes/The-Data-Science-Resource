from multiapp import MultiApp
# import your project modules here
from pages import ChooseStatisticModel
class Page:
    def app():
        page = MultiApp()
        page.add_app("🤔 Choose Statistical Model", ChooseStatisticModel.app)
        page.run(group_name = "Choose a Page:")
        pass
    pass