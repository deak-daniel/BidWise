from model.ProductDto import ProductDto
from model.FxRateDto import FxRateDto
import json

def parseProduct(jsonData):
    output = []
    for j in jsonData:

        prod = ProductDto(
            id = j["id"],
            name = j["name"],
            price = j["price"],
            weight = j["weight"],
        )
        output.append(prod)
    
    return output

def product_to_json(product_dto: ProductDto):
    return {
        "id":product_dto.id, 
        "name":product_dto.name, 
        "price":product_dto.price, 
        "weight":product_dto.weight, 
    }