from sqlalchemy import Table,Column
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from config.db import meta

userdb = Table(
    'tbl_user',meta,
    Column("id",Integer,primary_key=true,autoincrement=true),
    Column("name",String(255)),
    Column("dob",DateTime),
    Column("email",String(255)),
    Column("phone",String(255)),
    Column("username",String(255)),
    Column("password",String(255)),
    Column("role",String(255)),
    Column("image",String(255))
)

