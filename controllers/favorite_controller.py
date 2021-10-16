from sqlalchemy import log
from config.db import conn
from models.index import favoritedb,productdb
from schemas.index import favorite


def getProduct(id:int):
    getRS = conn.execute(productdb.select().where(productdb.c.id==id)).fetchone()
    return getRS


def getallfavorite():
    return conn.execute(favoritedb.select()).fetchall()

def getfavoritebyid(id):
    return conn.execute(favoritedb.select().where(favoritedb.c.id == id)).fetchall()

def getfavoritebyiduser(id):
    rs = conn.execute(favoritedb.select().where(favoritedb.c.user_id==id)).fetchall()

    array = []
    array_details = []
    for row in rs:
        array.append(row['product_id'])
        array_details.append(getProduct(row['product_id']))
    result = {
        "id":rs[0]['id'],
        "user_id":rs[0]['user_id'],
        "product_id":array,
        "product":array_details,
        "status":rs[0]['status']
    }
    return result
    
    # return
def addnewfavorite(newfavorite:favorite):
    conn.execute(favoritedb.insert().values(
        user_id=newfavorite.user_id,
        product_id=newfavorite.product_id,
        status=newfavorite.status
    ))
    return

def deletefavorite(id):
    conn.execute(favoritedb.delete().where(favoritedb.c.id == id))
    return