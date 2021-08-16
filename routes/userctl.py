# from os import name
# import re
from fastapi import APIRouter
from config.db import conn 
from models.index import userdb
from schemas.index import user
# import numpy as np

userctl = APIRouter()

@userctl.get("/user")
async def showalluser(): 
    sql = "select * from tbl_user"
    return conn.execute(sql).fetchall()

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

@userctl.post("/user/adduser")
async def adduser(newuser: user):
    sql = "INSERT INTO `dbapi`.`tbl_user` (`name`, `dob`, `email`, `phone`, `username`, `password`,`role`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')"
    conn.execute(sql.format(newuser.name,newuser.dob,newuser.email,newuser.phone,newuser.username,newuser.password,newuser.role))
    return "them thanh cong"

@userctl.put("/user/{id}")
async def updateuser(id: int, newuser: user):
    conn.execute(userdb.update().values(
        name = newuser.name,
        dob = newuser.dob,
        email = newuser.email,
        username = newuser.username,
        password = newuser.password,
        role = newuser.role
    ).where(userdb.c.id==id))
    return "sua thanh cong"

@userctl.delete("/user/{id}")
async def deleteuser(id: int):
    conn.execute(userdb.delete().where(userdb.c.id==id))
    return "xoa thanh cong"