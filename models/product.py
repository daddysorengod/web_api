from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

productdb = Table(
    'tbl_product',meta,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("product_name",String(255)),
    Column("category_id",Integer),
    Column("product_quantity",Integer),
    Column("product_price",String(255)),
    Column("product_image",String(255)),
    Column("product_description",String(255)),
    Column("product_hot",Integer)
)