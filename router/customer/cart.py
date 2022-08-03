from fast_boot.schemas import DataResponse
from fastapi import APIRouter, Body
from starlette import status
from starlette.responses import Response

from router.examples.cart import cart_opt1
from schema import CartItemReq
from service.customer.cart import CartItemService

router = APIRouter()


@router.post(
    path="/",
    response_model=DataResponse[CartItemReq],
    status_code=status.HTTP_201_CREATED
)
def insert_cart_item(cart_item: CartItemReq = Body(..., example=cart_opt1)) -> DataResponse:
    cart_item = CartItemService().insert_cart_item_service(CartItemReq(
        created_at=cart_item.created_at,
        created_by=cart_item.created_by,
        updated_at=cart_item.updated_at,
        updated_by=cart_item.updated_by,
        sku_id=cart_item.sku_id,
        main_image=cart_item.main_image,
        item_price=cart_item.item_price,
        username=cart_item.username))
    return DataResponse(data=cart_item)


@router.put(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=DataResponse
)
def update_cart_item(id: int, cart_item: CartItemReq = Body(..., example=cart_opt1)) -> DataResponse:
    cart_item = CartItemService().update_cart_item_service(
        cart_item=CartItemReq(
            created_at=cart_item.created_at,
            created_by=cart_item.created_by,
            updated_at=cart_item.updated_at,
            updated_by=cart_item.updated_by,
            sku_id=cart_item.sku_id,
            main_image=cart_item.main_image,
            item_price=cart_item.item_price,
            username=cart_item.username), id=id)
    return DataResponse(data=cart_item)


@router.get(
    path="/",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def get_cart_items(username: str) -> DataResponse:
    cart_items = CartItemService().get_cart_items_service(username=username)
    return DataResponse(data=cart_items)


@router.get(
    path="/{id}",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def get_cart_item_by_id(id: int) -> DataResponse:
    cart_item = CartItemService().get_cart_item_by_id_service(id=id)
    return DataResponse(data=cart_item)


@router.delete(
    path="/",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_cart_item(id: int):
    cart = CartItemService().delete_cart_item_service(id=id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
