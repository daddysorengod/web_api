from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

favoritedb = Table('tbl_favorite',meta,
    Column('id',Integer,primary_key=True,autoincrement=True),
    Column('user_id',Integer),
    Column('product_id',Integer),
    Column('status',String(255))                   
)