from decimal import Decimal
from fastapi.params import Query
from pydantic.datetime_parse import datetime
from starlette import status
from fastapi import APIRouter

from model import Order
from project.schemas import DataResponse, PageResponse, Sort
from schema import OrderReq
from service.admin.order import OrderService
from status import EOrderStatus

router = APIRouter()


@router.get(
    path="/orders",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def get_products_service(created_at: datetime = Query(datetime.strptime("2021-11-29", "%Y-%m-%d")),
                         created_by: str = Query(None),
                         updated_at: datetime = Query(datetime.strptime("2021-11-29", "%Y-%m-%d")),
                         updated_by: str = Query(None),
                         customer_name: str = Query(None),
                         from_price: Decimal = Query(None),
                         to_price: Decimal = Query(None),
                         id: int = Query(None),
                         payment_method: str = Query(None),
                         name_shipping: str = Query(None),
                         phone_shipping: str = Query(None),
                         address_shipping: str = Query(None),
                         province_code_shipping: str = Query(None),
                         ward_code_shipping: str = Query(None),
                         district_code_shipping: str = Query(None),
                         customer_username: str = Query(None),
                         sort_direction: Sort.Direction = Query(None),
                         page: int = Query(1),
                         size: int = Query(10)
                         ) -> DataResponse:
    orders = OrderService().get_order_service(created_at=created_at,
                                              created_by=created_by,
                                              updated_at=updated_at,
                                              updated_by=updated_by,
                                              customer_name=customer_name,
                                              from_price=from_price,
                                              to_price=to_price,
                                              id=id,
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
    return DataResponse(data=orders)


@router.get(
    path="/{id}",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def get_order_by_id_repo(order_id: int) -> DataResponse:
    order = OrderService().get_order_by_id_service(order_id=order_id)
    return DataResponse(data=order)


@router.post(
    path="/order",
    response_model=DataResponse,
    status_code=status.HTTP_201_CREATED
)
def insert_order(order: OrderReq):
    order = OrderService().insert_order(
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


@router.put(
    path="/change_status",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)


def change_order_status(order_id: int, next_status: EOrderStatus) -> DataResponse:
    order = OrderService().change_order_status_service(order_id=order_id, next_status=next_status)
    return DataResponse(data=order)
