# from os import name
# import re
from fastapi import APIRouter
from fastapi.params import Form
from config.db import conn 
from models.index import userdb
from schemas.index import user
from controllers import user_controller
# import numpy as np

userctl = APIRouter()

@userctl.get("/user")
async def showalluser(): 
    return user_controller.getListuser()

@userctl.get("/user/searchID={id}")
async def findUserbyid(id:int): 
    sql = "select * from tbl_user where `tbl_user`.`id`={}"
    return conn.execute(sql.format(id)).fetchall()
    # return sql.format(id)


@userctl.get("/user/searchname/{name}")
async def findUserbyName(name:str):
    sql = "select * from tbl_user where `tbl_user`.`name` like %s"
    return conn.execute(sql,("%"+name+"%")).fetchall()
    # sql = "select * from tbl_user"
    # cursor = conn.execute(sql).fetchall()
    # arr = np.array([],dtype=object)
    # arr1 = np.append(arr,cursor)
    # for row in cursor:
    #     if name in row['name']:
    #         arr = np.append(arr,row)
    # return conn.execute(userdb.select().where(userdb.c.name.like("%fTi%")))

# @userctl.get("/users/{username}")
# async def read_user(username: str):
#     return {"message": f"Hello {username}"}


# @userctl.get("/user/{username}")
# async def findUserbyUsername(username:str):
#     sql = "select * from tbl_user where `tbl_user`.`username` like '%"+"%s"+"%'"
#     return conn.execute(sql,username).fetchall()

@userctl.post("/user/adduserfromadmin")
async def adduser_admin(newuser: user):
    check:str
    rs = conn.execute(userdb.select()).fetchall()
    for humman in rs:
        if humman['username'] == newuser.username or humman['email']==newuser.email: 
            check = "tai khoan da ton tai"
            break
        else:
            sql = "INSERT INTO `dbapi`.`tbl_user` (`name`, `dob`, `email`, `phone`, `username`, `password`,`role`,`image`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}','{}')"
            conn.execute(sql.format(newuser.name,newuser.dob,newuser.email,newuser.phone,newuser.username,newuser.password,newuser.role,newuser.image))
            check = "them thanh cong"
    return check

@userctl.post("/user/adduserdefault")
async def adduser_default(newuser: user):
    check:str
    rs = conn.execute(userdb.select()).fetchall()
    for humman in rs:
        if humman['username'] == newuser.username or humman['email']==newuser.email:
            check = "tai khoan hoac email da ton tai"
            break
        else:
            sql = "INSERT INTO `dbapi`.`tbl_user` (`name`, `dob`, `email`, `phone`, `username`, `password`,`role`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}','{}')"
            conn.execute(sql.format(newuser.name,newuser.dob,newuser.email,newuser.phone,newuser.username,newuser.password,"default",newuser.image))
            check = "them thanh cong"
    return check


@userctl.put("/user/{id}")
async def updateuser(id: int, newuser: user):
    conn.execute(userdb.update().values(
        name = newuser.name,
        dob = newuser.dob,
        email = newuser.email,
        username = newuser.username,
        password = newuser.password,
        role = newuser.role,
        image = newuser.image
    ).where(userdb.c.id==id))
    return "sua thanh cong"

@userctl.delete("/user/{id}")
async def deleteuser(id: int):
    conn.execute(userdb.delete().where(userdb.c.id==id))
    return "xoa thanh cong"

@userctl.post("/user/login")
async def login_app(username:str = Form(...), password:str = Form(...)):
    check: str
    data = conn.execute(userdb.select()).fetchall()
    for humman in data:
        if humman['username'] == username and humman['password']==password:
            if humman['role']=='admin':
               check = humman['role']
            else:
                check = humman['role']
            break 
        else:
            check = "login hut me may roi"
    return check