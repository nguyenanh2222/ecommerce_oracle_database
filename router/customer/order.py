from decimal import Decimal

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Query
from starlette import status
from fastapi import APIRouter, Body
from project.schemas import DataResponse, Sort, PageResponse
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
    _order_item = OrderServiceCus().insert_order_item_service(username=order.customer_username)
    order = OrderServiceCus().insert_order_service(order=OrderReq(
        payment_method=order.payment_method,
        shipping_fee_discount=order.shipping_fee_discount,
        name_shipping=order.name_shipping,
        customer_username=order.customer_username,
        discount=order.discount))
    return DataResponse(data=order)


@router.get(
    path="/",
    response_model=PageResponse,
    status_code=status.HTTP_200_OK
)
def get_orders(
               from_price: Decimal = Query(None),
               to_price: Decimal = Query(None),
               payment_method: str = Query(None),
               name_shipping: str = Query(None),
               phone_shipping: str = Query(None),
               address_shipping: str = Query(None),
               province_code_shipping: str = Query(None),
               ward_code_shipping: str = Query(None),
               district_code_shipping: str = Query(None),
               sort_direction: Sort.Direction = Query(None),
               page: int = Query(1),
               size: int = Query(10)
               ) -> PageResponse:
    orders = OrderServiceCus().get_orders_repo_cus(
        from_price=from_price,
        to_price=to_price,
        payment_method=payment_method,
        name_shipping=name_shipping,
        phone_shipping=phone_shipping,
        address_shipping=address_shipping,
        province_code_shipping=province_code_shipping,
        ward_code_shipping=ward_code_shipping,
        district_code_shipping=district_code_shipping,
        sort_direction=sort_direction,
        page=page, size=size)
    return PageResponse(data=orders.data,
                        total_item=orders.total_items,
                        total_page=orders.total_page,
                        current_page=orders.current_page)
