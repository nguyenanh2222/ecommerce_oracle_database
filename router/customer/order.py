from fastapi.encoders import jsonable_encoder
from starlette import status
from fastapi import APIRouter, Body
from project.schemas import DataResponse
from router.examples.order import order_op3
from schema import OrderReq, OrderItemReq
from service.customer.order import OrderServiceCus

router = APIRouter()


@router.post(
    path="/",
    response_model=DataResponse,
    status_code=status.HTTP_201_CREATED
)
def place_order(order: OrderReq = Body(..., examples=order_op3)):
    order_item = OrderServiceCus().insert_order_item_service(username=order.customer_username)
    cart_item = OrderServiceCus().delete_cart_item_service(username=order.customer_username)

    order = OrderServiceCus().insert_order(order=OrderReq(
        shipping_fee_original=order.shipping_fee_original,
        payment_method=order.payment_method,
        shipping_fee_discount=order.shipping_fee_discount,
        name_shipping=order.name_shipping,
        customer_username=order.customer_username))
    return DataResponse(data=order)
