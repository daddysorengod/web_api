from schemas.Objectsearch import objectsearch
from fastapi import APIRouter,HTTPException
from config.db import conn 
from models.index import userdb
from schemas.index import user,account,passwordupdate
from controllers import user_controller

userctl = APIRouter()

@userctl.get("/user")
async def showalluser(): 
    return user_controller.getListuser()

@userctl.get("/user/searchID={id}")
async def findUserbyid(id:int): 
    return user_controller.getUserById(id)

@userctl.post("/user/searchname")
async def findUserbyName(name:objectsearch):
    return user_controller.getUserByName(name.key)

@userctl.post("/user/adduserfromadmin")
async def adduser_admin(newuser: user):
    return user_controller.addUser(newuser)

@userctl.put("/user/{id}")
async def updateuser(id: int, newuser: user):
    return user_controller.updateUser(id,newuser)

@userctl.put("/user/rePwd/{id}")
async def update(id: int,newpassword:passwordupdate):
    return user_controller.updatePassword(id,newpassword) 

@userctl.delete("/user/{id}")
async def deleteuser(id: int):
    return user_controller.deleteUser(id)

@userctl.post("/user/login")
async def login_app(loginAccount:account):
    return user_controller.login(loginAccount)