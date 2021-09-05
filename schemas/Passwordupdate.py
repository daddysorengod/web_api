from pydantic import BaseModel

class passwordupdate(BaseModel):
    current: str
    new:str