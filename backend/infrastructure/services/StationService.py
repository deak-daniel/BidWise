from backend.infrastructure.model.StationDto import StationDto
from backend.infrastructure.mappings.StationMapper import StationMapper
from backend.database.database import SessionLocal, engine, Base
from backend.infrastructure.entities.StationBdo import StationBdo
from sqlalchemy.orm import selectinload

db = SessionLocal()

class StationService:
    def get_stations():
        return db.query(StationBdo).all()
    
    def get_station_id(id: int):
        return db.query(StationBdo).filter(StationBdo.id == id).first()
    
    def add_or_update_station(shipment: StationDto):
        entity_db = db.query(StationBdo).filter(StationBdo.id == shipment.id).first()
        if entity_db is None:
            entity = StationMapper.to_station_bdo(shipment)
            db.add(entity)
        else:    
            entity = StationMapper.to_station_bdo(shipment)
        db.commit()

    def delete_station(id: int):
        entity_db = db.query(StationBdo).filter(StationBdo.id == id).first()
        db.delete(entity_db)
        db.commit()