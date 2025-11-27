from sqlalchemy import Column, Integer, String
from backend.database.database import Base

class ShipmentBdo(Base):
    __tablename__ = "shipment"
    __table_args__ = {"sqlite_autoincrement": True}
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    sourceStationId = Column(Integer,  nullable=False)
    destStationId = Column(Integer, nullable=False)
    trainId = Column(Integer,  nullable=False)
    
    def __init__(self, name, sourceId, destId, trainId):
        self.name = name
        self.sourceStationId = sourceId
        self.destStationId = destId
        self.trainId = trainId