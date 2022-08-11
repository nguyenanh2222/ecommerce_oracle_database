import math
from datetime import datetime
from decimal import Decimal
from typing import List
from fastapi import HTTPException
from numpy import ceil
from sqlalchemy.engine import Row
from starlette import status
from model import Order, OrderItem
from project.schemas import Sort, PageResponse
from repo.cart import CartItemRepo
from repo.customer import CustomerRepo
from repo.order import OrderRepo
from repo.order_item import OrderItemRepo
from repo.sku import SkuRepo
from schema import OrderReq
from status import EOrderStatus


class OrderServiceCus(OrderRepo):
    def insert_order_item_service(self, username: str) -> List:
        cart_items = CartItemRepo().get_cart_items_repo(username=username)
        order_items = []
        for cart_item in cart_items:
            sku = SkuRepo().get_sku_by_id_repo(cart_item.sku_id)
            if sku['Sku'].package_weight < 0.1:
                sku['Sku'].package_weight = 0.1
            shipping_fee = sku['Sku'].package_weight * 1_500
            order_item = OrderItemRepo().insert_order_item_repo(OrderItem(
                sku_id=cart_item.sku_id,
                name=cart_item.name,
                main_image=cart_item.main_image,
                item_price=cart_item.item_price,
                created_at=datetime.now(),
                created_by=cart_item.created_by,
                updated_by=cart_item.updated_by,
                updated_at=datetime.now(),
                shipping_fee=shipping_fee,
            )
            )
            order_items.append(order_item)
        return order_items

    def insert_order_service(self, order: OrderReq) -> Row:
        cart_items = CartItemRepo().get_cart_items_repo(username=order.customer_username)
        if cart_items == []:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        customer = CustomerRepo().get_customer_by_username_repo(
            username=order.customer_username)
        if customer == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        if order.customer_username == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        order_items = []
        for cart_item in cart_items:
            order_item = OrderItemRepo().get_order_item_by_sku_id(cart_item.sku_id)
            order_items.append(order_item)
        price = 0
        items_count = 0
        shipping_fee = 0
        for order_item in order_items:
            price += order_item['OrderItem'].item_price
            items_count += 1
            shipping_fee += order_item['OrderItem'].shipping_fee

        price = price - price * order.discount + shipping_fee * order.shipping_fee_discount

        order_id = OrderRepo().insert_order(Order(
            created_at=order.created_at,
            created_by=order.created_by,
            updated_by=order.updated_by,
            updated_at=order.updated_at,
            discount=order.discount,
            shipping_fee_original=shipping_fee,
            shipping_fee_discount=order.shipping_fee_discount,
            payment_method=order.payment_method,
            name_shipping=order.name_shipping,
            price=price,
            status=EOrderStatus.PENDING,
            customer_name=customer['Customer'].lastname + customer['Customer'].firstname,
            phone_shipping=customer['Customer'].phone,
            address_shipping=customer['Customer'].address,
            province_code_shipping=customer['Customer'].province_code,
            ward_code_shipping=customer['Customer'].ward_code,
            customer_username=customer['Customer'].username,
            district_code_shipping=customer['Customer'].district_code,
        ),
            items_count=items_count,
        )
        cart_items = CartItemRepo().get_cart_items_repo(username=order.customer_username)
        for cart_item in cart_items:
            _order_item = OrderItemRepo().update_order_item_by_sku_id(order_id=order_id)

        order = OrderRepo().get_order_by_id_repo(order_id=order_id)

        _cart_item = CartItemRepo().delete_cart_item_by_username_repo(username=order['Order'].customer_username)

        return order

    def get_orders_cus_service(self,
                               from_price: Decimal,
                               to_price: Decimal,
                               payment_method: str,
                               name_shipping: str,
                               phone_shipping: str,
                               address_shipping: str,
                               province_code_shipping: str,
                               ward_code_shipping: str,
                               district_code_shipping: str,
                               customer_username: str,
                               sort_direction: str,
                               page: int,
                               size: int
                               ):
        orders = OrderRepo().get_orders_cus_repo(from_price=from_price,
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
                                                 page=page,
                                                 size=size
                                                 )
        total_page = math.ceil(len(orders) / size)
        current_page = page
        total_items = len(orders)

        if page and size is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        data = [order["Order"] for order in orders]

        return PageResponse(data=data,
                            total_items=total_items,
                            total_page=total_page,
                            current_page=current_page)

