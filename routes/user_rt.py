from schemas.Objectsearch import objectsearch
from fastapi import APIRouter,HTTPException
from schemas.index import user,account,passwordupdate
from controllers import user_controller

user_rt = APIRouter()

@user_rt.get("/user")
async def showalluser(): 
    return user_controller.getListuser()

@user_rt.get("/user/searchID={id}")
async def findUserbyid(id:int): 
    return user_controller.getUserById(id)

@user_rt.post("/user/searchname")
async def findUserbyName(name:objectsearch):
    return user_controller.getUserByName(name.key)

@user_rt.post("/user/adduserfromadmin")
async def adduser_admin(newuser: user):
    return user_controller.addUserAdmin(newuser)

@user_rt.post("/user/adduser")
async def adduser(newuser:user):
    return user_controller.addUser(newuser)

@user_rt.put("/user/{id}")
async def updateuser(id: int, newuser: user):
    return user_controller.updateUser(id,newuser)

@user_rt.put("/user/updateimage/{id}")
async def updateimage(id: int, image:objectsearch):
    return user_controller.updateimageuser(id,image.key)

@user_rt.put("/user/rePwd/{id}")
async def update(id: int,newpassword:passwordupdate):
    return user_controller.updatePassword(id,newpassword) 

@user_rt.delete("/user/{id}")
async def deleteuser(id: int):
    return user_controller.deleteUser(id)

@user_rt.post("/user/login")
async def login_app(loginAccount:account):
    return user_controller.login(loginAccount)
