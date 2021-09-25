from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta

order_detaildb = Table(
    "tbl_order_detail",meta,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("order_detail_code",String(255)),
    Column("product_id",Integer),
    Column("order_detail_quantity",Integer)
)