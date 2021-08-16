from fastapi import APIRouter
# from sqlalchemy import lo
from config.db import conn 
from models.index import categorydb
from schemas.index import category


categoryctl = APIRouter()

@categoryctl.get("/category")
async def showallcategory():
    sql = "select * from tbl_category"
    return conn.execute(sql).fetchall()

@categoryctl.get("/category/{id}")
async def findCategorybyid(id:int):
    sql = "select * from tbl_category where `tbl_category`.`id` ={}"
    return conn.execute(sql.format(id)).fetchall()

@categoryctl.get("/category/{name}")
async def findCategorybyName(name:str):
    sql = "select * from tbl_category where `tbl_category`.`name` like %s"
    return conn.execute(sql,("%"+name+"%")).fetchall()

@categoryctl.post("/category")
async def addcategory(newcategory:category):
    conn.execute(categorydb.insert().values(
        name = newcategory.name
    ))
    return "them thanh cong"
    
@categoryctl.put("/category/{id}")
async def updatecategory(id:int,newcategory:category):
    conn.execute(categorydb.update().values(name = newcategory.name).where(categorydb.c.id==id))
    return "sua thanh cong"

@categoryctl.delete("/category/{id}")
async def deletecategory(id: int):
    conn.execute(categorydb.delete().where(categorydb.c.id==id))
    return "xoa thanh cong"


