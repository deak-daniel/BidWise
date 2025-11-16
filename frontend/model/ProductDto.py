from model.FxRateDto import FxRateDto

class ProductDto():    
    id: int = 0
    name: str = ""
    cost: float = 0.0
    fxRate: FxRateDto 
    
    def __init__(self, id, name, cost, fxRate):
        self.id = id
        self.name = name
        self.cost = cost
        self.fxRate = fxRate
    
    def __str__(self):
        return f"{self.name} {self.cost} {self.fxRate}"