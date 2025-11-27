from pydantic import BaseModel, Field

class ShipmentDto(BaseModel):    
    id: int = 0
    sourceStationId: int = 0
    destStationId: int = 0
    trainId: int = 0
    
    class Config:
        orm_mode = True