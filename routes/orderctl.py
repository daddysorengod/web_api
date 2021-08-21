from fastapi import APIRouter
from config.db import conn
from models.index import orderdb
from schemas.index import order


orderctl = APIRouter()

@orderctl.get("/order")
async def showAllorder():
    sql = "select * from tbl_order"
    return conn.execute(sql).fetchall()

@orderctl.get("/order/{id}")
async def getOderbyID(id:int):
    sql = "select * from tbl_order where `tbl_order`.`id` ={}"
    return conn.execute(sql.format(id)).fetchall()

@orderctl.get("/order/{oder_code}")
async def getOderbyOrderCode(oder_code:str):
    sql = "select * from tbl_order where `tbl_oder`.`oder_code` = {}"
    return conn.execute(sql.format(oder_code)).fetchall()

@orderctl.post("/order")
async def addoder(newoder: order):
    conn.execute(orderdb.insert().values(
        order_code = newoder.order_code,
        order_user_id = newoder.order_user_id,
        order_product_id = newoder.order_product_id,
        order_date = newoder.order_date,
        status = newoder.status
    ))
    return "them thanh cong"

@orderctl.put("/orderupdate/{id}")
async def updateOrder(id: int, newoder:order):
    conn.execute(orderdb.update().values(
        order_code = newoder.order_code,
        order_user_id = newoder.order_user_id,
        order_product_id = newoder.order_product_id,
        order_date = newoder.order_date,
        status = newoder.status
    ).where(orderdb.c.id==id))
    return "sua thanh cong"

@orderctl.delete("/orderdelete/{id}")
async def deleteorder(id: int):
    ok = conn.execute(orderdb.delete().where(orderdb.c.id==id))
    return ok