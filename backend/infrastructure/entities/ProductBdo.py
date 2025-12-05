from sqlalchemy import Column, Integer, String, Double, ForeignKey
from sqlalchemy.orm import relationship
from backend.database.database import Base

class ProductBdo(Base):
    __tablename__ = "Product"
    __table_args__ = {"sqlite_autoincrement": True}
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    weight = Column(Double, nullable=False)
    price = Column(Double, nullable=False)
    shipments = relationship("ShipmentBdo", back_populates="product")
    
    def __init__(self, id, name, weight, price):
        self.id = id
        self.name = name
        self.weight = weight
        self.price = price