from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

categorydb = Table(
    'tbl_category',meta,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("name",String(255)),
    Column("image",String(255))
)