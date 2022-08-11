from decimal import Decimal
from fastapi.params import Query
from starlette import status
from fastapi import APIRouter,HTTPException
from project.schemas import DataResponse, PageResponse, Sort
from repo.order import OrderRepo
from service.admin.order import OrderServiceAd
from status import EOrderStatus

router = APIRouter()


@router.get(
    path="/",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def get_orders(customer_name: str = Query(None),
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
               ) -> PageResponse:
    orders = OrderServiceAd().get_order_service(
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
    return PageResponse(data=orders.data,
                        total_item=orders.total_items,
                        total_page=orders.total_page,
                        current_page=orders.current_page)


@router.get(
    path="/{id}",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def get_order_by_id(order_id: int) -> DataResponse:
    order = OrderServiceAd().get_order_by_id_service(order_id=order_id)
    return DataResponse(data=order)



@router.put(
    path="/change_status",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def change_order_status(order_id: int, next_status: EOrderStatus) -> DataResponse:
    order = OrderServiceAd().change_order_status_service(order_id=order_id, next_status=next_status)
    return DataResponse(data=order)
