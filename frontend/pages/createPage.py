import streamlit as st
import json
from interceptor import *
from parsers.parseProductFromJson import *

st.title("My Streamlit Layout Example")
st.header("Section 1")
st.write("This content appears first.")
data = send_with_bearer('/Product/', requests.get)
data_dict = json.loads(data.text)
st.dataframe(data_dict)
prod = parseProduct(data_dict)
st.dataframe(prod)