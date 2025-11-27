from model.FxRateDto import FxRateDto
import json

def parseFxRate(jsonData):
    output = []
    for j in jsonData:
        fxRate = FxRateDto(
            id = j["id"],
            fromCurrency = j["fromCurrency"],
            toCurrency = j["toCurrency"],
            rate = j["rate"]
        )
        output.append(fxRate)
    
    return output
