import os
from datetime import datetime
from decimal import Decimal

from fastapi.encoders import jsonable_encoder
from fastapi.openapi.models import Response
from starlette import status
from fastapi import APIRouter, Query, Body, UploadFile
from starlette.responses import FileResponse

from project.schemas import DataResponse, Sort, PageResponse
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
def update_product(product_id: int, product: ProductReq = Body(..., examples=product_op1)):
    product = ProductService().update_product_service(product_id=product_id,
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
    return DataResponse(data=product)


@router.get(
    path="/products",
    response_model=PageResponse,
    status_code=status.HTTP_200_OK
)
def get_products(
                 name: str = Query("example product", description="Name"),
                 category: str = Query(None, description="Category"),
                 color: str = Query(None, description="Color"),
                 from_price: Decimal = Query(None, description="Price"),
                 to_price: Decimal = Query(None, description="Price"),
                 brand: str = Query(None, description="Brand"),
                 page: int = Query(1, description="Page"),
                 size: int = Query(10, description="Size in a page"),
                 sort_direction: Sort.Direction = Query(None)) -> PageResponse:
    products = ProductService().get_products_service(
                                                     name=name,
                                                     category=category,
                                                     color=color,
                                                     brand=brand,
                                                     page=page,
                                                     size=size,
                                                     from_price=from_price,
                                                     to_price=to_price,
                                                     sort_direction=sort_direction)
    return PageResponse(data=products.data,
                        total_page=products.total_page,
                        total_items=products.total_items,
                        current_page=products.current_page)


@router.get(
    path="/{product_id}",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def get_product_id(product_id: int) -> DataResponse:
    product = ProductService().get_product_id_service(product_id=product_id)
    return DataResponse(data=product)


@router.delete(
    path="/product",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_product(product_id: int):
    product = ProductService().delete_product_service(product_id=product_id)
    return product



@router.post(
    path="/file/"
)
async def create_upload_file(file: UploadFile):
    product = ProductService().create_upload_file_service(file=file)
    try:
        os.mkdir("../files")
    except Exception as e:
        print(e)
    file_name = os.getcwd() + "/files/" + file.filename.replace(" ", "-")
    with open(file_name, 'wb+') as f:
        f.write(file.file.read())
        f.close()
    return {'file_name': file.filename}

