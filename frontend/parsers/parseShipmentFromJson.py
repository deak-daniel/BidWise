from model.ShipmentDto import ShipmentDto
import json

def parseShipment(jsonData):
    output = []
    for j in jsonData:

        prod = ShipmentDto(
            id = j["id"],
            sourceStationId = j["sourceStationId"],
            destStationId = j["destStationId"],
            trainId = j["trainId"],
            productId = j["productId"],
        )
        output.append(prod)
    

    return output

def station_to_json(shipment_dto: ShipmentDto):
    return {
        "id":shipment_dto.id, 
        "sourceStationId":shipment_dto.sourceStationId, 
        "destStationId":shipment_dto.destStationId, 
        "trainId":shipment_dto.trainId, 
        "productId":shipment_dto.productId, 
    }