from fastapi import FastAPI
from routes.index import user_rt,category_rt,product_rt,order_rt,order_detail_rt,stockctl


app = FastAPI()
app.include_router(user_rt)
app.include_router(category_rt)
app.include_router(product_rt)
app.include_router(order_rt)
app.include_router(order_detail_rt)
app.include_router(stockctl)