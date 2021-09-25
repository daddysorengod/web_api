from config.db import conn
from models.index import order_detaildb
from schemas.index import order_detail

def getallorderdetail():
    sql = "select * from tbl_order_detail"
    return conn.execute(sql).fetchall()
    # return conn.execute(order_detaildb.select()).fetchall()

def getorderdetailbyodercode(code: str):
    sql = "select * from tbl_order_detail where `tbl_order_detail`.`id` ={}"
    return conn.execute(sql.format(code)).fetchall()