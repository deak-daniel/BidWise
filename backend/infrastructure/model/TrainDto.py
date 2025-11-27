from pydantic import BaseModel, Field

class TrainDto(BaseModel):    
    id: int = 0
    name: str = ""
    wagonNumber: int = 0
    price: float = 0.0
    
    class Config:
        orm_mode = True