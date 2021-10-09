from fastapi import APIRouter
from schemas.index import order,objectsearch
from controllers import order_controller

order_rt = APIRouter()

@order_rt.get("/order")
async def showAllorder():
    return order_controller.getallorder()

@order_rt.get("/order/{id}")
async def getOderbyID(id: int):
    return order_controller.getorderbyid(id)

@order_rt.get("/order/code/{order_code}")
async def getOderbyOrderCode(order_code:str):
    return order_controller.getorderbyordercode(order_code)

@order_rt.post("/order")
async def addoder(neworder: order):
    return order_controller.addneworder(neworder)

@order_rt.put("/orderupdate/{id}")
async def updateOrder(id: int, neworder:order):
    return order_controller.updateorderbyid(id, neworder)

@order_rt.delete("/orderdelete/{id}")
async def deleteorder(id: int):
    return order_controller.deleteorderbyid(id)

@order_rt.post("/order/filterdate")
async def filterdate(date:objectsearch):
    return order_controller.filterbydate(date.key)