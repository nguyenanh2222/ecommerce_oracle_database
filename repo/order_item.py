from decimal import Decimal
from typing import List

from sqlalchemy import update
from sqlalchemy.engine import Row
from sqlalchemy.orm import Session
from database import SessionLocal
from model import OrderItem, Order, Sku



class OrderItemRepo():
    def insert_order_item_repo(self, order_item: OrderItem):
        session: Session = SessionLocal()
        order_item = OrderItem(
            created_at=order_item.created_at,
            created_by=order_item.created_by,
            updated_at=order_item.updated_at,
            updated_by=order_item.updated_by,
            shipping_fee=order_item.shipping_fee,
            sku_id=order_item.sku_id,
            name=order_item.name,
            main_image=order_item.main_image,
            item_price=order_item.item_price,
        )
        session.add(order_item)
        session.commit()
        return order_item

    def get_order_items(self, order_id: str) -> List[Row]:
        session: Session = SessionLocal()
        query = session.query(OrderItem).filter(OrderItem.order_id == order_id)
        rs = session.execute(query).fetchall()
        return rs

    def get_order_item_by_sku_id(self, sku_id: int) -> Row:
        session: Session = SessionLocal()
        query = session.query(OrderItem).filter(OrderItem.sku_id == sku_id)
        rs = session.execute(query).fetchone()
        return rs

    def update_order_item_by_sku_id(self, order_id: int, sku_id: int):
        session: Session = SessionLocal()
        stmt = update(OrderItem).values(order_id=order_id).where(
         OrderItem.sku_id == sku_id).returning(OrderItem.order_id)
        rs = session.execute(stmt).fetchone()
        session.commit()
        return rs




