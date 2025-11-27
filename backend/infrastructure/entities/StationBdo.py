from sqlalchemy import Column, Integer, String
from backend.database.database import Base

class StationBdo(Base):
    __tablename__ = "station"
    __table_args__ = {"sqlite_autoincrement": True}
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    
    def __init__(self, name):
        self.name = name