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
            fxRate = fxRate
        )
        output.append(prod)
    
    return output
