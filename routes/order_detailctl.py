from config.db import conn
from models.index import order_detaildb
from schemas.index import order_detail,objectsearch
from fastapi import APIRouter
from controllers import orderdetail_controller

order_detailctl = APIRouter()

@order_detailctl.get("/detail")
async def getallorderdetail():
    return orderdetail_controller.getallorderdetail()

@order_detailctl.post("/detail_code")
async def getorderdetailbyid(code:objectsearch):
    return orderdetail_controller.getorderdetailbyodercode(code.key)

@order_detailctl.post("/detail")
async def addoderdetail(newod:order_detail):
    return orderdetail_controller.addOrderdetail(newod)

@order_detailctl.put("/detail/{id}")
async def updateOrderdetail(id: int, newod: order_detail):
    return orderdetail_controller.updateOrderdetail(id,newod)

@order_detailctl.delete("/detail/{id}")
async def deleteoderdetail(id:int):
    return orderdetail_controller.deleteorderbyid(id)