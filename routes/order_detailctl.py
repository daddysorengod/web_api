from config.db import conn
from models.index import order_detaildb,objectsearch
from schemas.index import order_detail
from fastapi import APIRouter
from controllers import orderdetail_controller
order_detailctl = APIRouter()

@order_detailctl.get("/detail/")
async def getallorderdetail():
    return orderdetail_controller.getallorderdetail()

@order_detailctl.post("/detail_code")
async def getorderdetailbyid(code:objectsearch):
    return orderdetail_controller.getorderdetailbyodercode(code.key)

@order_detailctl.post("/detail/")
async def addoderdetail(newod:order_detail):
    conn.execute(order_detaildb.insert().values(
        order_detail_code = newod.order_detail_code,
        product_id = newod.product_id,
        order_detail_quantity = newod.order_detail_quantity
    ))
    return "them thanh cong"

@order_detailctl.put("/detail/{id}")
async def updateOrderdetail(id: int, newod: order_detail):
    conn.execute(order_detaildb.update().values(
        order_detail_code = newod.order_detail_code,
        product_id = newod.product_id,
        order_detail_quantity = newod.order_detail_quantity
    ))
    return "sua  thanh cong"

@order_detailctl.delete("/detail/{id}")
async def deleteoderdetail(id:int):
    conn.execute(order_detaildb.delete().where(order_detaildb.c.id==id))
    return "xoa thanh cong"