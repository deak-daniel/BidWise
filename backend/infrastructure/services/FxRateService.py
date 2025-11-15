from backend.infrastructure.mappings.FxRateMapper import FxRateMapper
from backend.database.database import SessionLocal, engine, Base
from backend.infrastructure.entities.FxRateBdo import FxRateBdo
from backend.infrastructure.model.FxRateDto import FxRateDto

db = SessionLocal()

class FxRateService:
    def get_fx_rates():
        return db.query(FxRateBdo).all()
    
    def get_fx_rate_id(id: int):
        return db.query(FxRateBdo).filter(FxRateBdo.id == id).first()
    
    def add_or_update_fx_rate(product: FxRateBdo):
        entity_db = db.query(FxRateBdo).filter(FxRateBdo.id == product.id).first()
        if entity_db is None:
            entity = FxRateMapper.to_fx_rate_bdo(product)
            db.add(entity)
        else:    
            entity = FxRateMapper.to_fx_rate_bdo(product)
        db.commit()

    def delete_fx_rate(id: int):
        entity_db = db.query(FxRateBdo).filter(FxRateBdo.id == id).first()
        db.delete(entity_db)
        db.commit()