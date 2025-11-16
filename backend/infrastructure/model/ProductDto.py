from pydantic import BaseModel, Field
from backend.infrastructure.model.FxRateDto import FxRateDto

class ProductDto(BaseModel):    
    id: int = 0
    name: str = ""
    cost: float = 0.0
    fxRate: FxRateDto =  Field(default_factory=FxRateDto)
    
    class Config:
        orm_mode = True