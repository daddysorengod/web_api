from fastapi import FastAPI
from routes.index import userctl,categoryctl,productctl


app = FastAPI()
app.include_router(userctl)
app.include_router(categoryctl)
app.include_router(productctl)
