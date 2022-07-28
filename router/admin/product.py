from starlette import status

from project.schemas import DataResponse
from router.base import router
from schema import ProductRes, ProductReq
from service.admin.product import ProductService


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
