from backend.infrastructure.entities.TrainBdo import TrainBdo
from backend.infrastructure.model.TrainDto import TrainDto

class TrainMapper:

    @staticmethod
    def to_train_bdo(train_dto: TrainDto) -> TrainBdo:
        return TrainBdo(
            id = train_dto.id,
            name = train_dto.name,
            wagonNumber = train_dto.wagonNumber,
            price = train_dto.price
        )

    @staticmethod
    def to_train_dto(train_bdo: TrainBdo) -> TrainDto:
        return TrainDto(
            id = train_bdo.id,
            name = train_bdo.name,
            wagonNumber = train_bdo.wagonNumber,
            price = train_bdo.price
        )