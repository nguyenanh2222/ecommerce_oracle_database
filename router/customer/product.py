from decimal import Decimal

from fast_boot.schemas import Sort
from fastapi import APIRouter, Query
from starlette import status

from project.schemas import DataResponse, PageResponse
from service.customer.product import ProductServiceCus

router = APIRouter()

@router.get(
    path="/",
    response_model=PageResponse,
    status_code=status.HTTP_200_OK
)
def get_products(
                 name: str = Query(default=None, max_length=200, description="Name"),
                 category: str = Query(default=None, max_length=200, description="Category"),
                 color: str = Query(default=None, max_length=200, description="Color"),
                 from_price: Decimal = Query(default=None, gt=0, description="Price"),
                 to_price: Decimal = Query(default=None, gt=0, description="Price"),
                 brand: str = Query(default=None, max_length=200, description="Brand"),
                 page: int = Query(1,gt=0, description="Page"),
                 size: int = Query(100,gt=0, description="Size in a page"),
                 sort_direction: Sort.Direction = Query(None)
) -> PageResponse:
    products = ProductServiceCus().get_products_sevice_cus(
                                                     name=name,
                                                     category=category,
                                                     color=color,
                                                     brand=brand,
                                                     page=page,
                                                     size=size,
                                                     from_price=from_price,
                                                     to_price=to_price,
                                                     sort_direction=sort_direction
    )
    return PageResponse(data=products.data,
                        total_page=products.total_page,
                        total_items=products.total_items,
                        current_page=products.current_page)


@router.get(
    path="/{id}",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def get_product_id(product_id: int) -> DataResponse:
    product = ProductServiceCus().get_product_id_service_cus(product_id=product_id)
    return DataResponse(data=product)
