from sqlalchemy import Column, Integer, String, Double, DateTime
from backend.database.database import Base

class CreatedQuotationBdo(Base):
    __tablename__ = "Created_quotation"
    __table_args__ = {"sqlite_autoincrement": True}
    
    id = Column(Integer, primary_key=True, index=True)
    clientName = Column(String, unique=True, nullable=False)
    price = Column(Double, unique=True, nullable=False)
    currency = Column(String, unique=True, nullable=False)
    date = Column(DateTime, unique=True, nullable=False)
    
    def __init__(self, clientName, price, currency, date):
        self.clientName = clientName
        self.price = price
        self.currency = currency
        self.date = date