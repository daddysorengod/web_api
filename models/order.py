from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from config.db import meta

orderdb = Table(
    "tbl_oder",meta,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("oder_code",String(255)),
    Column("oder_user_id",Integer),    
    Column("oder_product_id",Integer),
    Column("oder_date",DateTime),
    Column("status",String(255))
)