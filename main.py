from backend.database.database import Base, engine, SQLALCHEMY_DATABASE_URL, seed_data
from backend.infrastructure.entities.ProductBdo import ProductBdo
from backend.infrastructure.entities.FxRateBdo import FxRateBdo
from backend.infrastructure.entities.UserBdo import UserBdo
from backend.infrastructure.entities.TrainBdo import TrainBdo
from backend.infrastructure.entities.ShipmentBdo import ShipmentBdo
from backend.infrastructure.entities.StationBdo import StationBdo
from backend.infrastructure.entities.CreatedQuotationBdo import CreatedQuotationBdo
import os
import sqlite3
from concurrent.futures import ThreadPoolExecutor
def start_backend():
    print("Starting backend")

def main():
    print("Creating database")
    Base.metadata.create_all(bind=engine)
    #seed_data()
    print("Database created")
    
    print("Starting backend and frontend")
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(lambda: os.system("fastapi dev ./backend/backend_main.py"))
        executor.submit(lambda: os.system("streamlit run ./frontend/Home.py"))

    

if __name__ == '__main__':
    main()