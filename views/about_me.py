import streamlit as st

from forms.contact import contact_form

# st.title("About Page")
@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

# Hero section
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/main-logo.jpg", width=230)

with col2:
    st.title("Sufe Meo", anchor=False)
    st.write("Data Scientist | Machine Learning Engineer | AI Enthusiast")
    if st.button("Contact Me"):
        show_contact_form()


# experience & qualification
st.write("\n")
st.subheader("Experience & Qualification", anchor=False)
st.write(
    """
    - **Data Scientist** at [Company Name](https://www.company.com) (2022 - Present)
    - **Machine Learning Engineer** at [Company Name](https://www.company.com) (2020 - 2022)
    - **Bachelor's Degree in Computer Science** from [University Name](https://www.university.com) (2016 - 2020)
    """
)

# skills
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Python, R, SQL
    - Machine Learning, Deep Learning
    - Data Visualization (Tableau, Power BI)
    - Cloud Computing (AWS, Azure)
    """
)