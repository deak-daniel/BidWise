from sqlalchemy import Column, Integer, String
from backend.database.database import Base

class UserBdo(Base):
    __tablename__ = "user"
    __table_args__ = {"sqlite_autoincrement": True}
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="admin")
    
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role