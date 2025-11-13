from typing import Union
from fastapi import FastAPI
from backend.database.database import SessionLocal, engine, Base
from backend.infrastructure.model.UserDto import *
from backend.infrastructure.services.UserService import *

app = FastAPI()
db = SessionLocal()
@app.post("/User/Register")
def create_user(user: UserDto):
    token = UserService.create_user_async(user, db)
    return token 


@app.post("/User/Login")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user = UserService.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return Token(access_token=access_token, token_type="bearer")