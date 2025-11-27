import requests
import streamlit as st
import os
from collections.abc import Callable
from dotenv import load_dotenv
load_dotenv("appsettings.env")
API = os.getenv("API")


def send_with_bearer(url,  http_action: Callable, data = None):
    if "token" not in st.session_state:
        return None
    
    headers = {"Authorization": f"Bearer {st.session_state.token}"}
    r = http_action(API + url, data=data, headers=headers)
    
    if r.status_code == 401:
        refresh_resp = requests.post(API + "/User/Refresh")
        if refresh_resp.status_code == 200:
            st.session_state.token = refresh_resp.json()["access_token"]
            headers = {"Authorization": f"Bearer {st.session_state.access}"}
            r = http_action(API + url, headers=headers)
    
    return r