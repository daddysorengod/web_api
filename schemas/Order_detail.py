from pydantic import BaseModel

class order_detail(BaseModel):
    oder_detail_code: str
    product_id: int 
    order_detail_quantity: int
    