from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from backend.database.database import Base

class ShipmentBdo(Base):
    __tablename__ = "Shipment"
    __table_args__ = {"sqlite_autoincrement": True}
    
    id = Column(Integer, primary_key=True, index=True)
    sourceStationId = Column(Integer, ForeignKey('Station.id'), nullable=False)
    destStationId = Column(Integer, ForeignKey('Station.id'), nullable=False)
    trainId = Column(Integer, ForeignKey('Train.id'), nullable=False)
    productId = Column(Integer, ForeignKey('Product.id'), nullable=False)
    source_station = relationship("StationBdo", foreign_keys=[sourceStationId], back_populates="source_shipments")
    dest_station = relationship("StationBdo", foreign_keys=[destStationId], back_populates="dest_shipments")
    train = relationship("TrainBdo", back_populates="shipments")
    product = relationship("ProductBdo", back_populates="shipments")
    
    def __init__(self, sourceId, destId, trainId, productId):
        self.sourceStationId = sourceId
        self.destStationId = destId
        self.trainId = trainId
        self.productId = productId