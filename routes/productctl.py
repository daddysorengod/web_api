from fastapi import APIRouter, File,UploadFile
from config.db import conn
from models.index import productdb
from schemas.index import product

productctl = APIRouter()

@productctl.get("/product")
async def showallproduct():
    sql = "select * from tbl_product,tbl_category where tbl_product.category_id = tbl_category.id"
    return conn.execute(sql).fetchall()

# @productctl.post("/testfile")
# async def uploadfile(file: UploadFile = File(...)):
#     return {"file":file.filename}

@productctl.post("/product")
async def addproduct(newproduct: product):
    conn.execute(productdb.insert().values(
        product_name = newproduct.product_name,
        category_id = newproduct.category_id,
        product_quantity = newproduct.product_quantity,
        product_price = newproduct.product_price,
        product_image = newproduct.product_image,
        product_description = newproduct.product_description,
        product_hot = newproduct.product_hot
    ))
    return "them thanh cong"

@productctl.get("/product/{id}")
async def findproductbyID(id: int):
    return conn.execute(productdb.select().where(productdb.c.id==id)).fetchall()

@productctl.get("/product/full/{id}")
async def getfullproduct(id:int):
    # sql = "select * from tbl_product, tbl_category where tbl_product.id={} and tbl_product.category_id = tbl_category.id"
    # return conn.execute(sql.format(id)).fetchall()
    return

@productctl.get("/product/searchname={name}")
async def findproductbyName(name:str):
    sql = "select * from tbl_product where `tbl_product`.`product_name` like %s"
    return conn.execute(sql,"%"+name+"%").fetchall()

@productctl.put("/product/update/{id}")
async def updateproduct(id: int, newproduct:product):
    conn.execute(productdb.update().values(
        product_name = newproduct.product_name,
        product_quantity = newproduct.product_quantity,
        product_price = newproduct.product_price,
        product_image = newproduct.product_image,
        product_description = newproduct.product_description,
        product_hot = newproduct.product_hot
    ))
    return "sua thanh cong"

@productctl.delete("/product/{id}")
async def deleteProduct(id: int):
    conn.execute(productdb.delete().where(productdb.c.id==id))
    return "xoa thanh cong"