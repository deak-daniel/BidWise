from pydantic import BaseModel, Field

class StationDto(BaseModel):    
    id: int = 0
    name: str = ""
    
    class Config:
        orm_mode = True