from fastapi import APIRouter
from config.db import conn
from models.index import productdb,categorydb
from schemas.index import product


productctl = APIRouter()

def getCategory(id: int):
        getRS = conn.execute(categorydb.select().where(categorydb.c.id==id)).fetchone()
        return getRS 

@productctl.get("/product")
async def showallproduct():
    # sql = "select * from tbl_product,tbl_category where tbl_product.category_id = tbl_category.id"
    # return conn.execute(sql).fetchall()
    rsPd = conn.execute(productdb.select()).fetchall()
    arrRS = []
    for row in rsPd:
        rs = {
            "id": row['id'],
            "product_name": row['product_name'],
            "category_id": row['category_id'],
            "product_quantity": row['product_quantity'],
            "product_price": row['product_price'],
            "product_image": row['product_image'],
            "product_description": row['product_description'],
            "product_hot": row['product_hot'],
            "category": getCategory(row['category_id'])
        }
        arrRS.append(rs)
    return arrRS
# @productctl.post("/testfile")
# async def uploadfile(file: UploadFile = File(...)):
#     return {"file":file.filename}

@productctl.get("/product/{id}")
async def findproductbyID(id: int):
    rsPd = conn.execute(productdb.select()).fetchall()
    for row in rsPd:
        if row['id']==id:
            rs = {
                "id": row['id'],
                "product_name": row['product_name'],
                "category_id": row['category_id'],
                "product_quantity": row['product_quantity'],
                "product_price": row['product_price'],
                "product_image": row['product_image'],
                "product_description": row['product_description'],
                "product_hot": row['product_hot'],
                "category": getCategory(row['category_id'])
            }
            break
    return rs


@productctl.get("/product/searchname={name}")
async def findproductbyName(name:str):
    # sql = "select * from tbl_product where `tbl_product`.`product_name` like %s"
    # return conn.execute(sql,"%"+name+"%").fetchall()
    rsPd = conn.execute(productdb.select()).fetchall()
    for row in rsPd:
        if name in row['product_name']:
            rs = {
                "id": row['id'],
                "product_name": row['product_name'],
                "category_id": row['category_id'],
                "product_quantity": row['product_quantity'],
                "product_price": row['product_price'],
                "product_image": row['product_image'],
                "product_description": row['product_description'],
                "product_hot": row['product_hot'],
                "category": getCategory(row['category_id'])
            }
            break
    return rs

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


@productctl.put("/product/update/{id}")
async def updateproduct(id: int, newproduct:product):
    conn.execute(productdb.update().values(
        product_name = newproduct.product_name,
        category_id = newproduct.category_id,
        product_quantity = newproduct.product_quantity,
        product_price = newproduct.product_price,
        product_image = newproduct.product_image,
        product_description = newproduct.product_description,
        product_hot = newproduct.product_hot
    ).where(productdb.c.id==id))
    return "sua thanh cong"

@productctl.delete("/product/{id}")
async def deleteProduct(id: int):
    conn.execute(productdb.delete().where(productdb.c.id==id))
    return "xoa thanh cong"