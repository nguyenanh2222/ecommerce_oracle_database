import datetime

from sqlalchemy import DateTime

from project.schemas import DataResponse
from repo.product import ProductRepo
from schema import ProductReq


class ProductService(ProductRepo):
    def insert_product_service(self, product: ProductReq):
        product = ProductRepo().insert_product_repo(ProductReq(
            created_at=product.created_at,
            created_by=product.created_by,
            updated_at=product.updated_at,
            updated_by=product.updated_by,
            name=product.name,
            description=product.description,
            brand=product.brand,
            category_id=product.category_id,
            quantity=product.quantity,
            images=product.images,
            color=product.color,
            price=product.price,
            size_product=product.size_product))

        return product

    def update_product_service(self, product: ProductReq, product_id: int):
        product = ProductRepo().update_product_repo(product_id=product_id,
                                                    product=ProductReq(
                                                        name=product.name,
                                                        description=product.description,
                                                        brand=product.brand,
                                                        created_at=product.created_at,
                                                        created_by=product.created_by,
                                                        updated_at=product.updated_at,
                                                        updated_by=product.updated_by,
                                                        category_id=product.category_id,
                                                        quantity=product.quantity,
                                                        images=product.images,
                                                        color=product.color,
                                                        price=product.price,
                                                        size_product=product.size_product
                                                    ))
        return product

    def get_products_service(self, created_at: datetime, created_by: str,
                             updated_at: datetime, updated_by: str,
                             name: str, category: str,
                             color: str, price: int,
                             brand: str,
                             page: int, size: int) -> DataResponse:
        products = ProductRepo().get_products_repo(created_at=created_at,
                                                   created_by=created_by,
                                                   updated_at=updated_at,
                                                   updated_by=updated_by,
                                                   name=name,
                                                   category=category,
                                                   color=color,
                                                   brand=brand,
                                                   page=page,
                                                   size=size,
                                                   price=price)
        return DataResponse(data=products)
