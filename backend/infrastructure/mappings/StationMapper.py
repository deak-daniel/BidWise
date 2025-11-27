from backend.infrastructure.entities.StationBdo import StationBdo
from backend.infrastructure.model.StationDto import StationDto

class StationMapper:

    @staticmethod
    def to_station_bdo(station_dto: StationDto) -> StationBdo:
        return StationBdo(
            id = station_dto.id,
            name = station_dto.name
        )

    @staticmethod
    def to_station_dto(station_bdo: StationBdo) -> StationDto:
        return StationDto(
            id = station_bdo.id,
            name = station_bdo.name
        )