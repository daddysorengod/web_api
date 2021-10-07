from models.index import productdb,categorydb
from config.db import conn
from schemas.index import product,objectsearch

def getCategory(id:int):
    getRS = conn.execute(categorydb.select().where(categorydb.c.id==id)).fetchone()
    return getRS

def getallproduct():
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

def getproductbyID(id: int):
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


def getproductbyname(name:str):
    rsPd = conn.execute(productdb.select()).fetchall()
    result = []
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
            result.append(rs)
    return result
    
def addproduct(newproduct: product):
    conn.execute(productdb.insert().values(
            product_name = newproduct.product_name.lower(),
            category_id = newproduct.category_id,
            product_quantity = newproduct.product_quantity,
            product_price = newproduct.product_price,
            product_image = newproduct.product_image,
            product_description = newproduct.product_description,
            product_hot = newproduct.product_hot
        ))
    return "complete!"


def updateproduct(id: int, newproduct:product):
    conn.execute(productdb.update().values(
        product_name = newproduct.product_name.lower(),
        category_id = newproduct.category_id,
        product_quantity = newproduct.product_quantity,
        product_price = newproduct.product_price,
        product_image = newproduct.product_image,
        product_description = newproduct.product_description,
        product_hot = newproduct.product_hot
    ).where(productdb.c.id==id)) 
    return "complete"

def buyproduct(id: int,quantity: int):
    conn.execute(productdb.update().values(product_quantity = quantity).where(productdb.c.id==id))
    # return    

def deleteproduct(id: int):
    conn.execute(productdb.delete().where(productdb.c.id==id))
    return "complete"