from pydantic import BaseModel, Field

class FxRateDto(BaseModel):
    id: int = 0
    fromCurrency: str = ""
    toCurrency: str = ""
    rate: float = ""
    
    class Config:
        orm_mode = True