from typing import Union
from fastapi import FastAPI
from .controllers import ProductController
from .controllers import UserController
from .controllers import FxRateController
from .controllers import ShipmentController
from .controllers import StationController
from .controllers import TrainController

app = FastAPI()


app.include_router(ProductController.router)
app.include_router(UserController.router)
app.include_router(FxRateController.router)
app.include_router(ShipmentController.router)
app.include_router(StationController.router)
app.include_router(TrainController.router)