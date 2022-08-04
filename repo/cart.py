from typing import List

from sqlalchemy import insert, delete, select, update
from sqlalchemy.engine import Row
from sqlalchemy.orm import Session

from database import SessionLocal
from model import CartItem
from schema import CartItemReq


class CartItemRepo():
    def insert_cart_item_repo(self, cart_item: CartItemReq, name: str) -> Row:
        session: Session = SessionLocal()
        cart_item = CartItem(created_at=cart_item.created_at,
                             created_by=cart_item.created_by,
                             updated_at=cart_item.updated_at,
                             updated_by=cart_item.updated_by,
                             sku_id=cart_item.sku_id,
                             name=name,
                             main_image=cart_item.main_image,
                             item_price=cart_item.item_price,
                             username=cart_item.username)
        session.add(cart_item)
        session.commit()
        rs = session.get(CartItem, cart_item.id)
        return rs

    def update_cart_item_repo(self,
                              cart_item: CartItemReq,name: str, id: int) -> Row:
        session: Session = SessionLocal()
        stmt = update(CartItem).values(created_at=cart_item.created_at,
                                       created_by=cart_item.created_by,
                                       updated_at=cart_item.updated_at,
                                       updated_by=cart_item.updated_by,
                                       sku_id=cart_item.sku_id,
                                       main_image=cart_item.main_image,
                                       item_price=cart_item.item_price,
                                       username=cart_item.username,
                                       name=name
                                       ).where(CartItem.id == id)
        session.execute(stmt)
        session.commit()
        rs = session.get(CartItem, id)
        return rs


    def get_cart_items_repo(self, username: str) -> List[Row]:
        session: Session = SessionLocal()
        stmt = select(CartItem).where(CartItem.username == username)
        rs = session.execute(stmt).fetchall()
        print(rs)
        return rs

    # def get_cart_item_by_id_repo(self, id: int) -> Row:
    #     session: Session = SessionLocal()
    #     return session.get(CartItem, id)

    def delete_cart_item_by_id_repo(self, id: int):
        session: Session = SessionLocal()
        stmt = delete(CartItem).where(CartItem.id == id)
        session.execute(stmt)
        session.commit()
        cart = session.get(CartItem, id)
        return cart

    def delete_cart_item_by_uername_repo(self, username: str):
        session: Session = SessionLocal()
        stmt = delete(CartItem).where(CartItem.username == username)
        session.execute(stmt)
        session.commit()

