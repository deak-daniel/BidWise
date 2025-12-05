from sqlalchemy import Column, Integer, String, Double
from backend.database.database import Base
from sqlalchemy.orm import relationship

class FxRateBdo(Base):
    __tablename__ = "FxRate"
    __table_args__ = {"sqlite_autoincrement": True}
    
    id = Column(Integer, primary_key=True, index=True)
    fromCurrency = Column(String, nullable=False)
    toCurrency = Column(String, nullable=False)
    rate = Column(Double, nullable=False)
    
    def __init__(self, id, fromCurrency, toCurrency, rate):
        self.id = id
        self.fromCurrency = fromCurrency
        self.toCurrency = toCurrency
        self.rate = rate