from config.db import conn
from models.index import order_detaildb
from schemas.index import order_detail
from controllers import product_controller
def getallorderdetail():
    sql = "select * from tbl_order_detail"
    return conn.execute(sql).fetchall()
    # return conn.execute(order_detaildb.select()).fetchall()

def getorderdetailbyodercode(code: str):
    return conn.execute(order_detaildb.select().where(order_detaildb.c.order_detail_code == code)).fetchall()
    
def  addOrderdetail(newod: order_detail):
    rs = product_controller.getproductbyID(newod.product_id)
    check = int(rs['product_quantity']) - int(newod.order_detail_quantity)
    if check >= 0:    
        conn.execute(order_detaildb.insert().values(
            order_detail_code = newod.order_detail_code,
            product_id = newod.product_id,
            order_detail_quantity = newod.order_detail_quantity
        ))
        product_controller.buyproduct(newod.product_id,check)
    return "complete!"

def updateOrderdetail(id: int, newod: order_detail):
    conn.execute(order_detaildb.update().values(
        order_detail_code = newod.order_detail_code,
        product_id = newod.product_id,
        order_detail_quantity = newod.order_detail_quantity
    ).where(order_detaildb.c.id==id))
    return "complete!"

def deleteorderbyid(id: int):
    conn.execute(order_detaildb.delete().where(order_detaildb.c.id==id))
    return "complete!"

