from sqlalchemy import Column, Integer, String, Double
from backend.database.database import Base

class ProductBdo(Base):
    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cost = Column(Double, nullable=False)
    fxRateId = Column(Integer, nullable=False)
    
    def __init__(self, id, name, cost, fxRateId):
        self.id = id
        self.name = name
        self.cost = cost
        self.fxRateId = fxRateId