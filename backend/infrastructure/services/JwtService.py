import time
from datetime import datetime, timedelta, timezone
from typing import Annotated
import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
import os
from dotenv import load_dotenv
import pwdlib
from pydantic import BaseModel

load_dotenv("appsettings.env")
SECRET_KEY = os.getenv("SECRET")
ALGORITHM = os.getenv("ALGORITHM")
EXPIRATION = int(os.getenv("JWT_EXPIRATION"))
REFRESH_EXPIRATION = int(os.getenv("REFRESH_EXPIRATION"))

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

password_hash = pwdlib.PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class JwtService:

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return password_hash.hash(password)

    @staticmethod
    def create_access_token(data: dict):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=EXPIRATION)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def create_refresh_token(data: dict):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_EXPIRATION)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def decodeToken(token):
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
