from starlette import status
from fastapi import APIRouter, Body
from project.schemas import DataResponse
from router.examples.order import order_op1
from schema import OrderReq
from service.customer.order import OrderServiceCus

router = APIRouter()
@router.post(
    path="/",
    response_model=DataResponse,
    status_code=status.HTTP_201_CREATED
)
def insert_order(order: OrderReq = Body(
    ..., examples=order_op1)):
    order = OrderServiceCus().insert_order_service(
        OrderReq(
            created_at=order.created_at,
            created_by=order.created_by,
            updated_by=order.updated_by,
            update_at=order.updated_at,
            customer_name=order.customer_name,
            price=order.price,
            payment_method=order.payment_method,
            items_count=order.items_count,
            name_shipping=order.name_shipping,
            phone_shipping=order.phone_shipping,
            address_shipping=order.address_shipping,
            province_code_shipping=order.province_code_shipping,
            ward_code_shipping=order.ward_code_shipping,
            customer_username=order.customer_username,
            status=order.status,
            district_code_shipping=order.district_code_shipping
        ))
    return DataResponse(data=order)