from pydantic.dataclasses import dataclass

@dataclass
class FxRateDto():
    id: int = 0
    fromCurrency: str = ""
    toCurrency: str = ""
    rate: float = ""