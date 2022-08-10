import datetime
from datetime import date
from decimal import Decimal
from itertools import product

from sqlalchemy.orm import Session
from starlette import status

from test.client import client
from test.executor.admin import AdminAPIExecutor


class TestSimpleCaseAdmin:
    executor_admin = AdminAPIExecutor()

    def test_admin_get_products(self):
        self.executor_admin.test_admin_get_products(
                                                    brand="no",
                                                    page=1,
                                                    size=2,
                                                    sort_direction="asc"
                                                    )
        self.executor_admin.test_admin_get_products(
            from_price=Decimal(0),
            to_price=Decimal(200000),
            brand="no",
            page=1,
            size=2,
            sort_direction="asc"
        )
        self.executor_admin.test_admin_get_products(
            size=2,
            sort_direction="desc"
        )
        self.executor_admin.test_admin_get_products()
        self.executor_admin.test_admin_get_products(
            brand="NO",
            page=1,
            size=2,
            sort_direction="asc"
        )
    def test_admin_insert_product(self):
        ...

    def test_admin_delete_product(self):
        ...

    def test_admin_get_product_by_id(self):
        ...

    def test_admin_update_product(self):
        ...

    def test_admin_get_orders(self):
        ...

    def test_admin_get_order_by_id(self):
        ...

    def test_admin_create_upload_file(self):
        ...
