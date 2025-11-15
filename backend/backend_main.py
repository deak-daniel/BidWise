from typing import Union
from fastapi import FastAPI
from .controllers import ProductController
from .controllers import UserController
from .controllers import FxRateController

app = FastAPI()


app.include_router(ProductController.router)
app.include_router(UserController.router)
app.include_router(FxRateController.router)