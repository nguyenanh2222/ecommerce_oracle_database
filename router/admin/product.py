from datetime import datetime
from decimal import Decimal

from starlette import status
from fastapi import APIRouter, Query, Body
from starlette.responses import FileResponse

from project.schemas import DataResponse, Sort
from router.examples.product import product_op1
from schema import ProductRes, ProductReq, SkuReq
from service.admin.product import ProductService
from status import EOrderStatus

router = APIRouter()


@router.post(
    path='/product',
    response_model=DataResponse[ProductRes],
    status_code=status.HTTP_201_CREATED
)
def insert_product(product: ProductReq = Body(..., examples=product_op1)):
    product = ProductService().insert_product_service(ProductReq(
        name=product.name,
        description=product.description,
        brand=product.brand,
        created_at=product.created_at,
        created_by=product.created_by,
        updated_at=product.updated_at,
        updated_by=product.updated_by,
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
    return DataResponse(data=product)


@router.put(
    path='/product',
    response_model=DataResponse[ProductRes],
    status_code=status.HTTP_200_OK
)
def update_product(product: ProductReq, product_id: int):
    product = ProductService().update_product_service(ProductReq(
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
        size_product=product.size_product),
        product_id=product_id)
    return DataResponse(data=product)


@router.get(
    path="/products",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def get_products(created_at: datetime = Query(datetime.strptime("2021-11-29", "%Y-%m-%d"),
                                              description="Create at"),
                 created_by: str = Query(None, description="Create by"),
                 updated_at: datetime = Query(datetime.strptime("2021-11-29", "%Y-%m-%d"),
                                              description="Update at"),
                 updated_by: str = Query(None, description="Update by"),
                 name: str = Query(None, description="Name"),
                 category: str = Query(None, description="Category"),
                 color: str = Query(None, description="Color"),
                 from_price: Decimal = Query(None, description="Price"),
                 to_price: Decimal = Query(None, description="Price"),
                 brand: str = Query(None, description="Brand"),
                 page: int = Query(1, description="Page"),
                 size: int = Query(10, description="Size in a page"),
                 sort_direction: Sort.Direction = Query(None)) -> DataResponse:
    products = ProductService().get_products_service(created_at=created_at,
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
    return DataResponse(data=products)


@router.get(
    path="/product",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def get_product_id(product_id: int) -> DataResponse:
    product = ProductService().get_product_id(product_id=product_id)
    return DataResponse(data=product)


@router.delete(
    path="/product",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_product(product_id: int):
    product = ProductService().delete_product_service(product_id=product_id)


@router.get(
    path="/files/{name}"
)
async def get_file(name: str):
    return FileResponse(f"files/{name}")
