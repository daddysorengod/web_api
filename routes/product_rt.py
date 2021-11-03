from fastapi import APIRouter
from schemas.index import product,objectsearch,product_hot
from controllers import product_controller

product_rt = APIRouter()

@product_rt.get("/product")
async def showallproduct():
    return product_controller.getallproduct()

@product_rt.get("/product/random")
async def showallproductrandom():
    return product_controller.getrandomproduct()


@product_rt.get("/producthot")
async def showallproducthot():
    return product_controller.getproducthot()
    
 
    
@product_rt.get("/productfavorite")
async def showallproductfavorite():
    return product_controller.getproductfavorite()

@product_rt.get("/product/{id}")
async def findproductbyID(id: int):
    return product_controller.getproductbyID(id)

@product_rt.post("/product/searchname")
async def findproductbyName(name:objectsearch):
    return product_controller.getproductbyname(name.key.lower())

@product_rt.post("/product")
async def addproduct(newproduct: product):
    return product_controller.addproduct(newproduct)


@product_rt.put("/product/update/{id}")
async def updateproduct(id: int, newproduct:product):
    return product_controller.updateproduct(id,newproduct)


@product_rt.put("/product/updateproducthot/{id}")
async def changeStatusProductToFavorite(id: int, newproduct_hot:product_hot):
    return product_controller.changeStatusProductToFavorite(id,newproduct_hot)

@product_rt.delete("/product/{id}")
async def deleteProduct(id: int):
    return product_controller.deleteproduct(id)

@product_rt.get("/product/categoryid/{id}")
async def showallproductbycategoryid(id: int):
    return product_controller.getProductByCategoryId(id)

