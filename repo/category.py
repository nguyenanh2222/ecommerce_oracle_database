from sqlalchemy.orm import Session

from database import SessionLocal
from model import Category


class CategoryRepo():
    def get_categories(self):
        session: Session = SessionLocal()
        query = session.query(Category)
        rs = session.execute(query).fetchall()
        return rs

    def get_category_by_id(self, id):
        session: Session = SessionLocal()
        query = session.query(Category).filter(
            Category.id == id)
        rs = session.execute(query).fetchone()
        return rs
