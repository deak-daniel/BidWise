from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from backend.infrastructure.services.JwtService import *

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/User/Login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = JwtService.decodeToken(token)
        return payload["sub"]
    except:
        raise HTTPException(401, "Invalid or expired access token")

def is_admin(token: str = Depends(oauth2_scheme)):
    try:
        payload = JwtService.decodeToken(token)
    except:
        raise HTTPException(401, "Invalid or expired access token")
    
    if payload["role"] != "admin":
        raise HTTPException(403,"User not authorized")
    return payload["sub"]
