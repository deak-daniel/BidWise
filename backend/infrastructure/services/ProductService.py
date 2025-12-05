from backend.infrastructure.model.ProductDto import ProductDto
from backend.infrastructure.mappings.ProductMapper import ProductMapper
from backend.database.database import SessionLocal, engine, Base
from backend.infrastructure.entities.ProductBdo import ProductBdo
from sqlalchemy.orm import selectinload

db = SessionLocal()

class ProductService:
    def get_products():
        return db.query(ProductBdo).all()
    
    def get_product_id(id: int):
        return db.query(ProductBdo).filter(ProductBdo.id == id).first()
    
    def add_or_update_product(product: ProductDto):
        entity_db = db.query(ProductBdo).filter(ProductBdo.id == product.id).first()
        if entity_db is None:
            entity = ProductMapper.to_product_bdo(product)
            db.add(entity)
        else:    
            entity = ProductMapper.to_product_bdo(product)
        db.commit()

    def delete_product(id: int):
        entity_db = db.query(ProductBdo).filter(ProductBdo.id == id).first()
        db.delete(entity_db)
        db.commit()