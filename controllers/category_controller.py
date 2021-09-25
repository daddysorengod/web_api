from config.db import conn
from models.index import categorydb
from schemas.index import category

def getallcategory():
    return conn.execute(categorydb.select()).fetchall()

def getcategorybyid(id: int):
    return conn.execute(categorydb.select().where(categorydb.c.id==id)).fetchone()

def getcategorybyname(name:str):
    sql = "select * from tbl_category where `tbl_category`.`name` like %s"
    return conn.execute(sql,("%"+name.lower()+"%")).fetchall()

def addCategory(newcategory:category):
    conn.execute(categorydb.insert().values(
        name = newcategory.name.lower(),
        image = newcategory.image,
    ))
    return "complete!"

def updateCategory(id: int,newcategory:category):
    conn.execute(categorydb.update().values(name = newcategory.name,image = newcategory.image).where(categorydb.c.id==id))
    return "complete!"

def deleteCategory(id: int):
    conn.execute(categorydb.delete().where(categorydb.c.id==id))
    return "complete!"