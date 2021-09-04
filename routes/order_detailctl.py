from config.db import conn
from models.index import order_detaildb
from schemas.index import order_detail
from fastapi import APIRouter

order_detailctl = APIRouter()

@order_detailctl.get("/detail/")
async def getallorderdetail():
    sql = "select * from tbl_order_detail"
    return conn.execute(sql).fetchall()

@order_detailctl.get("/detail/{id}")
async def getorderdetailbyid(id: int):
    sql = "select * from tbl_order_detail where `tbl_order_detail`.`id` ={}"
    return conn.execute(sql.format(id)).fetchone()

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