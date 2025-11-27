import requests
import streamlit as st
from interceptor import *
import json
import os
from parsers.parseUserFromJson import *
from model.UserDto import UserDto
from dotenv import load_dotenv


load_dotenv("appsettings.env")
API = os.getenv("API")


st.title("Account")

try:
    if st.session_state.token != "":
        data = send_with_bearer('/User/Me', requests.get) 
        if data is not None:
            data_dict = json.loads(data.text)
            user = parseUser(data_dict)
            st.session_state.user = user

        st.markdown(f"""
            User name: {user.username} \n
            Role: {user.role}
        """)
        col1, col2 = st.columns(2)
        with col1:
            pass

except:
    st.text("You are not logged in")

