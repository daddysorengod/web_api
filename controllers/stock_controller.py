from config.db import conn
from models.index import stockdb
from schemas.index import stock
from datetime import datetime


def getallstock():
    # sql = "select * from tbl_stock"
    return conn.execute(stockdb.select()).fetchall()

def addstock(newstock: stock):
    conn.execute(stockdb.insert().values(
        stock_product = newstock.stock_product,
        stock_category_id = newstock.stock_category_id,
        stock_quantity = newstock.stock_quantity,
        stock_purchaseprice = newstock.stock_purchaseprice,
        stock_date = newstock.stock_date
    ))
    return "complete!"

def updatestock(id: int,newstock:stock):
    conn.execute(stockdb.update().values(
        stock_product = newstock.stock_product,
        stock_category_id = newstock.stock_category_id,
        stock_quantity = newstock.stock_quantity,
        stock_purchaseprice = newstock.stock_purchaseprice,
        stock_date = newstock.stock_date
    ).where(stockdb.c.stock_id==id))
    return "complete"

def deletestock(id: int):
    conn.execute(stockdb.delete().where(stockdb.c.stock_id==id))
    return "complete!"

def datefilter(date: str):
    return conn.execute(stockdb.select().where(stockdb.c.stock_date==datetime.strptime(date,"%Y-%m-%d"))).fetchall()