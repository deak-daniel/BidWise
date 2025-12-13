from typing import Annotated
from fastapi import FastAPI, Path, APIRouter
from backend.infrastructure.model.ShipmentDto import *
from backend.infrastructure.services.ShipmentService import *
from backend.infrastructure.wrapper.HttpMessage import HttpMessage
from backend.controllers.auth import *

router = APIRouter(
    prefix="/Shipment",
    tags=["Shipment"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
def get_all_shipments():
    return ShipmentService.get_shipments()


@router.get("/{source_id}/{dest_id}/{product_id}")
def get_shipment(source_id: Annotated[int, Path(title="Source station id")], dest_id: Annotated[int, Path(title="Destination station id")], product_id:  Annotated[int, Path(title="Product Id")]):
    shipment = ShipmentService.get_shipment_id(source_id, dest_id, product_id)
    return shipment


@router.post("/")
def add_or_update_shipment(shipment: ShipmentDto, user = Depends(get_current_user), role = Depends(is_admin)):
    ShipmentService.add_or_update_shipment(shipment)
    return HttpMessage("Shipment added")


@router.delete("/{id}")
def delete_shipment(id: Annotated[int, Path(title="The ID of the item to delete")], user = Depends(get_current_user), role = Depends( is_admin)):
    ShipmentService.delete_shipment(id)
    return HttpMessage("Shipment deleted")