from pydantic import BaseModel 

class order(BaseModel): 
    order_code: str
    order_user_id: int 
    # order_product_id: int 
    order_date: str 
    status: str