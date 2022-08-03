from typing import List
import pandas as pd
from starlette import status

from model import Order
from repo.cart import CartItemRepo
from repo.customer import CustomerRepo
from repo.order import OrderRepo
from repo.order_item import OrderItemRepo
from schema import OrderItemReq, OrderReq
from status import EOrderStatus


class OrderServiceCus(OrderRepo):
    def insert_order_item(self, order_item: OrderItemReq, username: str) -> List:
        cart_items = CartItemRepo().get_cart_items_repo(username=username)
        order_items = []
        for cart_item in cart_items:
            order_item = OrderItemRepo().insert_order_item_repo(
                order_item=OrderItemReq(
                    created_at=cart_item['CartItem'].created_at,
                    created_by=cart_item['CartItem'].created_by,
                    updated_by=cart_item['CartItem'].updated_by,
                    updated_at=cart_item['CartItem'].updated_at,
                    sku_id=cart_item['CartItem'].sku_id,
                    name=cart_item['CartItem'].name,
                    main_image=cart_item['CartItem'].main_image,
                    item_price=cart_item['CartItem'].item_price,
                    order_id=order_item.order_id,
                    shipping_fee=order_item.shipping_fee,
                    item_discount=order_item.item_discount),
                paid_price=cart_item['CartItem'].item_price - cart_item['CartItem'].item_price * order_item.discount
            )
            order_items.append(order_item)
        return order_items


    def insert_order_service(self, order: OrderReq):
        customer = CustomerRepo().get_customer_by_username_repo(username=order.customer_username)
        order_items = self.insert_order_item(username=order.customer_username)
        paid_price = 0
        for order_item in order_items:
            paid_price += order_item['OrderItem'].item_price - order_item['OrderItem'].item_price * order_item[
                'OrderItem'].discount
        shipping_fee = order.shipping_fee_original - order.shipping_fee_original * order.shipping_fee_discount
        price = paid_price + shipping_fee
        order_id = OrderRepo().insert_order(Order(
            created_at=order.created_at,
            created_by=order.created_by,
            updated_by=order.updated_by,
            updated_at=order.updated_at,
            price=price,
            shipping_fee_original=order.shipping_fee_original,
            shipping_fee_discount=order.shipping_fee_discount,
            payment_method=order.payment_method,
            name_shipping=order.name_shipping,
            status=EOrderStatus.PENDING,
            customer_name=customer['Customer'].name,
            phone_shipping=customer['Customer'].phone,
            address_shipping=customer['Customer'].address_shipping,
            province_code_shipping=customer['Customer'].province_code_shipping,
            ward_code_shipping=customer['Customer'].ward_code_shipping,
            customer_username=customer['Customer'].username,
            district_code_shipping=customer['Customer'].district_code_shipping
        ),
            items_count=len(order_items),
        )
        order = OrderRepo().get_order_by_id_repo(order_id)
        return order
