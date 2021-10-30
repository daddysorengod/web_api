from pydantic import BaseModel
# from schemas.index import category
class product_hot(BaseModel):
    product_hot: int
    user_id:int
    