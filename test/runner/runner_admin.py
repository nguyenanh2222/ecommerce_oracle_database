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
        self.executor_admin.test_admin_get_products(
            brand="NO",
            page=1,
            size=2,
        )

    def test_admin_insert_product(self):
        self.executor_admin.test_admin_insert_product_successful(
            {
                "created_at": "2022-08-01T02:36:00.817Z",
                "created_by": "admin",
                "updated_at": "2022-08-01T02:36:00.817Z",
                "updated_by": "admin",
                "name": "AZ123",
                "description": "summer",
                "brand": "no brand",
                "category_id": 1,
                "skus": [
                    {
                        "status": "COMPLETED",
                        "quantity": 1,
                        "images": "abc",
                        "seller_sku": "123456",
                        "color": "black",
                        "package_width": 15,
                        "package_height": 15,
                        "package_length": 15,
                        "price": 156000,
                        "size_product": "150"
                    }
                ]
            }
        )

        self.executor_admin.test_admin_insert_product_validation_error(
            {
                "created_at": "2022-08-01T02:36:00.817Z",
                "created_by": "admin",
                "updated_at": "2022-08-01T02:36:00.817Z",
                "updated_by": "admin",
                "name": "AZ123",
                "description": "summer",
                "brand": "no brand",
                "category_id": 2,
                "skus": [
                    {
                        "status": "COMPLETED",
                        "quantity": 1,
                        "images": "abc",
                        "seller_sku": "123456",
                        "color": "black",
                        "package_width": 15,
                        "package_height": 15,
                        "package_length": 15,
                        "price": 156000,
                        "size_product": "150"
                    }
                ]
            }
        )

        self.executor_admin.test_admin_insert_product_validation_missing(
            {
                "created_by": "admin",
                "updated_at": "2022-08-01T02:36:00.817Z",
                "updated_by": "admin",
                "name": "AZ123",
                "description": "summer",
                "brand": "no brand",
                "skus": [
                    {
                        "status": "COMPLETED",
                        "quantity": 1,
                        "images": "abc",
                        "seller_sku": "123456",
                        "color": "black",
                        "package_width": 15,
                        "package_height": 15,
                        "package_length": 15,
                        "price": 156000,
                        "size_product": "150"
                    }
                ]
            }
        )

    def test_admin_delete_product(self):
        self.executor_admin.test_admin_delete_product_successful(1)
        self.executor_admin.test_admin_delete_product_not_found_id(100)

    def test_admin_get_product_by_id(self):
        self.executor_admin.test_admin_get_product_by_id_successful(1)
        self.executor_admin.test_admin_get_product_not_found_id(100)

    def test_admin_update_product(self):
        self.executor_admin.test_admin_update_product_by_id_successful(1,
                                                                       {
                                                                           "created_at": "2022-08-01T02:36:00.817Z",
                                                                           "created_by": "admin",
                                                                           "updated_at": "2022-08-01T02:36:00.817Z",
                                                                           "updated_by": "admin",
                                                                           "name": "AZ123",
                                                                           "description": "summer",
                                                                           "brand": "no brand",
                                                                           "category_id": 1,
                                                                           "skus": [
                                                                               {
                                                                                   "status": "COMPLETED",
                                                                                   "quantity": 1,
                                                                                   "images": "abc",
                                                                                   "seller_sku": "123456",
                                                                                   "color": "black",
                                                                                   "package_width": 15,
                                                                                   "package_height": 15,
                                                                                   "package_length": 15,
                                                                                   "price": 156000,
                                                                                   "size_product": "150"
                                                                               }
                                                                           ]
                                                                       })
        self.executor_admin.test_admin_update_product_not_found_id(100,
                                                                   {"created_at": "2022-08-01T02:36:00.817Z",
                                                                    "created_by": "admin",
                                                                    "updated_at": "2022-08-01T02:36:00.817Z",
                                                                    "updated_by": "admin",
                                                                    "name": "AZ123",
                                                                    "description": "summer",
                                                                    "brand": "no brand",
                                                                    "category_id": 1,
                                                                    "skus": [
                                                                        {
                                                                            "status": "COMPLETED",
                                                                            "quantity": 1,
                                                                            "images": "abc",
                                                                            "seller_sku": "123456",
                                                                            "color": "black",
                                                                            "package_width": 15,
                                                                            "package_height": 15,
                                                                            "package_length": 15,
                                                                            "price": 156000,
                                                                            "size_product": "150"}]})
        self.executor_admin.test_admin_update_product_validation_missing(
            1,
            {"created_at": "2022-08-01T02:36:00.817Z",
             "created_by": "admin",
             "updated_at": "2022-08-01T02:36:00.817Z",
             "updated_by": "admin",
             "name": "AZ123",
             "description": "summer",
             "brand": "no brand",
             "skus": [
                 {
                     "status": "COMPLETED",
                     "quantity": 1,
                     "images": "abc",
                     "seller_sku": "123456",
                     "color": "black",
                     "package_width": 15,
                     "package_height": 15,
                     "package_length": 15,
                     "price": 156000,
                     "size_product": "150"}]}
        )

    def test_admin_get_orders(self):
        self.executor_admin.test_admin_get_orders(
            customer_name='vietanh',
            id=1)
        self.executor_admin.test_admin_get_orders(
            customer_name='vietanh',
            sort_direction='asc',
            page=1,
            size=10)

    def test_admin_get_order_by_id(self):
        self.executor_admin.test_admin_get_order_by_id_successful(1)
        # self.executor_admin.test_admin_get_order_not_found_id(100)

    def test_admin_create_upload_file(self):
        ...
