from pydantic import BaseModel

class user(BaseModel):
    name: str
    dob: str
    email: str
    phone: str
    username: str
    password:str
    role: str
    image: str
    address: str