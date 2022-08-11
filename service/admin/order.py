import math
from decimal import Decimal
import pandas as pd
from fastapi import HTTPException
from starlette import status

from model import Order
from project.schemas import Sort, DataResponse, PageResponse
from repo.order import OrderRepo
from repo.order_item import OrderItemRepo
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
        orders = OrderRepo().get_orders_repo_ad(
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

        total_page = math.ceil(len(orders) / size)
        current_page = page
        total_item = len(orders)
        if page and size is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        data = [order['Order'] for order in orders]

        return PageResponse(data=data,
                            total_item=total_item,
                            total_page=total_page,
                            current_page=current_page)

    def get_order_by_id_service(self, order_id: int):
        order = OrderRepo().get_order_by_id_repo(order_id=order_id)
        if order == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        order_item = OrderItemRepo().get_order_items(order_id=order_id)
        data = [order,
                [order_item]]
        return data

    def change_order_status_service(self, order_id: int, next_status: EOrderStatus):
        order = OrderRepo().get_order_by_id_repo(order_id=order_id)
        if order == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        order = OrderRepo().change_order_status_repo(order_id=order_id, next_status=next_status)
        return order
