import datetime
import math
from decimal import Decimal

from fastapi import HTTPException
from starlette import status

from project.schemas import DataResponse, Sort
from repo.product import ProductRepo
from schema import ProductReq


class ProductService(ProductRepo):
    def insert_product_service(self, product: ProductReq) -> DataResponse:
        #case category_id : must have in table category
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

        return DataResponse(data=product)

    def update_product_service(self, product: ProductReq, product_id: int):
        #case category_id not found
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
                             color: str, from_price: Decimal, to_price: Decimal,
                             brand: str,
                             page: int, size: int,
                             sort_direction: Sort.Direction,) -> DataResponse:
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
                                                   from_price=from_price,
                                                   to_price=to_price,
                                                   sort_direction=sort_direction)
        total_page = math.ceil(len(products) / size)
        total_items = len(products)
        current_page = page

        if page and size is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return DataResponse(data=products,
                            total_items=total_items,
                            total_page=total_page,
                            current_page=current_page)

    def get_all_products_service(self) -> DataResponse:
        products = ProductRepo().get_all_products()
        return DataResponse(data=products)

    def get_product_id_service(self, product_id: int) -> DataResponse:
        product = ProductRepo().get_product_id(product_id=product_id)
        return DataResponse(data=product)

    def delete_product_service(self, product_id: int):
        product = ProductRepo().delete_product_repo(product_id=product_id)


