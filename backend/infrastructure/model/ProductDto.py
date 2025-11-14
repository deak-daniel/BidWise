from pydantic.dataclasses import dataclass

@dataclass
class ProductDto:    
    id: int = 0
    name: str = ""
    cost: float = 0.0
    fxRateId: int = 0