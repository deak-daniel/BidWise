from fastapi import APIRouter
from backend.infrastructure.model.UserDto import *
from backend.infrastructure.services.UserService import *

router = APIRouter(
    prefix="/User",
    tags=["User"],
    responses={404: {"description": "Not found"}}
)

@router.post("/Register")
def create_user(user: UserDto):
    token = UserService.create_user_async(user, db)
    return token 


@router.post("/Login")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user = UserService.authenticate_user(form_data.username, form_data.password)
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = JwtService.create_access_token(data={"sub": user.username})
    return Token(access_token=access_token, token_type="bearer")


@router.get("/me")
def me(token: Annotated[str, Depends(oauth2_scheme)]):
    user = UserService.me(token)
    return user