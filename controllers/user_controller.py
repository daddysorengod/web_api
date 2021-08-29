from models.index import userdb
# from schemas.index import user
from config.db import conn


def getListuser():
    return conn.execute(userdb.select()).fetchall()
    