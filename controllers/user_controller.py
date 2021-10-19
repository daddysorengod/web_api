from models.index import accountdb
from schemas.index import user,account,passwordupdate
from config.db import conn
from fastapi import HTTPException

def getListuser():
    return conn.execute(accountdb.select()).fetchall()

def getUserById(id: int):
    return conn.execute(accountdb.select().where(accountdb.c.id==id)).fetchone()

def getUserByName(name:str):
    sql = "select * from tbl_account where `tbl_account`.`name` like %s"
    return conn.execute(sql,("%"+name+"%")).fetchall()

def addUser(newuser: user):
    check = True
    rs = conn.execute(accountdb.select()).fetchall()
    for humman in rs:
        if humman['username'] == newuser.username or humman['email']==newuser.email: 
            check = False
            break
    if check == False:
        raise HTTPException(status_code=422,detail="registered account or email")
    else: 
        conn.execute(accountdb.insert().values(
            name = newuser.name,
            dob = newuser.dob,
            email = newuser.email,
            phone = newuser.phone,
            username = newuser.username,
            password = newuser.password,
            role = "user",
            image = newuser.image,
            address = newuser.address
        ))   
        raise HTTPException(status_code=200,detail="complete")
    
def addUserAdmin(newuser: user):
    check = True
    rs = conn.execute(accountdb.select()).fetchall()
    for humman in rs:
        if humman['username'] == newuser.username or humman['email']==newuser.email: 
            check = False
            break
    if check == False:
        raise HTTPException(status_code=422,detail="registered account or email")
    else: 
        conn.execute(accountdb.insert().values(
            name = newuser.name,
            dob = newuser.dob,
            email = newuser.email,
            phone = newuser.phone,
            username = newuser.username,
            password = newuser.password,
            role = newuser.role,
            image = newuser.image,
            address = newuser.address
        ))   
        raise HTTPException(status_code=200,detail="complete")
    
def updateUser(id:int , newuser: user):
    conn.execute(accountdb.update().values(
            name = newuser.name,
            dob = newuser.dob,
            email = newuser.email,
            username = newuser.username,
            password = newuser.password,
            role = newuser.role,
            address = newuser.address
        ).where(accountdb.c.id==id))
    return

def updateimageuser(id:int , image:str):
    conn.execute(accountdb.update().values(image = image).where(accountdb.c.id==id))
    return

def updatePassword(id:int, newpassword:passwordupdate):
    rs = conn.execute(accountdb.select()).fetchall()
    sql = "UPDATE `tbl_account` SET `password` = '{}' WHERE `tbl_account`.`id` = {}"
    for row in rs:
        if row['id']==id and newpassword.current==row['password']:
            conn.execute(sql.format(newpassword.new,id))
            ok = True
            break
        else:
            ok = False
    if ok == False:
        raise HTTPException(status_code=422,detail="update fail")
    else:
        return "update complete!"
        
def deleteUser(id: int):
    check = False
    rs = conn.execute(accountdb.select()).fetchall()
    for humman in rs:
        if humman['id'] == id:
            check = True
            break
    if check == False:
        raise HTTPException(status_code=422,detail="incomplete") 
    else:
        conn.execute(accountdb.delete().where(accountdb.c.id==id))
        raise HTTPException(status_code=200,detail="delete complete") 
    
def login(loginAccount:account):
    data = conn.execute(accountdb.select()).fetchall()
    ok = False
    for row in data:
        if row['username']==loginAccount.username and row['password']==loginAccount.password:
            rs = conn.execute(accountdb.select().where(accountdb.c.username==loginAccount.username and accountdb.c.password==loginAccount.password)).fetchone()
            ok = True
            break
        else:
            ok = False
    
    if ok == False: 
        raise HTTPException(status_code=422,detail="username or password is incorrect!")
    else:
        return rs
    
def getinfouser(id:int):
    rs = conn.execute(accountdb.select().where(accountdb.c.id==id)).fetchone()
    result = {
        "id": rs['id'],
        "name": rs['name'],
        "address": rs['address'],
        "phone": rs['phone']
    }
    return result
    