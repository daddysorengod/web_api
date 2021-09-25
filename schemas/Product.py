from pydantic import BaseModel
# from schemas.index import category
class product(BaseModel):
     
    product_name: str
    category_id: int
    product_quantity: int
    product_price: str
    product_image: str
    product_description:str
    product_hot: int
    