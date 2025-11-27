from model.FxRateDto import FxRateDto

class ProductDto():    
    id: int = 0
    name: str = ""
    cost: float = 0.0
    currency: str = ""
    fxRate: FxRateDto 
    amountInBase: str = ""
    
    def __init__(self, id, name, cost,currency, fxRate):
        self.id = id
        self.name = name
        self.cost = cost
        self.currency = currency
        self.fxRate = fxRate
        self.amountInBase = f"{cost*fxRate.rate} {fxRate.toCurrency}"
    
    def __str__(self):
        return f"{self.name} {self.cost} {self.fxRate}"