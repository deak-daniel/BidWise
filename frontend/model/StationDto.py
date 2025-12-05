from pydantic import BaseModel, Field

class StationDto:    
    id: int = 0
    name: str = ""
    
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.name}"