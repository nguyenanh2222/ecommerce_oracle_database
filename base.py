from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, BLOB, MetaData, Table, String
from sqlalchemy.dialects.oracle import VARCHAR2, NUMBER
from sqlalchemy.orm import as_declarative, declared_attr, declarative_base

# 1 -------------------
# from database import engine
# Base = declarative_base()
# Base.metadata.create_all(engine)
# 2 ---------------------
from database import engine


@as_declarative()
class Base:
    __name__: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def __str__(self):
        return str(self.__dict__)


class BaseUtil(Base):
    __abstract__ = True

    created_at = Column("CREATED_AT", DateTime, server_default=func.now())

    created_by = Column("CREATED_BY", VARCHAR2(20), default=None)

    updated_at = Column("UPDATED_AT", DateTime, server_default=func.now())

    updated_by = Column("UPDATED_BY", VARCHAR2(20), default=None)


class Permission(Base):
    __tablename__ = "permission"

    code = Column(VARCHAR2(50), primary_key=True)
    name = Column(VARCHAR2(100))


class RolePermission(Base):
    __tablename__ = "role_permission"
    permission_code = Column(VARCHAR2(50), ForeignKey("permission.code"), primary_key=True)
    role_code = Column(VARCHAR2(50), ForeignKey("role.code"), primary_key=True)


class Role(Base):
    __tablename__ = "role"
    code = Column(VARCHAR2(50), primary_key=True)
    name = Column(VARCHAR2(100))


class UserRole(Base):
    __tablename__ = "user_role"
    username = Column(VARCHAR2(100), ForeignKey("user.username"), primary_key=True)
    role_code = Column(VARCHAR2(50), ForeignKey("role.code"), primary_key=True)


class User(BaseUtil):
    __tablename__ = "user"
    username = Column(VARCHAR2(100), primary_key=True)
    password = Column(VARCHAR2(200))
    firstname = Column(VARCHAR2(200))
    lastname = Column(VARCHAR2(200))


class Customer(BaseUtil):
    __tablename__ = "customer"
    username = Column(VARCHAR2(100), primary_key=True)
    password = Column(VARCHAR2(200))
    firstname = Column(VARCHAR2(200))
    lastname = Column(VARCHAR2(200))
    phone = Column(VARCHAR2(200))
    address = Column(VARCHAR2(100))
    province_code = Column(VARCHAR2(50))
    district_code = Column(VARCHAR2(50))
    ward_code = Column(VARCHAR2(50))


class CarItem(BaseUtil):
    __tablename__ = "cart_item"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    sku_id = Column(Integer)
    name = Column(VARCHAR2(200))
    main_image = Column(VARCHAR2(200))
    item_price = Column(NUMBER(22, 2))


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR2(200))


class Product(BaseUtil):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR2(200))
    description = Column(VARCHAR2(4000))
    branch = Column(VARCHAR2(200))
    category_id = Column(Integer, ForeignKey("category.id"))


class Sku(BaseUtil):
    __tablename__ = "sku"
    id = Column(Integer, primary_key=True)
    status = Column(VARCHAR2(100))
    quantity = Column(Integer)
    images = Column(BLOB)
    seller_sku = Column(VARCHAR2(200))
    color = Column(VARCHAR2(200))
    package_width = Column(Integer)
    package_height = Column(Integer)
    package_length = Column(Integer)
    package_weight = Column(Integer)
    price = Column(NUMBER(22, 2))
    product_id = Column(Integer, ForeignKey("product.id"))


class Order(BaseUtil):
    __tablename__ = "tbl_order"
    id = Column(Integer, primary_key=True)
    customer_name = Column(VARCHAR2(200))
    price = Column(NUMBER(22, 2))
    shipping_fee_original = Column(NUMBER(22, 2))
    payment_method = Column(VARCHAR2(100))
    shipping_fee_discount = Column(NUMBER(22, 2))
    items_count = Column(Integer)
    name_shipping = Column(VARCHAR2(200))
    phone_shipping = Column(VARCHAR2(20))
    address_shipping = Column(VARCHAR2(200))
    province_code_shipping = Column(VARCHAR2(50))
    district_code_shipping = Column(VARCHAR2(50))
    ward_code_shipping = Column(VARCHAR2(50))
    customer_username = Column(VARCHAR2(100), ForeignKey("customer.username"))


class OrderItem(BaseUtil):
    __tablename__ = "order_item"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("tbl_order.id"))
    sku_id = Column(Integer, ForeignKey("sku.id"))
    name = Column(VARCHAR2(200))
    main_image = Column(VARCHAR2(200))
    item_price = Column(NUMBER(22, 2))
    paid_price = Column(NUMBER(22, 2))
    shipping_fee = Column(NUMBER(22, 2))



metadata_obj = Base.metadata
metadata_obj.bind = engine
metadata_obj.create_all()
