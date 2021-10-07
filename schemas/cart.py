
from pydantic import BaseModel 

class cart(BaseModel): 
    order_code: str
    order_user_id: int
    order_date: str
    status: str
    product_id: list[int]
    order_quantity: list[int]
        