from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class BaseUtil(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)

    created_by: str = Field(...)

    updated_at: datetime = Field(default_factory=datetime.now)

    updated_by: str = Field(...)

    class Config:
        orm_mode = True


class PermissionReq(BaseModel):
    code: str = Field(...)
    name: str = Field(...)

    class Config:
        orm_mode = True


class PermissionRes(BaseModel):
    code: str = Field(None)
    name: str = Field(None)

    class Config:
        orm_mode = True


class RolePermissionReq(BaseModel):
    permission_code: str = Field(...)
    role_code: str = Field(...)

    class Config:
        orm_mode = True


class RolePermissionRes(BaseModel):
    permission_code: str = Field(None)
    role_code: str = Field(None)

    class Config:
        orm_mode = True


class RoleReq(BaseModel):
    code: str = Field(...)
    name: str = Field(...)

    class Config:
        orm_mode = True


class RoleRes(BaseModel):
    code: str = Field(None)
    name: str = Field(None)

    class Config:
        orm_mode = True


class UserRoleReq(BaseModel):
    username: str = Field(...)
    role_code: str = Field(...)

    class Config:
        orm_mode = True


class UserRoleRes(BaseModel):
    username: str = Field(None)
    role_code: str = Field(None)

    class Config:
        orm_mode = True


class UserReq(BaseUtil):
    username: str = Field(..., autoincrement=True, nullable=True)
    password: str = Field(...)
    firstname: str = Field(...)
    lastname: str = Field(...)

    class Config:
        orm_mode = True


class UserRes(BaseUtil):
    username: str = Field(None,  autoincrement=True, nullable=True)
    password: str = Field(None)
    firstname: str = Field(None)
    lastname: str = Field(None)

    class Config:
        orm_mode = True



class CustomerReq(BaseUtil):
    username: str = Field(...)
    password: str = Field(...)
    firstname: str = Field(...)
    lastname: str = Field(...)
    phone: str = Field(...)
    address: str = Field(...)
    province_code: str = Field(...)
    district_code: str = Field(...)
    ward_code: str = Field(...)

    class Config:
        orm_mode = True


class CustomerRes(BaseUtil):
    username: str = Field(None)
    password: str = Field(None)
    firstname: str = Field(None)
    lastname: str = Field(None)
    phone: str = Field(None)
    address: str = Field(None)
    province_code: str = Field(None)
    district_code: str = Field(None)
    ward_code: str = Field(None)

    class Config:
        orm_mode = True


class CarItemReq(BaseUtil):
    id: int = Field(...)
    order_id: int = Field(...)
    sku_id: int = Field(...)
    name: str = Field(...)
    main_image: str = Field(...)
    item_price: Decimal = Field(...)

    class Config:
        orm_mode = True


class CarItemRes(BaseUtil):
    id: int = Field(None)
    order_id: int = Field(None)
    sku_id: int = Field(None)
    name: str = Field(None)
    main_image: str = Field(None)
    item_price: Decimal = Field(None)

    class Config:
        orm_mode = True


class CategoryReq(BaseModel):
    id: int = Field(...)
    name: str = Field(...)

    class Config:
        orm_mode = True


class CategoryRes(BaseModel):
    id: int = Field(None)
    name: str = Field(None)

    class Config:
        orm_mode = True


class ProductReq(BaseUtil):
    id: int = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    branch: str = Field(...)
    category_id: int = Field(...)

    class Config:
        orm_mode = True


class ProductRes(BaseUtil):
    id: int = Field(None)
    name: str = Field(None)
    description: str = Field(None)
    branch: str = Field(None)
    category_id: int = Field(None)

    class Config:
        orm_mode = True


class SkuReq(BaseUtil):
    id: int = Field(...)
    status: str = Field(...)
    quantity: int = Field(...)
    images: bytes = Field(...)
    seller_sku: str = Field(...)
    color: str = Field(...)
    package_width: int = Field(...)
    package_height: int = Field(...)
    package_length: int = Field(...)
    package_weight: int = Field(...)
    price: Decimal = Field(...)
    product_id: int = Field(...)

    class Config:
        orm_mode = True


class SkuRes(BaseUtil):
    id: int = Field(None)
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

    class Config:
        orm_mode = True


class OrderReq(BaseUtil):
    id: int = Field(...)
    customer_name: str = Field(...)
    price: Decimal = Field(...)
    shipping_fee_original: Decimal = Field(...)
    payment_method: str = Field(...)
    shipping_fee_discount: Decimal = Field(...)
    items_count: int = Field(...)
    name_shipping: str = Field(...)
    phone_shipping: str = Field(...)
    address_shipping: str = Field(...)
    province_code_shipping: str = Field(...)
    district_code_shipping: str = Field(...)
    ward_code_shipping: str = Field(...)
    customer_username: str = Field(...)

    class Config:
        orm_mode = True


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

    class Config:
        orm_mode = True


class OrderItemReq(BaseUtil):
    id: int = Field(...)
    order_id: int = Field(...)
    sku_id: int = Field(...)
    name: str = Field(...)
    main_image: str = Field(...)
    item_price: Decimal = Field(...)
    paid_price: Decimal = Field(...)
    shipping_fee: Decimal = Field(...)

    class Config:
        orm_mode = True


class OrderItemRes(BaseUtil):
    id: int = Field(None)
    order_id: int = Field(None)
    sku_id: int = Field(None)
    name: str = Field(None)
    main_image: str = Field(None)
    item_price: Decimal = Field(None)
    paid_price: Decimal = Field(None)
    shipping_fee: Decimal = Field(None)

    class Config:
        orm_mode = True
