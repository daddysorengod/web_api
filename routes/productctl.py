from fastapi import APIRouter
from config.db import conn
from models.index import productdb,categorydb
from schemas.index import product,objectsearch
from controllers import product_controller

productctl = APIRouter()

@productctl.get("/product")
async def showallproduct():
    return product_controller.getallproduct()

@productctl.get("/product/{id}")
async def findproductbyID(id: int):
    return product_controller.getproductbyID(id)

@productctl.post("/product/searchname")
async def findproductbyName(name:objectsearch):
    return product_controller.getproductbyname(name.key)

@productctl.post("/product")
async def addproduct(newproduct: product):
    return product_controller.addproduct(newproduct)


@productctl.put("/product/update/{id}")
async def updateproduct(id: int, newproduct:product):
    return product_controller.updateproduct(id,newproduct)

@productctl.delete("/product/{id}")
async def deleteProduct(id: int):
    return product_controller.deleteproduct(id)