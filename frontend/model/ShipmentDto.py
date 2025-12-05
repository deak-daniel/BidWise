from pydantic import BaseModel, Field
from .ProductDto import ProductDto
from .StationDto import StationDto
from .TrainDto import TrainDto

class ShipmentDto:    
    id: int = 0
    sourceStationId: int = 0
    destStationId: int = 0
    trainId: int = 0
    productId: int = 0
    product: ProductDto
    train: TrainDto
    sourceStation: StationDto
    destStation: StationDto
    
    def __init__(self, id, sourceStationId, destStationId, trainId, productId):
        self.id = id
        self.sourceStationId = sourceStationId
        self.destStationId = destStationId
        self.trainId = trainId
        self.productId = productId
        self.train = TrainDto
        self.product = ProductDto
        self.sourceStation = StationDto
        self.destStation = StationDto

    def __str__(self):
        return f"{self.id} {self.train.name} {self.product.name} {self.sourceStation.name} {self.destStation.name}"
    