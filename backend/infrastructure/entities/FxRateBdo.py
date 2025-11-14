from sqlalchemy import Column, Integer, String, Double
from backend.database.database import Base

class FxRateBdo(Base):
    __tablename__ = "fxRate"
    
    id = Column(Integer, primary_key=True, index=True)
    fromCurrency = Column(String, nullable=False)
    toCurrency = Column(String, nullable=False)
    rate = Column(Double, nullable=False)
    
    def __init__(self, id, fromCurrency, toCurrency, rate):
        self.id = id
        self.fromCurrency = fromCurrency
        self.toCurrency = toCurrency
        self.rate = rate