import json
from hashlib import sha256

from fastapi import FastAPI
from loguru import logger
from sqlalchemy import create_engine, insert, func, text

from database import engine, username, password, host, port, database
from model import *
from router.base import router as router_user
from router.admin.product import router as router_admin_product
from router.admin.order import router as router_admin_order

app = FastAPI(
    debug=True
)
app.include_router(router_user)
app.include_router(router_admin_product)
app.include_router(router_admin_order)

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
        name='nguyen'
    ))
    engine.execute(insert(Product).values(
        name="example product",
        category_id=1
    ))
    engine.execute(insert(Sku).values(
        product_id=1,
        images=json.dumps([{"name": "bbi0.jpg"}])
    ))
    # engine.execute(insert(Permission).values(code='001',
    #                                          name='EDIT'))
    # engine.execute(insert(RolePermission).values(
    #     permission_code='EDIT',
    #     role_code='001'))
    # engine.execute(insert(Role).values(code='001',
    #                                    name='ADMIN'))
    # engine.execute(insert(UserRole).values(username='vietanh',
    #                                        role_code='001'))
    # engine.execute(insert(User).values(username='vietanh',
    #                                    password=sha256(
    #                                        "12345678".encode('utf-8')).hexdigest(),
    #                                    firstname='anh',
    #                                    lastname='nguyen'
    #                                    ))
    # engine.execute(insert(CarItem).values())


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
