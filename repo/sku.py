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

    def get_skus_repo(self):
        ...

    def delete_sku_repo(self):
        ...
