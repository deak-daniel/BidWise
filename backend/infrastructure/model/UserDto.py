from pydantic.dataclasses import dataclass

@dataclass
class UserDto:
    def __init__(self):
        id: int = 0
        username: str = ""
        password: str = ""
        role: str = ""