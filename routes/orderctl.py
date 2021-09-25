from fastapi import APIRouter
from config.db import conn
from models.index import orderdb
from schemas.index import order
from controllers import order_controller

orderctl = APIRouter()

@orderctl.get("/order")
async def showAllorder():
    return order_controller.getallorder()

@orderctl.get("/order/{id}")
async def getOderbyID(id:int):
    return order_controller.getorderbyid(id)

@orderctl.get("/order/code/{order_code}")
async def getOderbyOrderCode(order_code:str):
    return order_controller.getorderbyordercode(order_code)

@orderctl.post("/order")
async def addoder(neworder: order):
    return order_controller.addneworder(neworder)

@orderctl.put("/orderupdate/{id}")
async def updateOrder(id: int, neworder:order):
    return order_controller.updateorderbyid(id, neworder)

@orderctl.delete("/orderdelete/{id}")
async def deleteorder(id: int):
    return order_controller.deleteorderbyid(id)