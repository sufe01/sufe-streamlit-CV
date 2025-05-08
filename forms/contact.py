import re

import streamlit as st
import requests

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern,email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit :material/send:", type="primary", use_container_width=True,)

        if submit_button:
            # st.success("Message successfully sent!")
            if not WEBHOOK_URL:
                st.error("Email service is not configured. PLease try again later")
                st.stop()

            if not name:
                st.error("Please provide your name.", icon="🥴")
                st.stop()

            if not email:
                st.error("Please provide your email address.", icon="📨")
                st.stop()

            if not is_valid_email(email):
                st.error("Please provide a valid email.", icon="📧")
                st.stop()

            if not message:
                st.error("Please type your message.", icon="💬")
                st.stop()

            # prepare the payload and send
            data = {"name": name, "email": email, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("Your Message has been sent successfully!")
            else:
                st.error("there was an error sending your message. Please try again later.")