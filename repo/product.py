from sqlalchemy import insert
from sqlalchemy.engine import Row
from sqlalchemy.orm import Session
from database import SessionLocal
from model import Product, Sku
from schema import ProductReq, SkuReq


class ProductRepo:
    def insert_product_repo(self, product: ProductReq):
        session: Session = SessionLocal()
        # stmt = insert(Product).values(created_at=product.created_at,
        #                               created_by=product.created_by,
        #                               updated_at=product.updated_at,
        #                               updated_by=product.updated_by,
        #                               name=product.name,
        #                               description=product.description,
        #                               brand=product.brand,
        #                               category_id=product.category_id
        #                               )
        # session.execute(stmt)
        # stmt = insert(Sku).values(created_at=product.created_at,
        #                           created_by=product.created_by,
        #                           updated_at=product.updated_at,
        #                           updated_by=product.updated_by,
        #                           quantity=product.quantity,
        #                           images=product.images,
        #                           color=product.color,
        #                           price=product.price,
        #                           size_product=product.size_product)
        p = Product(
            created_at=product.created_at,
            created_by=product.created_by,
            updated_at=product.updated_at,
            updated_by=product.updated_by,
            name=product.name,
            description=product.description,
            brand=product.brand,
            category_id=product.category_id
        )
        # session.execute(stmt)
        session.add(p)
        session.commit()
        # return product

    def update_product_repo(self, id: int, product: ProductReq) -> Row:
        # Ma SKU khong thay doi
        # them update price, quantity, status, images, seller_sku, color
        # size bao gom width, height, length, weight
        session: Session = SessionLocal()
        session.query(Product).filter(Product.id == id).update(ProductReq(created_at=product.created_at,
                                                                          created_by=product.created_by,
                                                                          updated_at=product.updated_at,
                                                                          updated_by=product.updated_by,
                                                                          name=product.name,
                                                                          description=product.description,
                                                                          brand=product.brand,
                                                                          category_id=product.category_id))
        session.commit()
        product = session.get(product, product.id)
        return product

    # def get_products_repo(self, created_at: date, created_by: str,
    #                       updated_at: date, updated_by: str,
    #                       name: str, category: str,
    #
    #                       page: int, size: int) -> List[Row]:
    #     session: Session = SessionLocal()
    #     query = select(productRole).join(product, product.productname)
    #     if created_at:
    #         query += query.where(product.created_at == created_at)
    #     if updated_at:
    #         query += query.where(product.updated_at == updated_at)
    #     if created_by:
    #         query += query.where(product.created_by == created_by)
    #     if updated_by:
    #         query += query.where(product.updated_by == updated_by)
    #     if first_name:
    #         query += query.where(product.firstname == first_name)
    #     if last_name:
    #         query += query.where(product.lastname == last_name)
    #     if page and size:
    #         query += query.limit(size).offset((page - 1) * size)
    #     rs = session.execute(query).fetchall()
    #     return rs
    #
    # def get_permission_repo(self, permission_name: str, role_name: str):
    #     session: Session = SessionLocal()
    #     query = select(RolePermission).join(Permission, Permission.code).join(Role, Role.code)
    #     if permission_name:
    #         query += query.where(Permission.name == permission_name)
    #     if role_name:
    #         query += query.where(Role.name == role_name)
    #     rs = session.execute(query).fetchall()
    #     return rs
    #
    # def delete_product_repo(self, productname: str):
    #     session: Session = SessionLocal()
    #     query = delete(product).where(product.productname == productname).returning(product)
    #     rs = session.execute(query).fetchone()
    #     return rs
