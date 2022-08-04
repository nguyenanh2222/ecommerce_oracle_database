from datetime import datetime
from typing import List

from fastapi import HTTPException
from sqlalchemy.engine import Row
from starlette import status

from model import Order, OrderItem
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
            sku = SkuRepo().get_sku_by_id_repo(cart_item['CartItem'].sku_id)
            if sku['Sku'].package_weight < 0.1:
                sku['Sku'].package_weight = 0.1
            shipping_fee = sku['Sku'].package_weight * 1_500
            order_item = OrderItemRepo().insert_order_item_repo(OrderItem(
                sku_id=cart_item['CartItem'].sku_id,
                name=cart_item['CartItem'].name,
                main_image=cart_item['CartItem'].main_image,
                item_price=cart_item['CartItem'].item_price,
                created_at=datetime.now(),
                created_by=cart_item['CartItem'].created_by,
                updated_by=cart_item['CartItem'].updated_by,
                updated_at=datetime.now(),
                shipping_fee=shipping_fee,
            )
            )
            order_items.append(order_item)
        return order_items

    def insert_order_service(self, order: OrderReq) -> Row:
        cart_items = CartItemRepo().get_cart_items_repo(username=order.customer_username)
        customer = CustomerRepo().get_customer_by_username_repo(
            username=order.customer_username)
        if customer == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        if order.customer_username == None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        order_items = []
        for cart_item in cart_items:
            order_item = OrderItemRepo().get_order_item_by_sku_id(cart_item['CartItem'].sku_id)
            order_items.append(order_item)
        price = 0
        items_count = 0
        shipping_fee = 0
        for order_item in order_items:
            price += order_item['OrderItem'].item_price
            items_count += 1
            shipping_fee += order_item['OrderItem'].shipping_fee

        price = price + shipping_fee*order.shipping_fee_discount

        order_id = OrderRepo().insert_order(Order(
            created_at=order.created_at,
            created_by=order.created_by,
            updated_by=order.updated_by,
            updated_at=order.updated_at,
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
            district_code_shipping=customer['Customer'].district_code
        ),
            items_count=items_count,
        )
        cart_items = CartItemRepo().get_cart_items_repo(username=order.customer_username)
        for cart_item in cart_items:
            order_item = OrderItemRepo().update_order_item_by_sku_id(sku_id=cart_item['CartItem'].sku_id,
                                                                     order_id=order_id)
        order = OrderRepo().get_order_by_id_repo(order_id=order_id)
        cart_item = CartItemRepo().delete_cart_item_by_uername_repo(username=order['Order'].customer_username)

        return order
