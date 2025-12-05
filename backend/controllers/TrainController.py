from typing import Annotated
from fastapi import FastAPI, Path, APIRouter
from backend.infrastructure.model.TrainDto import *
from backend.infrastructure.services.TrainService import *
from backend.infrastructure.wrapper.HttpMessage import HttpMessage
from backend.controllers.auth import *

router = APIRouter(
    prefix="/Train",
    tags=["Train"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
def get_all_trains():
    return TrainService.get_train()


@router.get("/{id}")
def get_train(id: Annotated[int, Path(title="The ID of the item to get")]):
    product = TrainService.get_train_id(id)
    return product


@router.post("/")
def add_or_update_train(train: TrainDto, user = Depends(get_current_user), role = Depends(is_admin)):
    TrainService.add_or_update_train(train)
    return HttpMessage("Train added")


@router.delete("/{id}")
def delete_train(id: Annotated[int, Path(title="The ID of the item to delete")], user = Depends(get_current_user), role = Depends( is_admin)):
    TrainService.delete_train(id)
    return HttpMessage("Train deleted")