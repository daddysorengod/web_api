from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String,DateTime
from config.db import meta

stockdb = Table(
    "tbl_stock",meta,
    Column("stock_id",Integer,primary_key=True,autoincrement=True),
    Column("stock_product",String(255)),
    Column("stock_category_id",Integer),
    Column("stock_quantity",Integer),
    Column("stock_purchaseprice",String(255)),
    Column("stock_date",DateTime),
    Column("status",Integer),
    Column("employee_id",Integer)
)