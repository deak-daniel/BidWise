from model.StationDto import StationDto
import json

def parseStation(jsonData):
    output = []
    for j in jsonData:

        prod = StationDto(
            id = j["id"],
            name = j["name"]
        )
        output.append(prod)
    
    return output

def station_to_json(station_dto: StationDto):
    return {
        "id":station_dto.id, 
        "name":station_dto.name
    }