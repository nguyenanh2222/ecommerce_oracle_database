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
        session.commit()
        stmt = insert(Sku).values(created_at=product.created_at,
                                  created_by=product.created_by,
                                  updated_at=product.updated_at,
                                  updated_by=product.updated_by,
                                  quantity=product.skus[0].quantity,
                                  images=product.skus[0].images,
                                  color=product.skus[0].color,
                                  price=product.skus[0].price,
                                  size_product=product.skus[0].size_product,
                                  status=product.skus[0].status,
                                  seller_sku=product.skus[0].seller_sku,
                                  package_width=product.skus[0].package_width,
                                  package_height=product.skus[0].package_height,
                                  package_length=product.skus[0].package_length,
                                  package_weight=product.skus[0].package_weight,
                                  )
        rs = session.execute(stmt).fetchone()
        session.commit()
        return rs

    def update_product_repo(self, product_id: int, product: ProductReq) -> Row:
        session: Session = SessionLocal()
        stmt = update(Product).values(created_at=product.created_at,
                                      created_by=product.created_by,
                                      updated_at=product.updated_at,
                                      updated_by=product.updated_by,
                                      name=product.name,
                                      description=product.description,
                                      brand=product.brand,
                                      category_id=product.category_id
                                      ).where(Product.id==product_id)
        session.execute(stmt)
        session.commit()
        stmt = update(Sku).values(created_at=product.created_at,
                                  created_by=product.created_by,
                                  updated_at=product.updated_at,
                                  updated_by=product.updated_by,
                                  quantity=product.skus[0].quantity,
                                  images=product.skus[0].images,
                                  color=product.skus[0].color,
                                  price=product.skus[0].price,
                                  size_product=product.skus[0].size_product,
                                  status=product.skus[0].status,
                                  seller_sku=product.skus[0].seller_sku,
                                  package_width=product.skus[0].package_width,
                                  package_height=product.skus[0].package_height,
                                  package_length=product.skus[0].package_length,
                                  package_weight=product.skus[0].package_weight,
                                  ).where(Sku.product_id==product_id)
        session.execute(stmt)
        session.commit()
        rs = session.get(Product, product_id)
        return rs

    def get_products_repo(self,
                          name: str, category: str,
                          color: str,
                          from_price: Decimal, to_price: Decimal,
                          brand: str,
                          page: int, size: int,
                          sort_direction: Sort.Direction) -> List[Row]:
        session: Session = SessionLocal()
        query = session.query(Product)
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
        query = delete(Sku).where(Sku.product_id == product_id)
        session.execute(query)
        session.commit()
        query = delete(Product).where(Product.id == product_id)
        session.commit()
        session.execute(query)
        return session.get(Product, product_id)
