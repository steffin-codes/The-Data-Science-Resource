"""
Check out the original here: https://github.com/upraneelnihar/streamlit-multiapps
Framework for running multiple Streamlit applications as a single app.
"""
import streamlit as st
class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    def __init__(self):
        self.apps = []
    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })
    def run(self,group_name=""):
        # app = st.sidebar.radio(
        # app = st.selectbox(
        app = st.sidebar.selectbox(
            group_name,
            self.apps,
            format_func=lambda app: app['title'])
        app['function']()
    # extra for toggling to show code/writeup/app
    def run_radio(self,group_name=""):
        # https://discuss.streamlit.io/t/horizontal-radio-buttons/2114/6
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        # for toggling between code/markdown/app
        app = st.radio(
        # app = st.sidebar.radio(
        # app = st.selectbox(
        # app = st.sidebar.selectbox(
            group_name,
            self.apps,
            format_func=lambda app: app['title'])
        app['function']()