from fastapi import FastAPI
from routes.index import userctl,categoryctl,productctl,orderctl,order_detailctl


app = FastAPI()
app.include_router(userctl)
app.include_router(categoryctl)
app.include_router(productctl)
app.include_router(orderctl)
app.include_router(order_detailctl)