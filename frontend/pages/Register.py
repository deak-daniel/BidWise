import requests
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv("appsettings.env")
API = os.getenv("API")

st.title("Register")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Register"):
    r = requests.post(API + "/User/Register", json={
        "id":0,
        "username": username,
        "password": password,
        "role":"admin"
    })
    st.switch_page("Home.py")