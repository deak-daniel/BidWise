from backend.infrastructure.model.ShipmentDto import ShipmentDto
from backend.infrastructure.mappings.ShipmentMapper import ShipmentMapper
from backend.database.database import SessionLocal, engine, Base
from backend.infrastructure.entities.ShipmentBdo import ShipmentBdo
from sqlalchemy.orm import joinedload
from sqlalchemy import select

db = SessionLocal()

class ShipmentService:
    def get_shipments():
            
        stmt = select(ShipmentBdo).options(
            joinedload(ShipmentBdo.source_station),
            joinedload(ShipmentBdo.dest_station),
            joinedload(ShipmentBdo.train),
            joinedload(ShipmentBdo.product)
        )
        shipments = db.scalars(stmt).unique().all()
        return shipments
    
    def get_shipment_id(source_id, dest_id, product_id):
        stmt = select(ShipmentBdo).options(
            joinedload(ShipmentBdo.source_station),
            joinedload(ShipmentBdo.dest_station),
            joinedload(ShipmentBdo.train),
            joinedload(ShipmentBdo.product)
        ).where(ShipmentBdo.sourceStationId == source_id and 
                ShipmentBdo.destStationId == dest_id and 
                ShipmentBdo.productId == product_id)
        shipments = db.scalars(stmt).all()
        print(shipments)
        return shipments
    
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