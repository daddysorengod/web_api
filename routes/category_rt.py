from schemas.Objectsearch import objectsearch
from fastapi import APIRouter
from schemas.index import category
from controllers import category_controller

category_rt = APIRouter()

@category_rt.get("/category")
async def showallcategory():
    return category_controller.getallcategory()

@category_rt.get("/category/{id}")
async def findCategorybyid(id:int):
    return category_controller.getcategorybyid(id)

@category_rt.post("/category/searchname")
async def findCategorybyName(name:objectsearch):
    return category_controller.getcategorybyname(name.key)

@category_rt.post("/category")
async def addcategory(newcategory:category):
    return category_controller.addCategory(newcategory)
    
@category_rt.put("/category/{id}")
async def updatecategory(id:int,newcategory:category):
    return category_controller.updateCategory(id,newcategory)


@category_rt.delete("/category/{id}")
async def deletecategory(id: int):
    return category_controller.deleteCategory(id)


