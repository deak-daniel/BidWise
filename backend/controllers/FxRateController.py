from typing import Annotated
from fastapi import Path, APIRouter
from backend.infrastructure.model.FxRateDto import *
from backend.infrastructure.services.FxRateService import FxRateService
from backend.infrastructure.wrapper.HttpMessage import HttpMessage

router = APIRouter(
    prefix="/FxRate",
    tags=["FX Rate"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
def get_all_fxRates():
    return FxRateService.get_fx_rates()


@router.get("/{id}")
def get_product(id: Annotated[int, Path(title="The ID of the item to get")]):
    product = FxRateService.get_fx_rate_id(id)
    return product


@router.post("/")
def add_or_update_product(fx_rate: FxRateDto):
    FxRateService.add_or_update_product(fx_rate)
    return HttpMessage("Product added")


@router.delete("/{id}")
def add_or_update_product(id: Annotated[int, Path(title="The ID of the item to delete")]):
    FxRateService.delete_fx_rate(id)
    return HttpMessage("Product deleted")
