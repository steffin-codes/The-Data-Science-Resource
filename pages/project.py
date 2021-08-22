from multiapp import MultiApp
from projects import p01,p02,p03,p04,p05,p06,p07
class Project:
    def app():
        app = MultiApp()
        app.add_app("📦️ List All", All.app)
        app.add_app("👷 ML", ML.app)
        app.add_app("📸 OpenCV", OpenCV.app)
        app.add_app("📈 DataViz", DataViz.app)
        app.run(group_name = "Choose a project:")
        pass
    pass

class All:
    def app():
        project = MultiApp()
        project.add_app("P01: Palette Generator using K-Means", p01.app)
        project.add_app("P02: Cartoonify Image using K-Means", p02.app)
        project.add_app("P03: Handwritten Digit Recognition", p03.app)
        project.add_app("P04: Real-Time Sentiment Analysis", p04.app)
        project.add_app("P05: Face Detection using OpenCV", p05.app)
        project.add_app("P06: Text to Speech using gtts", p06.app)
        project.add_app("P07: WhatsApp Chat Analyser", p07.app)
        project.run(group_name = "Choose a project:")
        pass
    pass

class OpenCV:
    def app():
        project = MultiApp()
        project.add_app("P01: Palette Generator using K-Means", p01.app)
        project.add_app("P02: Cartoonify Image using K-Means", p02.app)
        project.add_app("P03: Handwritten Digit Recognition", p03.app)
        project.add_app("P05: Face Detection using OpenCV", p05.app)
        project.run(group_name = "Choose an OpenCV project:")
        pass
    pass

class ML:
    def app():
        project = MultiApp()
        project.add_app("P01: Palette Generator using K-Means", p01.app)
        project.add_app("P03: Handwritten Digit Recognition", p03.app)
        project.add_app("P04: Real-Time Sentiment Analysis", p04.app)
        project.add_app("P06: Text to Speech using gtts", p06.app)
        project.run(group_name = "Choose a ML project:")
        pass
    pass

class DataViz:
    def app():
        project = MultiApp()
        project.add_app("P07: WhatsApp Chat Analyser", p07.app)
        project.run(group_name = "Choose a DataViz project:")
        pass
    pass
