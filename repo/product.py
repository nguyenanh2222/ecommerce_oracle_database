from decimal import Decimal
from typing import List

from sqlalchemy import insert, select, update, DateTime, delete
from sqlalchemy.engine import Row
from sqlalchemy.orm import Session
from database import SessionLocal
from model import Product, Sku
from project.schemas import Sort
from schema import ProductReq, SkuReq


class ProductRepo:
    def insert_product_repo(self, product: ProductReq) -> Row:
        session: Session = SessionLocal()
        stmt = insert(Product).values(created_at=product.created_at,
                                      created_by=product.created_by,
                                      updated_at=product.updated_at,
                                      updated_by=product.updated_by,
                                      name=product.name,
                                      description=product.description,
                                      brand=product.brand,
                                      category_id=product.category_id
                                      )
        session.execute(stmt)
        stmt = insert(Sku).values(created_at=product.created_at,
                                  created_by=product.created_by,
                                  updated_at=product.updated_at,
                                  updated_by=product.updated_by,
                                  quantity=product.quantity,
                                  images=product.images,
                                  color=product.color,
                                  price=product.price,
                                  size_product=product.size_product)
        session.execute(stmt)
        session.commit()
        return product

    def update_product_repo(self, product_id: int, product: ProductReq) -> Row:
        session: Session = SessionLocal()
        stmt = update(Product).where(Product.id == product_id).values(created_at=product.created_at,
                                                                      created_by=product.created_by,
                                                                      updated_at=product.updated_at,
                                                                      updated_by=product.updated_by,
                                                                      name=product.name,
                                                                      description=product.description,
                                                                      brand=product.brand,
                                                                      category_id=product.category_id)
        session.execute(stmt)
        stmt = update(Sku).where(Sku.id == product_id).values(
            created_at=product.created_at,
            created_by=product.created_by,
            updated_at=product.updated_at,
            updated_by=product.updated_by,
            quantity=product.quantity,
            images=product.images,
            color=product.color,
            price=product.price,
            size_product=product.size_product)
        session.execute(stmt)
        session.commit()
        product = session.get(Product, product_id)
        return product

    def get_products_repo(self, created_at: DateTime, created_by: str,
                          updated_at: DateTime, updated_by: str,
                          name: str, category: str,
                          color: str,
                          from_price: Decimal, to_price: Decimal,
                          brand: str,
                          page: int, size: int,
                          sort_direction: Sort.Direction) -> List[Row]:
        session: Session = SessionLocal()
        query = session.query(Product)
        if created_at:
            query = query.filter(Product.created_at == created_at)
        if updated_at:
            query = query.filter(Product.updated_at == updated_at)
        if created_by:
            query = query.filter(Product.created_by.like(f"%{created_by}%"))
        if updated_by:
            query = query.filter(Product.updated_by.like(f"%{created_by}%"))
        if name:
            query = query.filter(Product.name.like(f"%{name}%"))
        if category:
            query = query.filter(Product.catrpory.like(f"%{name}%"))
        if name:
            query = query.filter(Product.name.like(f"%{name}%"))
        if color:
            query = query.filter(Product.color.like(f"%{name}%"))
        if from_price:
            query = query.filter(Product.price == from_price)
        if to_price:
            query = query.filter(Product.price == to_price)
        if brand:
            query = query.filter(Product.brand.like(f"%{name}%"))
        if sort_direction == 'asc':
            query = query.order_by(Product.created_time)
        if sort_direction == 'desc':
            query = query.order_by(Product.created_time).desc()
        if page and size:
            query = query.limit(size).offset((page - 1) * size)
        rs = session.execute(query).fetchall()
        return rs


    def get_product_id(self, product_id: int) -> Row:
        session: Session = SessionLocal()
        rs = session.query(Product).filter(Product.id == product_id).first()
        return rs

    def delete_product_repo(self, product_id: int):
        session: Session = SessionLocal()
        query = delete(Product).where(Product.id == product_id)
        session.execute(query)
