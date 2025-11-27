from backend.infrastructure.model.UserDto import UserDto
from backend.infrastructure.mappings.UserMapper import UserMapper
from backend.database.database import SessionLocal, engine, Base
from backend.infrastructure.entities.UserBdo import UserBdo
import hashlib
from backend.infrastructure.services.JwtService import *

db = SessionLocal()

class UserService:
    @staticmethod
    def authenticate_user(username: str, password: str):
        user = db.query(UserBdo).filter(UserBdo.username == username).first()
        if not user:
            return False
        if not JwtService.verify_password(password, user.password):
            return False
        return user

    @staticmethod
    def create_user_async(user: UserDto, db) -> dict[str,str]:
        user.password = JwtService.get_password_hash(user.password)
        entity = UserMapper.to_user_bdo(user)
        db.add(entity)
        db.commit()

