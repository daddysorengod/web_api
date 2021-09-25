from config.db import conn
from models.index import orderdb
from schemas.index import order


def getallorder():
    sql = "select * from tbl_order"
    return conn.execute(sql).fetchall()

def getorderbyid(id: int):
    sql = "select * from tbl_order where id = %s"
    return conn.execute(sql,id).fetchone()

def getorderbyordercode(order_code:str):
    sql = "select * from tbl_order where order_code = '{}'"
    return conn.execute(sql.format(order_code)).fetchone()

def addneworder(neworder:order):
    conn.execute(orderdb.insert().values(
        order_code = neworder.order_code,
        order_user_id = neworder.order_user_id,
        order_date = neworder.order_date,
        status = neworder.status
    ))
    return "complete"    

def updateorderbyid(id: int, neworder: order):
    conn.execute(orderdb.update().values(
        order_code = neworder.order_code,
        order_user_id = neworder.order_user_id,
        order_product_id = neworder.order_product_id,
        order_date = neworder.order_date,
        status = neworder.status
    ).where(orderdb.c.id==id))
    return "complete"

def deleteorderbyid(id: int):
    conn.execute(orderdb.delete().where(orderdb.c.id==id))
    return "complete"