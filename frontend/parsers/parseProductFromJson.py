from model.ProductDto import ProductDto
from model.FxRateDto import FxRateDto
import json

def parseProduct(jsonData):
    output = []
    for j in jsonData:

        fxRate = FxRateDto(
            id = j["fxRate"]["id"],
            fromCurrency = j["fxRate"]["fromCurrency"],
            toCurrency = j["fxRate"]["toCurrency"],
            rate = j["fxRate"]["rate"],
        )
        prod = ProductDto(
            id = j["id"],
            name = j["name"],
            cost = j["cost"],
            currency = j["currency"],
            fxRate = fxRate
        )
        output.append(prod)
    
    return output

def to_json(product_dto: ProductDto):
    return {
        "id":product_dto.id, 
        "name":product_dto.name, 
        "cost":product_dto.cost, 
        "currency":product_dto.currency, 
        "fxRate":
        {
            "id":product_dto.fxRate.id, 
            "toCurrency":product_dto.fxRate.toCurrency,
            "fromCurrency":product_dto.fxRate.fromCurrency,
            "rate":product_dto.fxRate.rate
        }
    }