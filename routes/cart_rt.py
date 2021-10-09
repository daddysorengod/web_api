from fastapi import APIRouter
from schemas.index import cart
from controllers import cart_controller
cart_rt = APIRouter()

@cart_rt.post("/cart")
async def addcart(newcart: cart):
    return cart_controller.addnewCart(newcart)