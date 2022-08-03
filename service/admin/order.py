from decimal import Decimal
import pandas as pd
from fastapi import HTTPException
from starlette import status

from model import Order
from project.schemas import Sort, DataResponse, PageResponse
from repo.order import OrderRepo
from schema import OrderReq
from status import EOrderStatus


class OrderServiceAd(OrderRepo):
    def get_order_service(self,
                          customer_name: str, from_price: Decimal, to_price: Decimal,
                          id: int, payment_method: str, name_shipping: str,
                          phone_shipping: str, address_shipping: str,
                          province_code_shipping: str, ward_code_shipping: str,
                          district_code_shipping: str,
                          customer_username: str,
                          sort_direction: Sort.Direction,
                          page: int, size: int) -> PageResponse:
        orders = OrderRepo().get_orders_repo(
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

        total_page = len(orders) / size
        current_page = page
        total_item = len(orders)
        if page and size is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        return PageResponse(data=orders,
                            total_item=total_item,
                            total_page=total_page,
                            current_page=current_page)

    def get_order_by_id_service(self, order_id: int) -> DataResponse:
        order = OrderRepo().get_order_by_id_repo(order_id=order_id)
        return DataResponse(data=order)

    def change_order_status_service(self, order_id: int, next_status: EOrderStatus) -> DataResponse:
        order = OrderRepo().change_order_status_repo(order_id=order_id, next_status=next_status)
        return DataResponse(data=order)


