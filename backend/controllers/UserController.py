from fastapi import APIRouter, Cookie, Response
from backend.infrastructure.model.UserDto import *
from backend.infrastructure.services.UserService import *
from backend.controllers.auth import *

router = APIRouter(
    prefix="/User",
    tags=["User"],
    responses={404: {"description": "Not found"}}
)

@router.post("/Register")
def create_user(user: UserDto):
    UserService.create_user_async(user, db)
    return  

@router.post("/Refresh")
def refresh_token(refresh_token: str = Cookie(None)):
    if refresh_token is None:
        raise HTTPException(401, "No refresh token")

    try:
        payload = JwtService.decodeToken(refresh_token)
        user = payload["sub"]
        role = payload["role"]
    except:
        raise HTTPException(401, "Invalid refresh token")

    new_access = JwtService.create_access_token(data={"sub": user, "role":role})
    return {"access_token": new_access}

@router.post("/Login")
def login(body: UserDto, response: Response):
    user = UserService.authenticate_user(body.username, body.password)
    if user == False:
        raise HTTPException(
            405,
            "Wrong credentials"
        )
    access = JwtService.create_access_token(data={"sub": user.username, "role":user.role})
    refresh = JwtService.create_refresh_token(data={"sub": user.username, "role":user.role})

    response.set_cookie(
        key="refresh_token",
        value=refresh,
        httponly=True,
        secure=False, 
        samesite="lax",
        max_age=60*60*24*7,
    )
    return Token(access_token=access, token_type="bearer")


@router.get("/Me")
def me(username: Annotated[str, Depends(get_current_user)]):
    user = db.query(UserBdo).filter(UserBdo.username == username).first()
    return user