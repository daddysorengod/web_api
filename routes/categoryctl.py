from schemas.Objectsearch import objectsearch
from fastapi import APIRouter
# from sqlalchemy import lo
from config.db import conn 
from models.index import categorydb
from schemas.index import category
from controllers import category_controller

categoryctl = APIRouter()

@categoryctl.get("/category")
async def showallcategory():
    return category_controller.getallcategory()

@categoryctl.get("/category/{id}")
async def findCategorybyid(id:int):
    return category_controller.getcategorybyid(id)

@categoryctl.post("/category/searchname")
async def findCategorybyName(name:objectsearch):
    return category_controller.getcategorybyname(name.key)

@categoryctl.post("/category")
async def addcategory(newcategory:category):
    return category_controller.addCategory(newcategory)
    
@categoryctl.put("/category/{id}")
async def updateDategory(id:int,newcategory:category):
    return category_controller.updatecategory(id,newcategory)


@categoryctl.delete("/category/{id}")
async def deletecategory(id: int):
    return category_controller.deleteCategory(id)


