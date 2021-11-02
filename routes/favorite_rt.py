from fastapi import APIRouter
from controllers import favorite_controller
from schemas.index import favorite

favorite_rt = APIRouter()

@favorite_rt.get('/favorite/{id}')
async def getall(id: int):
    return favorite_controller.getfavoritebyiduser(id)

@favorite_rt.post('/favorite')
async def addfavorite(newfavorite: favorite):
    return favorite_controller.addnewfavorite(newfavorite)

@favorite_rt.delete('/favorite/{id}')
async def removefavorite(id: int):
    return favorite_controller.deletefavorite(id)

@favorite_rt.get('/favoriterandom/{id}')
async def getrandom(id: int):
    return favorite_controller.randomfavorite(id)

@favorite_rt.get('/favoriteall')
async def getFunc():
    return favorite_controller.getallfavorite()