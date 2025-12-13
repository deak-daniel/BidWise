import requests
import streamlit as st
import json
import pandas as pd
from interceptor import *
from parsers.parseProductFromJson import *
from parsers.parseFxRateFromJson import *
from parsers.parseStationFromJson import *
from parsers.parseShipmentFromJson import *
from parsers.parseTrainFromJson import *
import os
from dotenv import load_dotenv
load_dotenv("appsettings.env")
API = os.getenv("API")

@st.cache_data
def get_products():
    p = requests.get(API + '/Product/')
    products_dict = json.loads(p.text)
    products_clean = parseProduct(products_dict) 
    return [t for t in products_clean]

@st.cache_data
def get_fxrates():
    fxrates_response = requests.get(API+'FxRate')
    if fxrates_response.status_code == 200:
        data_dict = json.loads(fxrates_response.text)
        return parseFxRate(data_dict)
    return []

@st.cache_data
def get_stations():
    stations_response = requests.get(API + '/Station/')
    if stations_response.status_code == 200:
        stations_dict = json.loads(stations_response.text)
        return parseStation(stations_dict)
    return []

@st.cache_data
def get_trains():
    trains_response = requests.get(API + '/Train/')
    if trains_response.status_code == 200:
        trains_dict = json.loads(trains_response.text)
        return parseTrain(trains_dict)
    return []


def select(enumerable: list, predicate: Callable):
    output = []
    for i in enumerable:
        if predicate(i):
            output.append(i)
    return output

PRODUCTS = get_products() 
FXRATES = get_fxrates()
STATIONS = get_stations()
TRAINS = get_trains()


source_stations = STATIONS
dest_stations = STATIONS

@st.dialog("Add New Product")
def addProduct():
    st.subheader("Enter Product Details")
    name = st.text_input("Product Name", key="product_name_input")
    weight = st.number_input("Weight (tonnes)", min_value=0.0, step=0.01, format="%.2f", key="product_weight_input")
    price = st.number_input("Unit Price", min_value=0.0, step=0.01, format="%.2f", key="product_price_input")
    
    if st.button("Add Product to Catalog"):
        
        if not name or weight <= 0 or price <= 0:
            st.error("Please fill in all fields with positive values for weight and price.")
            return
        last_id = PRODUCTS[-1].id + 1
        product = ProductDto(
            id = last_id,
            name=name, 
            weight=int(weight), 
            price=int(price)
        )
        try:
            response = send_with_bearer('/Product/', requests.post, product_to_json(product))
            if response and response.status_code in [201, 200]:
                st.success(f"Product '{name}' added successfully!")
                get_products.clear()
                st.rerun() 
            else:
                st.error(f"Failed to add product. API responded with status: {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred while communicating with the API: {e}")


@st.dialog("Create quotation")
def createQuotation():
    source = st.selectbox("From", (s for s in source_stations), index=None)
    dest = st.selectbox("To", (d for d in dest_stations), index=None)
    product = st.selectbox("Product", (p for p in PRODUCTS), index=None)
    if st.button("Create"):
        shipment_response = requests.get(API + f"/Shipment/{source.id}/{dest.id}/{product.id}")
        
        if shipment_response.status_code != 200:
             st.error("Error fetching shipment data from API.")
             return
             
        shipment_dict = json.loads(shipment_response.text)
        shipment_clean = parseShipment(shipment_dict) 

        if not shipment_clean:
            st.warning("No available shipments found for this route.")
            return

        st.markdown("###  Available Quotations")

        quotation_data = []
        for shipment_dto in shipment_clean:
            train_list = select(TRAINS, lambda x: x.id == shipment_dto.trainId)
            train = train_list[0] if train_list else None
            
            if train:
                total_price = train.price + product.price
                
                quotation_data.append({
                    "Shipment ID": shipment_dto.id,
                    "Route": f"{source.name} → {dest.name}",
                    "Train Name": train.name,
                    "Train Price": train.price,
                    "Product Price": product.price,
                    "Total Price": total_price
                })
        
        if quotation_data:
            quotation_df = pd.DataFrame(quotation_data)
            
            st.dataframe(
                quotation_df, 
                width='stretch', 
                hide_index=True
            )
        else:
             st.warning("Could not calculate quotations due to missing train data.")


st.title("Home Page")
st.markdown("""
## 🌍 Welcome to BidWise!

This application is your central dashboard for managing and calculating efficient rail freight quotations. We leverage real-time data on products, trains, stations, and exchange rates to provide fast, accurate, and optimized shipping estimates.

### Why Choose Our Platform?

* **⚡ Instant Quotations:** Use the **'Create quotation'** feature below to instantly calculate the best shipping price and route between any two stations, factoring in the specific product weight and price.
* **🔗 Integrated Data:** All essential components—from **Product Specifications** (like weight and value, visible below) to **Available Trains** and **Exchange Rates**—are centrally managed and continuously updated via secure API access.
* **⚙️ Data-Driven Efficiency:** For authenticated administrators, the system provides full **CRUD (Create, Read, Update, Delete)** access on the 'Account' page, ensuring that all underlying data (Trains, Stations, Products, FxRates) is always accurate for optimal routing and pricing calculations.

Scroll down to view the current list of products in the catalog or click 'Create quotation' to begin calculating your next shipment!
***
""")

if PRODUCTS is not None:
    try:
        if st.session_state.user.role == "admin":
            if st.button("Add product"):
                addProduct()
    except Exception:    
        pass
    st.text("Products")
    products_df = pd.DataFrame([[t.id, t.name, t.price, t.weight] for t in PRODUCTS])
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
    }, hide_index=True)
    

    if st.button("Create quotation"):
        createQuotation()

