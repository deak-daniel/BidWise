from model.TrainDto import TrainDto
import json

def parseTrain(jsonData):
    output = []
    for j in jsonData:

        prod = TrainDto(
            id = j["id"],
            name = j["name"],
            wagonNumber = j["wagonNumber"],
            price = j["price"],
        )
        output.append(prod)
    
    return output

def to_json(train_dto: TrainDto):
    return {
        "id":train_dto.id, 
        "name":train_dto.name, 
        "price":train_dto.price, 
        "wagonNumber":train_dto.wagonNumber, 
    }