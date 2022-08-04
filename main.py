import json
from enum import Enum
from hashlib import sha256
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from loguru import logger
from sqlalchemy import create_engine, insert
from starlette.middleware.cors import CORSMiddleware
from database import username, password, host, port, database
from model import *
from status import EOrderStatus

from router.permisstion.user import router as router_user
from router.admin.product import router as router_admin_product
from router.admin.order import router as router_admin_order
from router.admin.file import router as router_admin_file

from router.customer.customer import router as router_customer
from router.customer.cart import router as router_customer_cart
from router.customer.order import router as router_customer_order
from router.customer.product import router as router_customer_product

app = FastAPI(
    title="ecommerce",
    description="ecommerce description",
    debug=True,
    version="0.0.3",
    docs_url="/",
    redoc_url="/redoc",
    default_response_class=ORJSONResponse,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["POST", "GET"],
)


class Tags(str, Enum):
    customer = "[Customer]"
    admin = "[Admin]"
    user = "[User]"


app.include_router(router_user, prefix="/users", tags=[Tags.user])

app.include_router(router_admin_product, prefix="/products", tags=[Tags.admin])
app.include_router(router_admin_order, prefix="/orders", tags=[Tags.admin])
app.include_router(router_admin_file, prefix="/files", tags=[Tags.admin])

app.include_router(router_customer, prefix="/customers", tags=[Tags.customer])
app.include_router(router_customer_cart, prefix="/customers/carts", tags=[Tags.customer])
app.include_router(router_customer_order, prefix="/customers/orders", tags=[Tags.customer])
app.include_router(router_customer_product, prefix="/customers/products", tags=[Tags.customer])

tables = ("ORDER_ITEM", "SKU", "PRODUCT", "CATEGORY", "TBL_ORDER", "CART_ITEM")


@app.on_event("startup")
async def startup():
    metadata = Base.metadata
    metadata.bind = engine
    metadata.drop_all(bind=engine)
    metadata.create_all(bind=engine)
    for tbl in tables:
        try:
            engine.execute(f"""DROP SEQUENCE {tbl}_SEQ""")
        except:
            ...
        engine.execute(f"""
    CREATE SEQUENCE {tbl}_SEQ START WITH 1
            """)
        engine.execute(f"""
    CREATE OR REPLACE TRIGGER {tbl}_INSERT
        BEFORE INSERT
        ON {tbl}
        FOR EACH ROW
    BEGIN
        SELECT {tbl}_SEQ.nextval
        INTO :new.ID
        FROM dual;
    END;
    """)

    engine.execute(insert(Customer).values(
        username="vietanh",
        password=sha256("12345678".encode('utf-8')).hexdigest(),
        firstname="Viet",
        lastname="Anh",
        phone="091234567",
        address="56 Nguyen Hue",
        province_code="	79",
        district_code="760",
        ward_code="26734",
    ))
    engine.execute(insert(Category).values(
        name='A'
    ))
    engine.execute(insert(Product).values(
        name="example product",
        category_id=1,
        brand="no brand"
    ))
    engine.execute(insert(Sku).values(
        product_id=1,
        images=json.dumps([{"name": "bbi0.jpg"}]),
        color='red',
        size_product='120*120',
        package_width=3,
        package_height=4,
        package_length=5,
        package_weight=60,
        quantity=100
    ))

    engine.execute(insert(User).values(username='vietanh',
                                       password=sha256(
                                           "12345678".encode('utf-8')).hexdigest(),
                                       firstname='anh',
                                       lastname='nguyen'
                                       ))
    engine.execute(insert(Role).values(code='001',
                                       name='ADMIN'))

    engine.execute(insert(UserRole).values(username='vietanh',
                                           role_code='001'))

    engine.execute(insert(Permission).values(code='00E',
                                             name='EDIT'))

    engine.execute(insert(RolePermission).values(
        permission_code='00E',
        role_code='001'))

    engine.execute(insert(CartItem).values(
        name="nguyen",
        username="vietanh",
        sku_id=1,
        item_price=200_000,
    ))
    engine.execute(insert(Order).values(status=EOrderStatus.CANCELLED,
                                        customer_name='vietanh'))
    engine.execute(insert(OrderItem).values(shipping_fee=15_000,
                                            created_by="admin",
                                            updated_by="admin",
                                            order_id=1,
                                            sku_id=1,
                                            item_price=300_000,
                                            name="product_name+sku_color+sku_size",
                                            main_image=json.dumps([{"name": "bbi0.jpg"}]
                                                                  )))


@app.on_event("shutdown")
async def teardown():
    engine1 = create_engine(f"oracle+cx_oracle://{username}:{password}@{host}:{port}/{database}")
    for tbl in tables:
        try:
            engine1.execute(f"""
            DROP SEQUENCE {tbl}_SEQ
            """)
        except:
            continue
    metadata = Base.metadata
    metadata.drop_all(bind=engine1)
    logger.info("APP TEAR DOWN COMPLETED")
