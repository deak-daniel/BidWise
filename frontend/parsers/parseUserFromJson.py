from model.UserDto import UserDto
import json

def parseUser(jsonData):
    prod = UserDto(
        id = jsonData["id"],
        username = jsonData["username"],
        password="",
        role = jsonData["role"]
    )
    
    return prod
