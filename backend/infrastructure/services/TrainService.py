from backend.infrastructure.model.TrainDto import TrainDto
from backend.infrastructure.mappings.TrainMapper import TrainMapper
from backend.database.database import SessionLocal, engine, Base
from backend.infrastructure.entities.TrainBdo import TrainBdo
from sqlalchemy.orm import selectinload

db = SessionLocal()

class TrainService:
    def get_train():
        return db.query(TrainBdo).all()
    
    def get_train_id(id: int):
        return db.query(TrainBdo).filter(TrainBdo.id == id).first()
    
    def add_or_update_train(train: TrainBdo):
        entity_db = db.query(TrainBdo).filter(TrainBdo.id == train.id).first()
        if entity_db is None:
            entity = TrainMapper.to_train_bdo(train)
            db.add(entity)
        else:    
            entity = TrainMapper.to_train_bdo(train)
        db.commit()

    def delete_train(id: int):
        entity_db = db.query(TrainBdo).filter(TrainBdo.id == id).first()
        db.delete(entity_db)
        db.commit()