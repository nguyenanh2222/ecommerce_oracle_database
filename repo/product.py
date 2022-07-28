
from typing import List

from sqlalchemy import insert, select, update, DateTime
from sqlalchemy.engine import Row
from sqlalchemy.orm import Session
from database import SessionLocal
from model import Product, Sku
from schema import ProductReq, SkuReq


class ProductRepo:
    def insert_product_repo(self, product: ProductReq):
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

    def get_products_repo(self, created_at: DateTime, created_by: str,
                          updated_at: DateTime, updated_by: str,
                          name: str, category: str,
                          color: str, price: int,
                          brand: str,
                          page: int, size: int) -> List[Row]:
        session: Session = SessionLocal()
        query = select(Product).join(Sku, Sku.product_id)
        if created_at:
            query += query.where(Product.created_at == created_at)
        if updated_at:
            query += query.where(Product.updated_at == updated_at)
        if created_by:
            query += query.where(Product.c.created_by.like(f"%{created_by}%"))
        if updated_by:
            query += query.where(Product.c.update_by.like(f"%{created_by}%"))
        if name:
            query += query.where(Product.c.name.like(f"%{name}%"))
        if category:
            query += query.where(Product.c.catrpory.like(f"%{name}%"))
        if name:
            query += query.where(Product.c.name.like(f"%{name}%"))
        if color:
            query += query.where(Product.c.color.like(f"%{name}%"))
        if price:
            query += query.where(Product.c.price == price)
        if brand:
            query += query.where(Product.c.brand.like(f"%{name}%"))
        if page and size:
            query += query.limit(size).offset((page - 1) * size)
        rs = session.execute(query).fetchall()
        return rs



    #
    # def delete_product_repo(self, productname: str):
    #     session: Session = SessionLocal()
    #     query = delete(product).where(product.productname == productname).returning(product)
    #     rs = session.execute(query).fetchone()
    #     return rs
