from pydantic.dataclasses import dataclass

@dataclass
class UserDto:
    id: int = 0
    username: str = ""
    password: str = ""
    role: str = ""