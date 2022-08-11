from decimal import Decimal
from starlette import status
from fastapi import APIRouter, Body, Path, Query
from project.schemas import DataResponse, Sort, PageResponse
from router.examples.order import order_op3
from schema import OrderReq
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
    return DataResponse(data=order["Order"])


@router.get(
    path="/",
    response_model=PageResponse,
    status_code=status.HTTP_200_OK
)
def get_orders_cus(
        from_price: Decimal = Query(default=None, gt=0),
        to_price: Decimal = Query(default=None, gt=0),
        payment_method: str = Query(default=None, max_length=100),
        name_shipping: str = Query(default=None, max_length=200),
        phone_shipping: str = Query(default=None, max_length=20),
        address_shipping: str = Query(default=None, max_length=200),
        province_code_shipping: str = Query(default=None, max_length=50), ward_code_shipping: str = None,
        district_code_shipping: str = Query(default=None, max_length=50),
        customer_username: str = Query(default=None, max_length=100),
        page: int = Query(1, gt=0),
        size: int = Query(100, gt=0),
        sort_direction: Sort.Direction = Query(None)
):
    orders = OrderServiceCus().get_orders_cus_service(
        from_price=from_price,
        to_price=to_price,
        payment_method=payment_method,
        name_shipping=name_shipping,
        phone_shipping=phone_shipping,
        address_shipping=address_shipping,
        province_code_shipping=province_code_shipping,
        ward_code_shipping=ward_code_shipping,
        district_code_shipping=district_code_shipping,
        customer_username=customer_username,
        sort_direction=sort_direction,
        page=page, size=size)
    return PageResponse(data=orders.data,
                        total_items=orders.total_items,
                        total_page=orders.total_page,
                        current_page=orders.current_page)
