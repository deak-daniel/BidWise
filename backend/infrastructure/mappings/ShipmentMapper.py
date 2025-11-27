from backend.infrastructure.entities.ShipmentBdo import ShipmentBdo
from backend.infrastructure.model.ShipmentDto import ShipmentDto

class ShipmentMapper:

    @staticmethod
    def to_shipment_bdo(shipment_dto: ShipmentDto) -> ShipmentBdo:
        return ShipmentBdo(
            id = shipment_dto.id,
            sourceId = shipment_dto.sourceId,
            destId = shipment_dto.destId,
            trainId= shipment_dto.trainId
        )

    @staticmethod
    def to_shipment_dto(shipment_bdo: ShipmentBdo) -> ShipmentDto:
        return ShipmentDto(
            id = shipment_bdo.id,
            sourceId = shipment_bdo.sourceId,
            destId = shipment_bdo.destId,
            trainId= shipment_bdo.trainId
        )