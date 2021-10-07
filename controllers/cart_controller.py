from config.db import conn
from schemas.index import cart,order,order_detail
from controllers import order_controller,orderdetail_controller 

def addnewCart(newcart : cart):
    neworder = order(
        order_code = newcart.order_code,
        order_user_id = newcart.order_user_id,
        order_date = newcart.order_date,
        status = newcart.status
    )
    order_controller.addneworder(neworder)
    
    # newdetail.order_detail_code = newcart.order_code
    for i in range(len(newcart.product_id)):
        newdetail = order_detail(
            order_detail_code = newcart.order_code,
            product_id = newcart.product_id[i],
            order_detail_quantity = newcart.order_quantity[i]
        )
        orderdetail_controller.addOrderdetail(newdetail)
    return
