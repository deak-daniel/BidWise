from typing import Annotated
from fastapi import FastAPI, Path
from backend.infrastructure.model.ProductDto import *
from backend.infrastructure.services.ProductService import *
from backend.infrastructure.wrapper.HttpMessage import HttpMessage

app = FastAPI()

@app.get("/Product")
def get_all_products():
    return ProductService.get_products()


@app.get("/Product/{id}")
def get_product(id: Annotated[int, Path(title="The ID of the item to get")]):
    product = ProductService.get_product_id(id)
    return product


@app.post("/Product")
def add_or_update_product(product: ProductDto):
    ProductService.add_or_update_product(product)
    return HttpMessage("Product added")


@app.delete("/Product/{id}")
def add_or_update_product(id: Annotated[int, Path(title="The ID of the item to delete")]):
    ProductService.delete_product(id)
    return HttpMessage("Product deleted")
