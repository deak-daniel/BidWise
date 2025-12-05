
class FxRateDto():
    id: int = 0
    fromCurrency: str = ""
    toCurrency: str = ""
    rate: float = ""
    
    def __init__(self, id, fromCurrency, toCurrency, rate):
        self.id = id
        self.fromCurrency = fromCurrency
        self.toCurrency = toCurrency
        self.rate = rate

    def __str__(self):
        return f"{self.fromCurrency} {self.toCurrency} {self.rate}"