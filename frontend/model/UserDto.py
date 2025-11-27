class UserDto:
    id: int = 0
    username: str = ""
    password: str = ""
    role: str = ""

    def __init__(self, username, password, role = "", id = 0, ):
        self.id = id
        self.username = username
        self.password = password
        self.role = role