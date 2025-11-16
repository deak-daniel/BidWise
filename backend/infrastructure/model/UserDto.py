from pydantic import BaseModel, Field

class UserDto(BaseModel):
    id: int = 0
    username: str = ""
    password: str = ""
    role: str = ""