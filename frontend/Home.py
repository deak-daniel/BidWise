import requests
import streamlit as st
import json
from jinja2 import Environment, FileSystemLoader
from interceptor import *
from parsers.parseProductFromJson import *
from parsers.parseFxRateFromJson import *
import os
from dotenv import load_dotenv
load_dotenv("appsettings.env")
API = os.getenv("API")

fxrates = requests.get(API+'FxRate')
if fxrates is not None:
    data_dict = json.loads(fxrates.text)
    fxratelist = parseFxRate(data_dict)


@st.dialog("Add Product")
def addProduct():
    name = st.text_input("Name")
    cost = int(st.number_input("Cost"))
    currency = st.text_input("Currency")
    fxRate = st.selectbox("Exchange Rate", (f for f in fxratelist), index=None)
    if st.button("Add product"):
        product = ProductDto(0, name, cost, currency, fxRate)
        print(to_json(product))
        send_with_bearer('/Product/', requests.post, to_json(product))


@st.dialog("Create quotation")
def createQuotation():
    
    if st.button("Create"):
        pass


st.title("Home Page")

data = requests.get(API + '/Product/')
if data is not None:
    try:
        if st.session_state.user.role == "admin":
            if st.button("Add product"):
                addProduct()
    except Exception:
        print(st.session_state)
    data_dict = json.loads(data.text)
    prod = parseProduct(data_dict)
    st.table([p.__dict__ for p in prod])

    if st.button("Create quotation"):
        createQuotation()

