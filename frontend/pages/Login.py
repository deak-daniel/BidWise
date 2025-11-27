import requests
import streamlit as st
from interceptor import *
import json
import os
from parsers.parseUserFromJson import *
from model.UserDto import UserDto
from model.UserDto import UserDto
from dotenv import load_dotenv
load_dotenv("appsettings.env")
API = os.getenv("API")
st.title("Admin Login")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Admin Login"):
    user = UserDto(username, password, "admin", 0)
    r = requests.post(API + "/User/Login", data=json.dumps(user.__dict__))
    if r.status_code == 200:
        st.session_state.token = r.json()['access_token']
        data = send_with_bearer(url='/User/Me',http_action=requests.get) 
        if data is not None:
            data_dict = json.loads(data.text)
            user = parseUser(data_dict)
            st.session_state.user = user
        st.success("Logged in!")
        st.switch_page("Home.py")
    else:
        st.error("Invalid credentials")

col1, col2 = st.columns(2)
with col1:
    st.write("If you don't have an account register here: ")

with col2:    
    if st.button("Register"):
        st.switch_page("pages/Register.py")

