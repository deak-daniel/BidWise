from backend.database.database import Base, engine, SQLALCHEMY_DATABASE_URL
from backend.infrastructure.entities import UserBdo
import sqlite3

def main():
    print("Creating database")
    Base.metadata.create_all(bind=engine)
    print("Database created")

if __name__ == '__main__':
    main()