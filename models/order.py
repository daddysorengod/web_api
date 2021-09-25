from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from config.db import meta

orderdb = Table(
    "tbl_order",meta,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("order_code",String(255)),
    Column("order_user_id",Integer),    
    # Column("order_product_id",Integer),
    Column("order_date",DateTime),
    Column("status",String(255))
)