from config.db import conn
from models.index import orderdb
from schemas.index import order
from datetime import datetime
from controllers import user_controller

def getallorder():
    # sql = "select * from tbl_order"
    # return conn.execute(sql).fetchall()
    rs = conn.execute(orderdb.select()).fetchall()
    arrRs = []
    for row in rs:
        result = {
            "id":row['id'],
            "order_code":row['order_code'],
            "order_user_id":row['order_user_id'],
            "order_date":row['order_date'],
            "status": row['status'],
            "user_id":user_controller.getinfouser(row['order_user_id'])
        }
        arrRs.append(result)        
    return arrRs
    
def getorderbyid(id: int):
    rs = conn.execute(orderdb.select().where(orderdb.c.order_user_id == id)).fetchall()
    array = []
    for row in rs:
        result = {
            "id":row['id'],
            "order_code":row['order_code'],
            "order_user_id":row['order_user_id'],
            "order_date":row['order_date'],
            "status": row['status'],
            "user_id":user_controller.getinfouser(row['order_user_id'])
        }
        array.append(result)

    return array

def getorderbyordercode(order_code:str):
    rs = conn.execute(orderdb.select().where(orderdb.c.order_code == order_code)).fetchall()
    for row in rs:
        result = {
            "id":row['id'],
            "order_code":row['order_code'],
            "order_user_id":row['order_user_id'],
            "order_date":row['order_date'],
            "status": row['status'],
            "user_id":user_controller.getinfouser(row['order_user_id'])
        }
    return result

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

def filterbydate(date :str): 
    rs = conn.execute(orderdb.select().where(orderdb.c.order_date==datetime.strptime(date,"%Y-%m-%d"))).fetchall()
    arrRs = []
    for row in rs:
        result = {
            "id":row['id'],
            "order_code":row['order_code'],
            "order_user_id":row['order_user_id'],
            "order_date":row['order_date'],
            "status": row['status'],
            "user_id":user_controller.getinfouser(row['order_user_id'])
        }
        arrRs.append(result)        
    return arrRs

def deleteorderbyid(id: int):
    conn.execute(orderdb.delete().where(orderdb.c.id==id))
    return "complete"