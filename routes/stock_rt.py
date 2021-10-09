from fastapi import APIRouter
from controllers import stock_controller
from schemas.index import stock,objectsearch

stock_rt = APIRouter()

@stock_rt.get("/stock")
async def showall():
    return stock_controller.getallstock()

@stock_rt.get("/stock/{id}")
async def getbyid(id: int):
    return stock_controller.getstockbyid(id)

@stock_rt.post("/stock/create")
async def createstock(newstock: stock):
    return stock_controller.addstock(newstock)

@stock_rt.put("/stock/update/{id}")
async def updatestockbyid(id: int, newstock:stock):
    return stock_controller.updatestock(id,newstock)

@stock_rt.delete("/stock/{id}")
async def deletestockbyid(id: int):
    return stock_controller.deletestock(id)

@stock_rt.post("/stock/filterbydate")
async def filterbydate(date:objectsearch):
    return stock_controller.datefilter(date.key)