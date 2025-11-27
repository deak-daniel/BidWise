from backend.infrastructure.model.ShipmentDto import ShipmentDto
from backend.infrastructure.mappings.ShipmentMapper import ShipmentMapper
from backend.database.database import SessionLocal, engine, Base
from backend.infrastructure.entities.ShipmentBdo import ShipmentBdo
from sqlalchemy.orm import selectinload

db = SessionLocal()

class ShipmentService:
    def get_shipments():
        return db.query(ShipmentBdo).all()
    
    def get_shipment_id(id: int):
        return db.query(ShipmentBdo).filter(ShipmentBdo.id == id).first()
    
    def add_or_update_shipment(shipment: ShipmentDto):
        entity_db = db.query(ShipmentBdo).filter(ShipmentBdo.id == shipment.id).first()
        if entity_db is None:
            entity = ShipmentMapper.to_shipment_bdo(shipment)
            db.add(entity)
        else:    
            entity = ShipmentMapper.to_shipment_bdo(shipment)
        db.commit()

    def delete_shipment(id: int):
        entity_db = db.query(ShipmentBdo).filter(ShipmentBdo.id == id).first()
        db.delete(entity_db)
        db.commit()