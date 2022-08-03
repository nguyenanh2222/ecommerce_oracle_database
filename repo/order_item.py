from decimal import Decimal
from typing import List

from sqlalchemy.engine import Row
from sqlalchemy.orm import Session
from database import SessionLocal
from model import OrderItem
from schema import OrderItemReq

class OrderItemRepo():
    def insert_order_item_repo(self, order_item: OrderItemReq, paid_price: Decimal):
        session: Session = SessionLocal()
        order_item = OrderItem(
            created_at=order_item.created_at,
            created_by=order_item.created_by,
            updated_at=order_item.updated_at,
            updated_by=order_item.updated_by,
            order_id=order_item.order_id,
            sku_id=order_item.sku_id,
            name=order_item.name,
            main_image=order_item.main_image,
            item_price=order_item.item_price,
            paid_price=order_item.paid_price,
            shipping_fee=order_item.shipping_fee
        )
        session.add(order_item)
        session.commit()
        order_item = session.get(OrderItem, order_item.order_id)
        return order_item

    def get_order_items(self, order_id: str) -> List[Row]:
        session: Session = SessionLocal()
        query = session.query(OrderItem).filter(OrderItem.order_id == order_id)
        rs = session.execute(query).fetchall()
        return rs

