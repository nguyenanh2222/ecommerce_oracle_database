from fastapi import HTTPException
from starlette import status
from repo.cart import CartItemRepo
from repo.product import ProductRepo
from repo.sku import SkuRepo
from schema import CartItemReq


class CartItemService(CartItemRepo):
    def insert_cart_item_service(self,
                                 cart_item: CartItemReq):
        sku = SkuRepo().get_sku_by_id_repo(cart_item.sku_id)
        if sku  == None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        product = ProductRepo().get_product_id(sku['Sku'].product_id)
        cart_item = CartItemRepo().insert_cart_item_repo(CartItemReq(
            created_at=cart_item.created_at,
            created_by=cart_item.created_by,
            updated_at=cart_item.updated_at,
            updated_by=cart_item.updated_by,
            sku_id=cart_item.sku_id,
            main_image=cart_item.main_image,
            item_price=cart_item.item_price,
            username=cart_item.username),
            name=product['Product'].name + sku['Sku'].color + sku['Sku'].size_product)

        if sku['Sku'].quantity < 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        sub_quantity = sku['Sku'].quantity - 1
        sku_quantity = SkuRepo().update_sku_quantity_repo(quantity=sub_quantity, product_id=sku['Sku'].product_id)

        return cart_item

    def update_cart_item_service(self,
                                 cart_item: CartItemReq,
                                 id: int):
        sku = SkuRepo().get_sku_by_id_repo(cart_item.sku_id)
        product = ProductRepo().get_product_id(cart_item.sku_id)
        if sku == None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        is_cart_item = CartItemRepo().get_cart_item_by_id_repo(id=id)
        if is_cart_item == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        cart_item = CartItemRepo().update_cart_item_repo(
            cart_item=CartItemReq(
                created_at=cart_item.created_at,
                created_by=cart_item.created_by,
                updated_at=cart_item.updated_at,
                updated_by=cart_item.updated_by,
                sku_id=cart_item.sku_id,
                main_image=cart_item.main_image,
                item_price=cart_item.item_price,
                username=cart_item.username),
            name=product['Product'].name + sku['Sku'].color + sku['Sku'].size_product,
        id=id)
        return cart_item

    def get_cart_items_service(self, username: str):
        cart_items = CartItemRepo().get_cart_items_repo(username=username)
        return cart_items

    def get_cart_item_by_id_service(self, id: int):
        cart = CartItemRepo().get_cart_item_by_id_repo(id=id)
        return cart

    def delete_cart_item_service(self, id: int):
        cart = CartItemRepo().delete_cart_item_repo(id=id)
        return cart
