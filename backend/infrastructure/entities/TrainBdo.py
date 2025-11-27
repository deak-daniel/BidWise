from sqlalchemy import Column, Integer, String, Double
from backend.database.database import Base

class TrainBdo(Base):
    __tablename__ = "train"
    __table_args__ = {"sqlite_autoincrement": True}
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    wagonNumber = Column(Integer, nullable=False)
    price = Column(Double, nullable=False)
    
    def __init__(self, name, wagonNumber, price):
        self.name = name
        self.wagonNumber = wagonNumber
        self.price = price