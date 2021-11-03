from starlette.exceptions import HTTPException
from controllers.stock_controller import getallstock
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

def getproducthot():
    select = "select * from tbl_product where tbl_product.product_hot = 2 ORDER BY RAND() LIMIT 3"
    rsPdh = conn.execute(select).fetchall()
    return rsPdh

def getproductfavorite():
    select = "select * from tbl_product where tbl_product.product_hot = 1 ORDER BY RAND() LIMIT 3"
    rsPdh = conn.execute(select).fetchall()
    return rsPdh

def getrandomproduct():
    sql = "select * from tbl_product ORDER BY RAND() LIMIT 4"
    rsPdh = conn.execute(sql).fetchall()
    return rsPdh

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
    rs = getallstock()
    rs1 = getallproduct()
    checkStock = False
    checkProduct = True
    for key in rs:
        if key['stock_product'] == newproduct.product_name.lower():
            checkStock = True
            break
    for key in rs1:
        if key['product_name'] == newproduct.product_name.lower():
            checkProduct = False
            break
    if checkStock == False:
        raise HTTPException(status_code=422, detail="name does not exist in stock!")
    else:
        if checkProduct == False:
            raise HTTPException(status_code=422,detail="product name is exist")
        else:
            conn.execute(productdb.insert().values(
            product_name = newproduct.product_name.lower(),
            category_id = newproduct.category_id,
            product_quantity = newproduct.product_quantity,
            product_price = newproduct.product_price,
            product_image = newproduct.product_image,
            product_description = newproduct.product_description,
            product_hot = newproduct.product_hot
        )) 
        raise HTTPException(status_code=200,detail="complete!")             
    


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

def getproductindetail(id: int):
    rs = conn.execute(productdb.select().where(productdb.c.id==id)).fetchone()
    result = {
        "product_name":rs['product_name'],
        "product_price":rs['product_price']
    }
    return result

def deleteproduct(id: int):
    conn.execute(productdb.delete().where(productdb.c.id==id))
    return "complete"


def getProductByCategoryId(id: int):
      rs = conn.execute(productdb.select().where(productdb.c.category_id==id)).fetchall()
      return rs

def changeStatusProductToFavorite(id: int,newproduct_hot):
    conn.execute(productdb.update().values(product_hot=newproduct_hot.product_hot).where(productdb.c.id==id))
    return "update success fully"

