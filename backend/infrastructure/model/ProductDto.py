from pydantic import BaseModel, Field
from backend.infrastructure.model.FxRateDto import FxRateDto

class ProductDto(BaseModel):    
    id: int = 0
    name: str = ""
    weight: float = 0.0
    price: float = 0.0
    
    class Config:
        orm_mode = True