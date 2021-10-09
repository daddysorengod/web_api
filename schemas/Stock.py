from pydantic import BaseModel

class stock(BaseModel):
    stock_product: str
    stock_category_id: int
    stock_quantity: int
    stock_purchaseprice: str
    stock_date: str
    status: int
    employee_id: int