class UserDto:
    id: int = 0
    username: str = ""
    password: str = ""
    role: str = ""

    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role