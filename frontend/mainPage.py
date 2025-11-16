import requests
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv("appsettings.env")
API = os.getenv("API")

st.title("Home Page")
st.write("Welcome to my multipage Streamlit app!")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    r = requests.post(API + "/User/Login", json={
        "id":0,
        "username": username,
        "password": password,
        "role":"admin"
    })
    if r.status_code == 200:
        st.session_state.token = r.json()['access_token']
        st.success("Logged in!")
    else:
        st.error("Invalid credentials")