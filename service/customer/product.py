import math
from decimal import Decimal

from fastapi import HTTPException
from starlette import status

from project.schemas import Sort, PageResponse
from repo.product import ProductRepo


class ProductServiceCus(ProductRepo):
    def get_products_sevice_cus(self,
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
        return PageResponse(data=[product['Product'] for product in products],
                            total_items=total_items,
                            total_page=total_page,
                            current_page=current_page)

    def get_product_id_service_cus(self, product_id: int):
        product = ProductRepo().get_product_id(product_id=product_id)
        if product:
            return product["Product"]
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
