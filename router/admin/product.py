from decimal import Decimal
from starlette import status
from fastapi import APIRouter, Query, Body
from starlette.responses import Response

from project.schemas import DataResponse, Sort, PageResponse
from router.examples.product import product_op1
from schema import ProductReq, SkuReq
from service.admin.product import ProductServiceAd

router = APIRouter()


@router.post(
    path='/',
    response_model=DataResponse,
    status_code=status.HTTP_201_CREATED
)
def insert_product(product: ProductReq = Body(..., examples=product_op1)):
    product = ProductServiceAd().insert_product_service(ProductReq(
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
                     package_weight=product.skus[0].package_width * product.skus[0].package_height * product.skus[
                         0].package_length,
                     )]))
    return DataResponse(data=product['Product'])


@router.put(
    path='/{id}',
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def update_product(product_id: int, product: ProductReq = Body(..., examples=product_op1)):
    product = ProductServiceAd().update_product_service(product_id=product_id,
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
                                                                         )]))
    return DataResponse(data=product['Product'])


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
        page: int = Query(1, gt=0, description="Page"),
        size: int = Query(100, gt=0, description="Size in a page"),
        sort_direction: Sort.Direction = Query(None)
) -> PageResponse:
    products = ProductServiceAd().get_products_service(
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
    product = ProductServiceAd().get_product_id_service(product_id=product_id)
    return DataResponse(data=product['Product'])


@router.delete(
    path="/",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_product(product_id: int):
    _product = ProductServiceAd().delete_product_service(product_id=product_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
