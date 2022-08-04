from datetime import datetime
from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class BaseUtil(BaseModel):
    created_at: datetime = Field(default_factory=datetime.utcnow)
    created_by: str = Field(None)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    updated_by: str = Field(None)

    class Config:
        orm_mode = True


class BaseUtilRes(BaseModel):
    created_at: datetime = Field(None)
    created_by: str = Field(None)
    updated_at: datetime = Field(None)
    updated_by: str = Field(None)


class PermissionReq(BaseModel):
    code: str = Field(...)
    name: str = Field(...)


class PermissionRes(BaseModel):
    # code: str = Field(None)
    name: str = Field(None)


class RolePermissionReq(BaseModel):
    permission_code: str = Field(...)
    role_code: str = Field(...)


class RolePermissionRes(BaseModel):
    permission_code: str = Field(None)
    role_code: str = Field(None)


class RoleReq(BaseModel):
    code: str = Field(...)
    name: str = Field(...)


class RoleRes(BaseModel):
    # code: str = Field(None)
    name: str = Field(None)


class UserRoleReq(BaseModel):
    username: str = Field(...)
    role_code: str = Field(...)


class UserRoleRes(BaseModel):
    username: str = Field(None)
    role_code: str = Field(None)


class UserReq(BaseUtil):
    username: str = Field(None, autoincrement=True, nullable=True)
    password: str = Field(...)
    firstname: str = Field(...)
    lastname: str = Field(...)


class UserRes(BaseUtilRes):
    username: str = Field(None, autoincrement=True, nullable=True)
    password: str = Field(None)
    firstname: str = Field(None)
    lastname: str = Field(None)
    role_name: str = Field(None)


class CustomerReq(BaseUtil):
    phone: str = Field(...)
    address: str = Field(...)
    province_code: str = Field(...)
    district_code: str = Field(...)
    ward_code: str = Field(...)
    username: str = Field(...)
    # user: UserReq = Field(...)


class CustomerRes(BaseModel):
    username: str = Field(None)
    password: str = Field(None)
    firstname: str = Field(None)
    lastname: str = Field(None)
    phone: str = Field(None)
    address: str = Field(None)
    province_code: str = Field(None)
    district_code: str = Field(None)
    ward_code: str = Field(None)


class CartItemReq(BaseUtil):
    # id: int = Field(...)
    sku_id: int = Field(...)
    # name: str = Field(...)
    main_image: str = Field(...)
    item_price: Decimal = Field(...)
    username: str = Field(...)


class CartItemRes(BaseUtil):
    id: int = Field(None)
    order_id: int = Field(None)
    sku_id: int = Field(None)
    name: str = Field(None)
    main_image: str = Field(None)
    item_price: Decimal = Field(None)


class CategoryReq(BaseModel):
    id: int = Field(...)
    name: str = Field(...)


class CategoryRes(BaseModel):
    name: str = Field(None)


class SkuReq(BaseModel):
    status: str = Field(...)
    quantity: int = Field(...)
    images: bytes = Field(...)
    seller_sku: str = Field(...)
    color: str = Field(...)
    package_width: int = Field(...)
    package_height: int = Field(...)
    package_length: int = Field(...)
    price: Decimal = Field(...)
    size_product: str = Field(...)


class ProductReq(BaseUtil):
    name: str = Field(...)
    description: str = Field(...)
    brand: str = Field(default_factory="No Brand")
    category_id: int = Field(...)
    skus: List[SkuReq] = Field(...)


class ProductRes(BaseModel):
    name: str = Field(None)
    description: str = Field(None)
    brand: str = Field("No Brand")
    category: List[CategoryRes] = Field(None)
    quantity: int = Field(None)
    images: bytes = Field(None)
    color: str = Field(None)
    price: Decimal = Field(None)
    size_product: str = Field(None)


class SkuRes(BaseUtil):
    status: str = Field(None)
    quantity: int = Field(None)
    images: bytes = Field(None)
    seller_sku: str = Field(None)
    color: str = Field(None)
    package_width: int = Field(None)
    package_height: int = Field(None)
    package_length: int = Field(None)
    package_weight: int = Field(None)
    price: Decimal = Field(None)
    product_id: int = Field(None)
    size: str = Field(None)


class OrderItemReq(BaseUtil):
    shipping_fee: Decimal = Field(...)
    item_discount: Decimal = Field(...)
    sku_id: int = Field(...)
    name: str = Field(...)
    main_image: bytes = Field(...)
    item_price: Decimal = Field(...)
    paid_price: Decimal = Field(...)


class OrderReq(BaseUtil):
    payment_method: str = Field(...)
    shipping_fee_discount: Decimal = Field(...)
    discount: Decimal = Field(...)
    name_shipping: str = Field(...)
    customer_username: str = Field(...)



class OrderRes(BaseUtil):
    id: int = Field(None)
    customer_name: str = Field(None)
    price: Decimal = Field(None)
    shipping_fee_original: Decimal = Field(None)
    payment_method: str = Field(None)
    shipping_fee_discount: Decimal = Field(None)
    items_count: int = Field(None)
    name_shipping: str = Field(None)
    phone_shipping: str = Field(None)
    address_shipping: str = Field(None)
    province_code_shipping: str = Field(None)
    district_code_shipping: str = Field(None)
    ward_code_shipping: str = Field(None)
    customer_username: str = Field(None)


class OrderItemRes(BaseUtil):
    id: int = Field(None)
    order_id: int = Field(None)
    sku_id: int = Field(None)
    name: str = Field(None)
    main_image: str = Field(None)
    item_price: Decimal = Field(None)
    paid_price: Decimal = Field(None)
    shipping_fee: Decimal = Field(None)
