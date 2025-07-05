# my_app/streamlit_app.py

import streamlit as st
import requests

st.set_page_config(page_title="My FastAPI App UI")

st.title("Hello from Streamlit 👋")

# FastAPI base URL
API_URL = "http://127.0.0.1:8000/greetings/hello"

if st.button("Say Hello"):
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            st.success(response.json()["message"])
        else:
            st.error(f"Error: {response.status_code}")
    except Exception as e:
        st.error(f"Failed to reach API: {e}")
