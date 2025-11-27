from backend.infrastructure.entities.UserBdo import UserBdo
from backend.infrastructure.model.UserDto import UserDto

class UserMapper:

    @staticmethod
    def to_user_bdo(user_dto) -> UserBdo:
        return UserBdo(
            username = user_dto.username,
            password = user_dto.password,
            role = user_dto.role
        )

    @staticmethod
    def to_user_dto(user_bdo) -> UserDto:
        return UserDto(
            id = user_bdo.id,
            username = user_bdo.username,
            password = user_bdo.password,
            role = user_bdo.role
        )

