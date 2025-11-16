from sqlalchemy import Column, Integer, String, Double, ForeignKey
from sqlalchemy.orm import relationship
from backend.database.database import Base

class ProductBdo(Base):
    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cost = Column(Double, nullable=False)
    fxRateId = Column(Integer, ForeignKey("fxRate.id"))
    fxRate = relationship("FxRateBdo", back_populates="product")
    
    def __init__(self, id, name, cost, fxRateId):
        self.id = id
        self.name = name
        self.cost = cost
        self.fxRateId = fxRateId