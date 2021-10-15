from pydantic import BaseModel

class favorite(BaseModel):
    user_id: int
    product_id:int
    status:str