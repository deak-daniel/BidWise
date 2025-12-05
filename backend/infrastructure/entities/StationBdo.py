from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.database.database import Base

class StationBdo(Base):
    __tablename__ = "Station"
    __table_args__ = {"sqlite_autoincrement": True}
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    source_shipments = relationship("ShipmentBdo", back_populates="source_station", foreign_keys="ShipmentBdo.sourceStationId")
    dest_shipments = relationship("ShipmentBdo", back_populates="dest_station", foreign_keys="ShipmentBdo.destStationId")
    
    def __init__(self, name):
        self.name = name