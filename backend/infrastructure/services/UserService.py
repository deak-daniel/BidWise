from backend.infrastructure.model.UserDto import UserDto
from backend.infrastructure.mappings.user_mapper import *
from sqlalchemy.orm import Session
import hashlib
from backend.infrastructure.services.JwtService import *

db = Session()

class UserService:
    @staticmethod
    def authenticate_user(username: str, password: str):
        user = db.query().filter(UserBdo.username == username).all()
        if not user:
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user

    @staticmethod
    def create_user_async(user: UserDto, db: Session) -> dict[str,str]:
        password = user.password.encode('utf-8')
        hashed = hashlib.sha256(password).hexdigest()
        user.password = hashed
        entity = to_user_bdo(user)
        db.add(entity)
        db.commit()
        access_token = create_access_token(data={"sub": entity.username})
        return access_token

