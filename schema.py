import datetime
import decimal
from decimal import Decimal
from datetime import date

from pydantic import BaseModel, Field


class BaseUtil(BaseModel):
    created_at: datetime = Field(None, default=datetime.datetime.now())

    created_by: str = Field(None, default=datetime.datetime.now())

    updated_at: date = Field(None, default=datetime.datetime.now())

    updated_by: str = Field(None, default=datetime.datetime.now())


class PermissionReq(BaseModel):
    code: str = Field(..., gt=50)
    name: str = Field(..., gt=100)


class PermissionRes(BaseModel):
    code: str = Field(None, gt=50)
    name: str = Field(None, gt=100)


class RolePermissionReq(BaseModel):
    permission_code: str = Field(..., gt=50)
    role_code: str = Field(..., gt=50)


class RolePermissionRes(BaseModel):
    permission_code: str = Field(None, gt=50)
    role_code: str = Field(None, gt=50)


class RoleReq(BaseModel):
    code: str = Field(..., gt=50)
    name: str = Field(..., gt=50)


class RoleRes(BaseModel):
    code: str = Field(None, gt=50)
    name: str = Field(None, gt=50)


class UserRoleReq(BaseModel):
    username: str = Field(..., gt=100)
    role_code: str = Field(..., gt=50)


class UserRoleRes(BaseModel):
    username: str = Field(None, gt=100)
    role_code: str = Field(None, gt=50)


class UserReq(BaseUtil):
    username: str = Field(..., gt=100)
    password: str = Field(..., gt=200)
    firstname: str = Field(..., gt=200)
    lastname: str = Field(..., gt=200)


class UserRes(BaseUtil):
    username: str = Field(None, gt=100)
    password: str = Field(None, gt=200)
    firstname: str = Field(None, gt=200)
    lastname: str = Field(None, gt=200)


class CustomerReq(BaseUtil):
    username: str = Field(..., gt=100)
    password: str = Field(..., gt=200)
    firstname: str = Field(..., gt=200)
    lastname: str = Field(..., gt=200)
    phone: str = Field(..., gt=200)
    address: str = Field(..., gt=100)
    province_code: str = Field(..., gt=50)
    district_code: str = Field(..., gt=50)
    ward_code: str = Field(..., gt=50)


class CustomerRes(BaseUtil):
    username: str = Field(None, gt=100)
    password: str = Field(None, gt=200)
    firstname: str = Field(None, gt=200)
    lastname: str = Field(None, gt=200)
    phone: str = Field(None, gt=200)
    address: str = Field(None, gt=100)
    province_code: str = Field(None, gt=50)
    district_code: str = Field(None, gt=50)
    ward_code: str = Field(None, gt=50)


class CarItemReq(BaseUtil):
    id: int = Field(...)
    order_id: int = Field(...)
    sku_id: int = Field(...)
    name: str = Field(..., gt=50)
    main_image: str = Field(..., gt=50)
    item_price: decimal = Field(..., gt=0)


class CarItemRes(BaseUtil):
    id: int = Field(None)
    order_id: int = Field(None)
    sku_id: int = Field(None)
    name: str = Field(None, gt=50)
    main_image: str = Field(None, gt=50)
    item_price: decimal = Field(None, gt=0)


class CategoryReq(BaseModel):
    id: int = Field(...)
    name: str = Field(..., gt=200)


class CategoryRes(BaseModel):
    id: int = Field(None)
    name: str = Field(None, gt=200)


class ProductReq(BaseUtil):
    id: int = Field(...)
    name: str = Field(..., gt=200)
    description: str = Field(..., gt=4000)
    branch: str = Field(..., gt=200)
    category_id: int = Field(...)


class ProductRes(BaseUtil):
    id: int = Field(None)
    name: str = Field(None, gt=200)
    description: str = Field(None, gt=4000)
    branch: str = Field(None, gt=200)
    category_id: int = Field(None)


class SkuReq(BaseUtil):
    id: int = Field(...)
    status: str = Field(..., gt=200)
    quantity: int = Field(...)
    images: bytes = Field(...)
    seller_sku: str = Field(..., gt=200)
    color: str = Field(..., gt=200)
    package_width: int = Field(...)
    package_height: int = Field(...)
    package_length: int = Field(...)
    package_weight: int = Field(...)
    price: Decimal = Field(...)
    product_id: int = Field(...)


class SkuRes(BaseUtil):
    id: int = Field(None)
    status: str = Field(None, gt=200)
    quantity: int = Field(None)
    images: bytes = Field(None)
    seller_sku: str = Field(None, gt=200)
    color: str = Field(None, gt=200)
    package_width: int = Field(None)
    package_height: int = Field(None)
    package_length: int = Field(None)
    package_weight: int = Field(None)
    price: Decimal = Field(None)
    product_id: int = Field(None)


class OrderReq(BaseUtil):
    id: int = Field(...)
    customer_name: str = Field(...)
    price: decimal = Field(...)
    shipping_fee_original: decimal = Field(...)
    payment_method: str = Field(..., gt=100)
    shipping_fee_discount: decimal = Field(...)
    items_count: int = Field(...)
    name_shipping: str = Field(..., gt=200)
    phone_shipping: str = Field(..., gt=20)
    address_shipping: str = Field(..., gt=200)
    province_code_shipping: str = Field(..., gt=50)
    district_code_shipping: str = Field(..., gt=50)
    ward_code_shipping: str = Field(..., gt=50)
    customer_username: str = Field(..., gt=100)


class OrderRes(BaseUtil):
    id: int = Field(None)
    customer_name: str = Field(None)
    price: decimal = Field(None)
    shipping_fee_original: decimal = Field(None)
    payment_method: str = Field(None, gt=100)
    shipping_fee_discount: decimal = Field(None)
    items_count: int = Field(None)
    name_shipping: str = Field(None, gt=200)
    phone_shipping: str = Field(None, gt=20)
    address_shipping: str = Field(None, gt=200)
    province_code_shipping: str = Field(None, gt=50)
    district_code_shipping: str = Field(None, gt=50)
    ward_code_shipping: str = Field(None, gt=50)
    customer_username: str = Field(None, gt=100)


class OrderItemReq(BaseUtil):
    id: int = Field(...)
    order_id: int = Field(...)
    sku_id: int = Field(...)
    name: str = Field(..., gt=200)
    main_image: str = Field(..., gt=200)
    item_price: decimal = Field(...)
    paid_price: decimal = Field(...)
    shipping_fee: decimal = Field(...)


class OrderItemRes(BaseUtil):
    id: int = Field(None)
    order_id: int = Field(None)
    sku_id: int = Field(None)
    name: str = Field(None, gt=200)
    main_image: str = Field(None, gt=200)
    item_price: decimal = Field(None)
    paid_price: decimal = Field(None)
    shipping_fee: decimal = Field(None)
