import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
import streamlit as st

# Must be the first Streamlit command
st.set_page_config(page_title="B站最强工作室", layout="wide")

# Import pages from the new directory
from page_content.home import 组织头目
from page_content.education import 代表作品
from page_content.experience import 七人传奇
from page_content.resume import 开枝散叶
from page_content.contact import 联系我们

# Import components
from components.footer import display_footer
from components.styles import load_css

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        # Load custom CSS
        load_css()

        st.sidebar.markdown("## 雀巢工作室")
        app = st.sidebar.radio(
            "目录", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")

        app["function"]()
        
        # Display footer at the bottom of each page
        display_footer()

# Initialize the app
app = MultiApp()

# Add pages to the app
app.add_app("组织头目", 组织头目)
app.add_app("代表作品", 代表作品)
app.add_app("七人传奇", 七人传奇)
app.add_app("开枝散叶", 开枝散叶)
app.add_app("联系我们", 联系我们)

# Run the app
app.run()
