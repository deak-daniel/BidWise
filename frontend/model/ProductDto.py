from model.FxRateDto import FxRateDto

class ProductDto():    
    id: int = 0
    name: str = ""
    weight: float = 0.0
    price: float = 0.0
    
    def __init__(self, id, name, weight, price):
        self.id = id
        self.name = name
        self.price = price
        self.weight = weight
    
    def __str__(self):
        return f"{self.name} {self.weight} {self.price}"