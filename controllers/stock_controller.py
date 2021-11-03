import re
from sqlalchemy.sql.expression import false, true
from config.db import conn
from models.index import stockdb,accountdb
from schemas.Product import product
from schemas.index import stock
from datetime import datetime


def getUserById(id: int):
    return conn.execute(accountdb.select().where(accountdb.c.id==id)).fetchone()

def getallstock():
    rsPd = conn.execute(stockdb.select()).fetchall()
    arrRS = []
    for row in rsPd:
        rs = {
            "stock_id": row['stock_id'],
            "stock_product": row['stock_product'],
            "stock_category_id": row['stock_category_id'],
            "product_quantity": row['stock_quantity'],
            "stock_purchaseprice": row['stock_purchaseprice'],
            "stock_date": row['stock_date'],
            "status": row['status'],
            "employee_id": row['employee_id'],

            "employee": getUserById(row['employee_id'])
        }
        arrRS.append(rs)
    return arrRS

def getstockbyid(id: int):
    return conn.execute(stockdb.select().where(stockdb.c.stock_id==id)).fetchone()

def addstock(newstock: stock):
    conn.execute(stockdb.insert().values(
        stock_product = newstock.stock_product.lower(),
        stock_category_id = newstock.stock_category_id,
        stock_quantity = newstock.stock_quantity,
        stock_purchaseprice = newstock.stock_purchaseprice,
        stock_date = newstock.stock_date,
        status = newstock.status,
        employee_id = newstock.employee_id
    ))
    return "complete!"

def updatestock(id: int,newstock:stock):
    conn.execute(stockdb.update().values(
        stock_product = newstock.stock_product.lower(),
        stock_category_id = newstock.stock_category_id,
        stock_quantity = newstock.stock_quantity,
        stock_purchaseprice = newstock.stock_purchaseprice,
        stock_date = newstock.stock_date,
        status = newstock.status,
        employee_id = newstock.employee_id
    ).where(stockdb.c.stock_id==id))
    return "complete"

def deletestock(id: int):
    conn.execute(stockdb.delete().where(stockdb.c.stock_id==id))
    return "complete!"

def datefilter(date: str):
    return conn.execute(stockdb.select().where(stockdb.c.stock_date==datetime.strptime(date,"%Y-%m-%d"))).fetchall()
