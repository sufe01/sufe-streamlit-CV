import streamlit as st

# page setup
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    page = "views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    page = "views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)

# navigation setup
# methos 1
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# method2
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)

# shared on all pages
st.logo("assets/sidebar-logo.png")
st.sidebar.text("Made with ❤️ by Sufe")


# run navigation
pg.run()