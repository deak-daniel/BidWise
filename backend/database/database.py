from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
from sqlalchemy.sql import text
load_dotenv("appsettings.env")
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_CONNECTION")


def seed_data():
    with SessionLocal() as session:
        session.execute(text("PRAGMA foreign_keys = ON;")) 
        session.execute(text("""INSERT INTO Train (id, name, wagonNumber, price) VALUES
                                (1, 'InterCity 901', 8, 15000.00),
                                (2, 'Cargo Express 22', 12, 85000.00);"""))
        session.execute(text("""INSERT INTO Station (id, name) VALUES
                                (1, 'Budapest-Kelenföld'),
                                (2, 'Munich Central'),
                                (3, 'Vienna Hauptbahnhof'),
                                (4, 'Debrecen');"""))
        
        session.execute(text("""INSERT INTO Product (id, name, weight, price) VALUES
                                (1, 'High-Value Electronics', 5.5, 120000.00),
                                (2, 'Bulk Wheat Grain', 150.0, 5000.00),
                                (3, 'Auto Parts', 25.0, 45000.00);"""))
        session.execute(text("""INSERT INTO FxRate (id, fromCurrency, toCurrency, rate) VALUES
                                (1, 'USD', 'HUF', 328.86),
                                (2, 'EUR', 'HUF', 381.56);"""))
        session.execute(text("""INSERT INTO Shipment (id, sourceStationId, destStationId, trainId, productId) VALUES
                                (1, 1, 2, 2, 1), 
                                (2, 3, 4, 1, 2),
                                (3, 2, 1, 2, 3);"""))
        session.commit()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

