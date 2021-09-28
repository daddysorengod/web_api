from fastapi import APIRouter
from controllers import stock_controller
from schemas.index import stock,objectsearch

stockctl = APIRouter()

@stockctl.get("/stock")
async def showall():
    return stock_controller.getallstock()

@stockctl.post("/stock/create")
async def createstock(newstock: stock):
    return stock_controller.addstock(newstock)

@stockctl.put("/stock/update/{id}")
async def updatestockbyid(id: int, newstock:stock):
    return stock_controller.updatestock(id,newstock)

@stockctl.delete("/stock/{id}")
async def deletestockbyid(id: int):
    return stock_controller.deletestock(id)

@stockctl.post("/stock/filterbydate")
async def filterbydate(date:objectsearch):
    return stock_controller.datefilter(date.key)