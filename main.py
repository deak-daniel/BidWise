from backend.database.database import Base, engine, SQLALCHEMY_DATABASE_URL
from backend.infrastructure.entities.ProductBdo import ProductBdo
from backend.infrastructure.entities.FxRateBdo import FxRateBdo
from backend.infrastructure.entities.UserBdo import UserBdo
import os
import sqlite3

def main():
    print("Creating database")
    Base.metadata.create_all(bind=engine)
    print("Database created")
    print("Starting backend")
    os.system("fastapi dev ./backend/backend_main.py")
    os.system("")
    

if __name__ == '__main__':
    main()