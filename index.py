from fastapi import FastAPI
from routes.index import userctl


app = FastAPI()
app.include_router(userctl)

