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


# async def async_fetch_endpoint(client: httpx.AsyncClient, endpoint: str):
#     """Mocks an asynchronous API request using httpx."""
#     # In a real application, you would use:
#     # response = await client.get(f"{API}{endpoint}")
#     # response.raise_for_status()
#     # return response.json()
    
#     # Mocking the response directly from the dictionary
#     return MOCK_API_RESPONSES[endpoint]


# async def async_get_all_data(token: str):
#     """Fetches all necessary data concurrently."""
#     async with httpx.AsyncClient(base_url=API, headers={
#         "Authorization": f"Bearer {token}"
#     }) as client:
#         # Define all concurrent tasks
#         tasks = {
#             'user': async_fetch_endpoint(client, '/User/Me'),
#             'trains': async_fetch_endpoint(client, '/Train/'),
#             'stations': async_fetch_endpoint(client, '/Station/'),
#             'shipments': async_fetch_endpoint(client, '/Shipment/'),
#             'products': async_fetch_endpoint(client, '/Product/'),
#             'fxRates': async_fetch_endpoint(client, '/FxRate/'),
#         }

#         # Execute all tasks concurrently and wait for all results
#         results = await asyncio.gather(*tasks.values())
        
#         # Map results back to their keys
#         fetched_data = dict(zip(tasks.keys(), results))
        
#         return fetched_data



def get_trains():
    trains = requests.get(API + '/Train/')
    trains_dict = json.loads(trains.text)
    trains_clean = parseTrain(trains_dict)
    return [[t.id, t.name, t.wagonNumber, t.price] for t in trains_clean]

def get_stations():
    stations = requests.get(API + '/Station/')
    stations_dict = json.loads(stations.text)
    stations_clean = parseStation(stations_dict)
    return [[t.id, t.name] for t in stations_clean]

def get_shipments():
    shipments = requests.get(API + '/Shipment/')
    shipments_dict = json.loads(shipments.text)
    shipments_clean = parseShipment(shipments_dict)
    return shipments_clean

def get_products():
    products = requests.get(API + '/Product/')
    products_dict = json.loads(products.text)
    products_clean = parseProduct(products_dict)
    return [[t.id, t.name, t.price, t.weight] for t in products_clean]

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


st.title("Account")

if st.session_state.token != "":
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
        trains_df = pd.DataFrame(trains)
        edited_trains_df = st.data_editor(trains_df, num_rows="dynamic")

        shipments_df = pd.DataFrame([[s.id, s.sourceStation.name, s.destStation.name, s.train.name, s.product.name] for s in shipments])
        edited_shipments_df = st.data_editor(shipments_df, num_rows="dynamic")

        products_df = pd.DataFrame(products)
        edited_products_df = st.data_editor(products_df, num_rows="dynamic")

        stations_df = pd.DataFrame(stations)
        edited_stations_df = st.data_editor(stations_df, num_rows="dynamic")

        fxRates_df = pd.DataFrame(fxRates)
        edited_fxRates_df = st.data_editor(fxRates_df, num_rows="dynamic")


