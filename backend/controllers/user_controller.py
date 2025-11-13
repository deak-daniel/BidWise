from typing import Union
from fastapi import FastAPI
from backend.database.database import SessionLocal, engine, Base
from backend.infrastructure.model.UserDto import *
from backend.infrastructure.services.user_service import *

app = FastAPI()
db = SessionLocal()
@app.post("User", response_model=UserDto)
async def create_user(user: UserDto):
    create_user_async(user, db)
    return         

@app.get("/")
async def greet():
    return {"message": "hello"}
        
