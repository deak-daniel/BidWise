from pydantic import BaseModel, Field

class TrainDto:    
    id: int = 0
    name: str = ""
    wagonNumber: int = 0
    price: float = 0.0
    
    def __init__(self, id, name, wagonNumber, price):
        self.id = id
        self.name = name
        self.wagonNumber = wagonNumber
        self.price = price

    def __str__(self):
        return f"{self.name} {self.wagonNumber} {self.price}"