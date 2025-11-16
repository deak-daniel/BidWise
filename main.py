from backend.database.database import Base, engine, SQLALCHEMY_DATABASE_URL
from backend.infrastructure.entities.ProductBdo import ProductBdo
from backend.infrastructure.entities.FxRateBdo import FxRateBdo
from backend.infrastructure.entities.UserBdo import UserBdo
import os
import sqlite3
from concurrent.futures import ThreadPoolExecutor
def start_backend():
    print("Starting backend")

def main():
    print("Creating database")
    Base.metadata.create_all(bind=engine)
    print("Database created")
    
    print("Starting backend and frontend")
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(lambda: os.system("fastapi dev ./backend/backend_main.py"))
        executor.submit(lambda: os.system("streamlit run ./frontend/mainPage.py"))

    

if __name__ == '__main__':
    main()