from typing import Annotated
from fastapi import FastAPI, Path, APIRouter
from backend.infrastructure.model.StationDto import *
from backend.infrastructure.services.StationService import *
from backend.infrastructure.wrapper.HttpMessage import HttpMessage
from backend.controllers.auth import *

router = APIRouter(
    prefix="/Station",
    tags=["Station"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
def get_all_stations():
    return StationService.get_stations()


@router.get("/{id}")
def get_station(id: Annotated[int, Path(title="The ID of the item to get")]):
    product = StationService.get_station_id(id)
    return product


@router.post("/")
def add_or_update_station(station: StationDto, user = Depends(get_current_user), role = Depends(is_admin)):
    StationService.add_or_update_station(station)
    return HttpMessage("Station added")


@router.delete("/{id}")
def delete_station(id: Annotated[int, Path(title="The ID of the item to delete")], user = Depends(get_current_user), role = Depends( is_admin)):
    StationService.delete_station(id)
    return HttpMessage("Station deleted")