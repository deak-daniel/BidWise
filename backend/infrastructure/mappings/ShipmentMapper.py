from backend.infrastructure.entities.ShipmentBdo import ShipmentBdo
from backend.infrastructure.model.ShipmentDto import ShipmentDto

class ShipmentMapper:

    @staticmethod
    def to_shipment_bdo(shipment_dto: ShipmentDto) -> ShipmentBdo:
        return ShipmentBdo(
            id = shipment_dto.id,
            sourceStationId = shipment_dto.sourceStationId,
            destStationId = shipment_dto.destStationId,
            trainId= shipment_dto.trainId,
            productId = shipment_dto.productId
        )

    @staticmethod
    def to_shipment_dto(shipment_bdo: ShipmentBdo) -> ShipmentDto:
        return ShipmentDto(
            id = shipment_bdo.id,
            sourceStationId = shipment_bdo.sourceId,
            destStationId = shipment_bdo.destStationId,
            trainId= shipment_bdo.trainId,
            productId = shipment_bdo.productId
        )