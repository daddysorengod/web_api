from schemas.index import order_detail,objectsearch
from fastapi import APIRouter
from controllers import orderdetail_controller

order_detail_rt = APIRouter()

@order_detail_rt.get("/detail")
async def getallorderdetail():
    return orderdetail_controller.getallorderdetail()

@order_detail_rt.post("/detail_code")
async def getorderdetailbyid(code:objectsearch):
    return orderdetail_controller.getorderdetailbyodercode(code.key)

@order_detail_rt.post("/detail")
async def addoderdetail(newod:order_detail):
    return orderdetail_controller.addOrderdetail(newod)

@order_detail_rt.put("/detail/{id}")
async def updateOrderdetail(id: int, newod: order_detail):
    return orderdetail_controller.updateOrderdetail(id,newod)

@order_detail_rt.delete("/detail/{id}")
async def deleteoderdetail(id:int):
    return orderdetail_controller.deleteorderbyid(id)

