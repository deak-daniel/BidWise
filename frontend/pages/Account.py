import requests
import streamlit as st
import pandas as pd
from interceptor import *
import json
import os
import asyncio
from parsers.parseUserFromJson import *
from parsers.parseFxRateFromJson import *
from parsers.parseProductFromJson import *
from parsers.parseShipmentFromJson import *
from parsers.parseTrainFromJson import *
from parsers.parseStationFromJson import *
from model.UserDto import UserDto
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv


load_dotenv("appsettings.env")
API = os.getenv("API")

@st.cache_data()
def get_trains():
    trains = requests.get(API + '/Train/')
    trains_dict = json.loads(trains.text)
    trains_clean = parseTrain(trains_dict)
    return [[t.id, t.name, t.wagonNumber, t.price] for t in trains_clean]

@st.cache_data()
def get_stations():
    stations = requests.get(API + '/Station/')
    stations_dict = json.loads(stations.text)
    stations_clean = parseStation(stations_dict)
    return [[t.id, t.name] for t in stations_clean]

@st.cache_data()
def get_shipments():
    shipments = requests.get(API + '/Shipment/')
    shipments_dict = json.loads(shipments.text)
    shipments_clean = parseShipment(shipments_dict)
    return shipments_clean

@st.cache_data()
def get_products():
    products = requests.get(API + '/Product/')
    products_dict = json.loads(products.text)
    products_clean = parseProduct(products_dict)
    return [[t.id, t.name, t.price, t.weight] for t in products_clean]

@st.cache_data()
def get_fxRates():
    fxRates = requests.get(API + '/FxRate/')
    fxRates_dict = json.loads(fxRates.text)
    fxRates_clean = parseFxRate(fxRates_dict)
    return [[t.id, t.fromCurrency, t.toCurrency, t.rate] for t in fxRates_clean]

def get_item_by_function(enumerable, func):
    index = 0
    while index < len(enumerable) and (not func(enumerable[index])):
        index+=1
    if index < len(enumerable):
        return enumerable[index]
    else:
        return object

def logout():
    if 'token' in st.session_state:
        del st.session_state.token
        
    if 'user' in st.session_state:
        del st.session_state.user
        
    st.success("You have been logged out.")
    
    st.rerun()


st.title("Account")
try:
    if st.session_state.token != "":
        if st.button("Log Out", type="primary"):
            logout()

            
        data = send_with_bearer('/User/Me', requests.get) 
        if data is not None:
            trains = get_trains()
            products = get_products()
            stations = get_stations()
            fxRates = get_fxRates()
            shipments = get_shipments()
            for s in shipments:
                t = get_item_by_function(trains, lambda x: x[0] == s.trainId)
                s.train = TrainDto(t[0], t[1], t[2], t[3])  
                prod = get_item_by_function(products, lambda x: x[0] == s.productId)
                s.product = ProductDto(prod[0], prod[1], prod[2], prod[3])
                source = get_item_by_function(stations,lambda x: x[0] == s.sourceStationId) 
                s.sourceStation = StationDto(source[0], source[1])
                dest = get_item_by_function(stations, lambda x: x[0] == s.destStationId)
                s.destStation = StationDto(dest[0], dest[1])

            data_dict = json.loads(data.text)
            user = parseUser(data_dict)
            st.session_state.user = user
            st.markdown(f"""
                User name: {user.username} \n
                Role: {user.role}
            """)

            st.text("Trains")
            trains_df = pd.DataFrame(trains)
            edited_trains_df = st.data_editor(trains_df, column_config={
                "0": st.column_config.Column(
                    "Train Id",
                    help="The train's id",
                    width="small",
                    required=True,
                ),
                "1":st.column_config.Column(
                    "Name",
                    help="The train name",
                    width="small",
                    required=True,
                ),
                "2":st.column_config.Column(
                    "Wagons",
                    help="The number of wagons",
                    width="small",
                    required=True,
                ),
                "3":st.column_config.Column(
                    "Price",
                    help="The prince to get this train",
                    width="small",
                    required=True,
                )
            }, num_rows="dynamic")
            
            st.text("Shipments")
            shipments_df = pd.DataFrame([[s.id, s.sourceStation.name, s.destStation.name, s.train.name, s.product.name] for s in shipments])
            edited_shipments_df = st.data_editor(shipments_df,column_config={
                "0": st.column_config.Column(
                    "Train Id",
                    width="small",
                    required=True,
                ),
                "1":st.column_config.Column(
                    "Name",
                    width="small",
                    required=True,
                ),
                "2":st.column_config.Column(
                    "Wagons",
                    width="small",
                    required=True,
                ),
                "3":st.column_config.Column(
                    "Price",
                    width="small",
                    required=True,
                ),
                "4":st.column_config.Column(
                    "Product",
                    width="small",
                    required=True,
                )
            }, num_rows="dynamic")

            st.text("Products")
            products_df = pd.DataFrame(products)
            edited_products_df = st.data_editor(products_df,column_config={
                "0": st.column_config.Column(
                    "Product Id",
                    width="small",
                    required=True,
                ),
                "1":st.column_config.Column(
                    "Name",
                    width="small",
                    required=True,
                ),
                "2":st.column_config.Column(
                    "Price",
                    width="small",
                    required=True,
                ),
                "3":st.column_config.Column(
                    "Weight (tonnes)",
                    width="small",
                    required=True,
                )
            }, num_rows="dynamic")

            st.text("Stations")
            stations_df = pd.DataFrame(stations)
            edited_stations_df = st.data_editor(stations_df,column_config={
                "0": st.column_config.Column(
                    "Station Id",
                    help="The station's id",
                    width="small",
                    required=True,
                ),
                "1":st.column_config.Column(
                    "Name",
                    help="The station name",
                    width="small",
                    required=True,
                )
            }, num_rows="dynamic")
            
            st.text("Exchange Rates")
            fxRates_df = pd.DataFrame(fxRates)
            edited_fxRates_df = st.data_editor(fxRates_df,column_config={
            "0": st.column_config.Column(
                "Exchange Id",
                help="The exchange's id",
                width="small",
                required=True,
            ),
            "1":st.column_config.Column(
                "From",
                help="Currency we are converting from",
                width="small",
                required=True,
            ),
            "2":st.column_config.Column(
                "To",
                help="Currency we are converting to",
                width="small",
                required=True,
            ),
            "3":st.column_config.Column(
                "Rate",
                help="The rate at which we convert",
                width="small",
                required=True,
            )
        }, num_rows="dynamic")
except:
    st.text("You are not logged in")

