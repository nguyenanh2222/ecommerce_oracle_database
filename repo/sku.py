from sqlalchemy import update
from sqlalchemy.engine import Row
from sqlalchemy.orm import Session
from database import SessionLocal
from model import Sku


class SkuRepo():
    def get_sku_by_id_repo(self, sku_id: int) -> Row:
        session: Session = SessionLocal()
        query = session.query(Sku).filter(Sku.id == sku_id)
        rs = session.execute(query).fetchone()
        return rs


    def delete_sku_repo(self):
        ...

    def update_sku_quantity_repo(self, quantity: int, product_id: int):
        session: Session = SessionLocal()
        query = update(Sku).values(quantity=quantity).where(Sku.product_id == product_id)