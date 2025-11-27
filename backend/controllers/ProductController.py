from typing import Annotated
from fastapi import FastAPI, Path, APIRouter
from backend.infrastructure.model.ProductDto import *
from backend.infrastructure.services.ProductService import *
from backend.infrastructure.wrapper.HttpMessage import HttpMessage
from backend.controllers.auth import *

router = APIRouter(
    prefix="/Product",
    tags=["Product"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
def get_all_products():
    return ProductService.get_products()


@router.get("/{id}")
def get_product(id: Annotated[int, Path(title="The ID of the item to get")]):
    product = ProductService.get_product_id(id)
    return product


@router.post("/")
def add_or_update_product(product: ProductDto, user = Depends(get_current_user), role = Depends( is_admin)):
    ProductService.add_or_update_product(product)
    return HttpMessage("Product added")


@router.delete("/{id}")
def add_or_update_product(id: Annotated[int, Path(title="The ID of the item to delete")], user = Depends(get_current_user), role = Depends( is_admin)):
    ProductService.delete_product(id)
    return HttpMessage("Product deleted")
