
from datetime import datetime
from starlette import status
from fastapi import APIRouter, Query
from project.schemas import DataResponse
from schema import ProductRes, ProductReq
from service.admin.product import ProductService

router = APIRouter()


@router.post(
    path='/product',
    response_model=DataResponse[ProductRes],
    status_code=status.HTTP_201_CREATED
)
def insert_product_router(product: ProductReq):
    product = ProductService().insert_product_service(ProductReq(
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
    return DataResponse(data=product)


@router.put(
    path='/product',
    response_model=DataResponse[ProductRes],
    status_code=status.HTTP_200_OK
)
def update_product_router(product: ProductReq, product_id: int):
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
    path="products",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def get_products_service(created_at: datetime = Query(datetime.now(), description="Create at"),
                         created_by: str = Query(None, description="Create by"),
                         updated_at: datetime = Query(datetime.now(), description="Update at"),
                         updated_by: str = Query(None, description="Update by"),
                         name: str = Query(None, description="Name"),
                         category: str = Query(None, description="Category"),
                         color: str = Query(None, description="Color"),
                         price: int = Query(None, description="Price"),
                         brand: str = Query(None, description="Brand"),
                         page: int = Query(1, description="Page"),
                         size: int = Query(10, description="Size in a page"),
                         ) -> DataResponse:
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
                                                     price=price)
    return DataResponse(data=products)
