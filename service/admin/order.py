from datetime import datetime
from decimal import Decimal
from typing import List

import pandas as pd
from DateTime import DateTime
from fastapi import HTTPException
from starlette import status

from model import Order
from project.schemas import PageResponse, Sort, DataResponse
from repo.order import OrderRepo
from schema import OrderReq
from status import EOrderStatus


class OrderService(OrderRepo):
    def get_order_service(self, created_at: DateTime, created_by: str,
                          updated_at: DateTime, updated_by: str,
                          customer_name: str, from_price: Decimal, to_price: Decimal,
                          id: int, payment_method: str, name_shipping: str,
                          phone_shipping: str, address_shipping: str,
                          province_code_shipping: str, ward_code_shipping: str,
                          district_code_shipping: str,
                          customer_username: str,
                          sort_direction: Sort.Direction,
                          page: int, size: int) -> DataResponse:
        orders = OrderRepo().get_orders_repo(created_at=created_at,
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
        total_page = len(orders) / size
        current_page = page
        total_item = len(orders)
        if page and size is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        return DataResponse(data=orders,
                            total_item=total_item,
                            total_page=total_page,
                            current_page=current_page)

    def get_order_by_id_service(self, order_id: int) -> DataResponse:
        order = OrderRepo().get_order_by_id_repo(order_id=order_id)
        return DataResponse(data=order)

    def insert_order(self, order: OrderReq):
        data_district = pd.read_excel('./district_29_07.xls', dtype=str)['Mã']
        data_province = pd.read_excel('./province_29_07.xls', dtype=str)['Mã']
        data_ward = pd.read_excel('./ward_29_07.xls', dtype=str)['Mã']
        province_code = '001'
        ward_code = '002'
        district_code = '003'
        for item in data_ward:
            if order.ward_code_shipping == item:
                ward_code = item
        for item in data_district:
            if order.district_code_shipping == item:
                district_code = item
        for item in data_province:
            if order.province_code_shipping == item:
                province_code = item
        order = OrderRepo().insert_order(Order(
            created_at=order.created_at,
            created_by=order.created_by,
            updated_by=order.updated_by,
            updated_at=order.updated_at,
            customer_name=order.customer_name,
            price=order.price,
            payment_method=order.payment_method,
            items_count=order.items_count,
            name_shipping=order.name_shipping,
            phone_shipping=order.phone_shipping,
            address_shipping=order.address_shipping,
            province_code_shipping=province_code,
            ward_code_shipping=ward_code,
            customer_username=order.customer_username,
            status=order.status,
            district_code_shipping=district_code
        ))
        return order

    def change_order_status_service(self, order_id: int, next_status: EOrderStatus) -> DataResponse:
        order = OrderRepo().change_order_status_repo(order_id=order_id, next_status=next_status)
        return DataResponse(data=order)
