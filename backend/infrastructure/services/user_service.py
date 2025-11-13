from backend.infrastructure.model.UserDto import UserDto
from backend.infrastructure.mappings.user_mapper import *
from sqlalchemy.orm import Session
import hashlib


async def create_user_async(user: UserDto, db: Session):
    password = user.password.encode('utf-8')
    hashed = hashlib.sha256(password).hexdigest()
    user.password = hashed
    entity = to_user_bdo(user)
    await db.add(entity)

async def login(user: UserDto, db: Session):
    password = user.password.encode('utf-8')
    hashed = hashlib.sha256(password).hexdigest()
    user.password = hashed
    entity = to_user_bdo(user)
    results = db.filter(UserBdo.password == entity.password).all()
    

async def create_user_async(user: UserDto, db: Session):
    entity = to_user_bdo(user)
    await db.add(entity)
