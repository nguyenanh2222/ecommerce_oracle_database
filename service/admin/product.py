import datetime
import math
from decimal import Decimal

from fastapi import HTTPException
from starlette import status

from project.schemas import DataResponse, Sort, PageResponse
from repo.product import ProductRepo
from schema import ProductReq, SkuReq


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
            skus=[SkuReq(created_at=product.created_at,
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

                         )]))
        return product

    def update_product_service(self, product: ProductReq, product_id: int):
        product = ProductRepo().update_product_repo(product_id=product_id,
                                                    product=ProductReq(
                                                        created_at=product.created_at,
                                                        created_by=product.created_by,
                                                        updated_at=product.updated_at,
                                                        updated_by=product.updated_by,
                                                        name=product.name,
                                                        description=product.description,
                                                        brand=product.brand,
                                                        category_id=product.category_id,
                                                        skus=[SkuReq(created_at=product.created_at,
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
                                                                     package_weight=product.skus[0].package_weight
                                                                     )]))
        return product

    def get_products_service(self,
                             name: str, category: str,
                             color: str, from_price: Decimal, to_price: Decimal,
                             brand: str,
                             page: int, size: int,
                             sort_direction: Sort.Direction, ) -> PageResponse:
        products = ProductRepo().get_products_repo(
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
        return PageResponse(data=products,
                            total_items=total_items,
                            total_page=total_page,
                            current_page=current_page)

    def get_product_id_service(self, product_id: int):
        product = ProductRepo().get_product_id(product_id=product_id)
        if product:
            return product
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


    def delete_product_service(self, product_id: int):
        product = ProductRepo().delete_product_repo(product_id=product_id)
        return product
