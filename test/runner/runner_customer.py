import random
import string
from decimal import Decimal
from typing import Dict

from test.executor.customer import CustomerAPIExecutor


class TestSimpleCaseCustomer:
    executor_customer = CustomerAPIExecutor()

    def test_customer_created_profile(self):
        self.executor_customer.test_customer_created_profile_successful(
            {
                "created_at": "2022-08-01 15:43:39.000",
                "created_by": "customer",
                "updated_at": "2022-08-01 15:43:39.000",
                "updated_by": "customer",
                "phone": "033578982",
                "address": "quan 8",
                "province_code": "01",
                "district_code": "001",
                "ward_code": "00001",
                "username": ''.join(random.choices(string.ascii_lowercase, k=5)),
                "password": "Anh123@",
                "firstname": "anh",
                "lastname": "viet"
            }
        )
        self.executor_customer.test_customer_created_profile_values_error(
            {
                "created_at": "2022-08-01 15:43:39.000",
                "created_by": "customer",
                "updated_at": "2022-08-01 15:43:39.000",
                "updated_by": "customer",
                "phone": "033578982",
                "address": "quan 8",
                "province_code": " 78",
                "district_code": "468",
                "ward_code": "234",
                "username": "nguyenanh123",
                "password": "Nguyenanh2103.",
                "firstname": "anh",
                "lastname": "viet"
            }
        )
        self.executor_customer.test_customer_created_profile_values_error(
            {
                "created_at": "2022-08-01 15:43:39.000",
                "created_by": "customer",
                "updated_at": "2022-08-01 15:43:39.000",
                "updated_by": "customer",
                "phone": "033578982",
                "address": "quan 8",
                "province_code": "999999999999999",
                "district_code": "468",
                "ward_code": "234",
                "username": "nguyenanh123",
                "password": "Nguyenanh2103.",
                "firstname": "anh",
                "lastname": "viet"
            }
        )

    def test_customer_get_profile_by_username(self):
        self.executor_customer.test_customer_get_profile_by_username_successful('vietanh')
        self.executor_customer.test_customer_get_profile_by_username_not_found('XYZ')

    def test_customer_update_profile(self):
        self.executor_customer.test_customer_update_profile_successful(
            {
                "created_at": "2022-08-01 15:43:39.000",
                "created_by": "customer",
                "updated_at": "2022-08-01 15:43:39.000",
                "updated_by": "customer",
                "phone": "033578982",
                "address": "quan 8",
                "province_code": "01",
                "district_code": "001",
                "ward_code": "00001",
                "username": "GM9BHW",
                "password": "Anh123@",
                "firstname": "anh",
                "lastname": "viet"
            }, 'vietanh'
        )
        self.executor_customer.test_customer_update_profile_not_found_username(
            {"created_at": "2022-08-01 15:43:39.000",
             "created_by": "customer",
             "updated_at": "2022-08-01 15:43:39.000",
             "updated_by": "customer",
             "phone": "033578982",
             "address": "quan 8",
             "province_code": "01",
             "district_code": "001",
             "ward_code": "00001",
             "username": "1VRNQ4",
             "password": "Annh123@",
             "firstname": "anh",
             "lastname": "viet"
             }, 'XYZ'
        )

        self.executor_customer.test_customer_update_profile_value_error(
            {"created_at": "2022-08-01 15:43:39.000",
             "created_by": "customer",
             "updated_at": "2022-08-01 15:43:39.000",
             "updated_by": "customer",
             "phone": "033578982",
             "address": "quan 8",
             "province_code": "0000000000000",
             "district_code": "468",
             "ward_code": "234",
             "username": "1VRNQ4",
             "password": "Annh123@",
             "firstname": "anh",
             "lastname": "viet"
             }, 'vietanh'
        )

        self.executor_customer.test_customer_update_profile_value_error(
            {
                "created_at": "2022-08-01 15:43:39.000",
                "created_by": "customer",
                "updated_at": "2022-08-01 15:43:39.000",
                "updated_by": "customer",
                "phone": "033578982",
                "address": "quan 8",
                "province_code": "01",
                "district_code": "001",
                "ward_code": "00001",
                "username": "1VRNQ4",
                "password": "123456",
                "firstname": "anh",
                "lastname": "viet"
            }, 'vietanh'
        )

    def test_customer_get_cart_items(self):
        self.executor_customer.test_customer_get_cart_items_successful('vietanh')
        self.executor_customer.test_customer_get_cart_items_not_found_username('XYZ')

    def test_customer_insert_cart_item(self):
        self.executor_customer.test_customer_insert_cart_item_successful(
            {
                "created_at": "2022-08-03T06:41:58.630Z",
                "created_by": "string",
                "updated_at": "2022-08-03T06:41:58.630Z",
                "updated_by": "string",
                "sku_id": 1,
                "main_image": "string",
                "item_price": 500000,
                "username": "vietanh"
            }
        )

        self.executor_customer.test_customer_insert_cart_item_value_missing(
            {
                "created_by": "string",
                "updated_at": "2022-08-03T06:41:58.630Z",
                "updated_by": "string",
                "sku_id": 1,
                "main_image": "string",
                "username": "vietanh"
            }
        )

    def test_customer_get_cart_item_by_id(self):
        self.executor_customer.test_customer_get_cart_item_by_id_successful(1)
        self.executor_customer.test_customer_get_cart_item_by_id_not_found(100)

    def test_customer_update_cart_item(self):
        self.executor_customer.test_customer_update_cart_item_successful(
            1,
            {
                "created_at": "2022-08-03T06:41:58.630Z",
                "created_by": "string",
                "updated_at": "2022-08-03T06:41:58.630Z",
                "updated_by": "string",
                "sku_id": 1,
                "main_image": "string",
                "item_price": 500000,
                "username": "vietanh"
            }
        )

        self.executor_customer.test_customer_update_cart_item_not_found(
            100,
            {
                "created_at": "2022-08-03T06:41:58.630Z",
                "created_by": "string",
                "updated_at": "2022-08-03T06:41:58.630Z",
                "updated_by": "string",
                "sku_id": 1,
                "main_image": "string",
                "item_price": 500000,
                "username": "vietanh"
            }
        )

        self.executor_customer.test_customer_update_cart_item_value_error(
            1,
            {
                "created_at": "2022-08-03T06:41:58.630Z",
                "created_by": "string",
                "updated_at": "2022-08-03T06:41:58.630Z",
                "updated_by": "string",
                "sku_id": 1,
                "main_image": "string",
                "item_price": -5000,
                "username": "vietanh"
            }
        )

    def test_customer_delete_cart_item(self):
        self.executor_customer.test_customer_delete_cart_item_successful(1)
        self.executor_customer.test_customer_delete_cart_item_not_found(100)

    def test_customer_get_orders(self):
        self.executor_customer.test_customer_get_orders(
            customer_name='vietanh',
            id=1)
        self.executor_customer.test_customer_get_orders(
            customer_name='vietanh',
            sort_direction='asc',
            page=1,
            size=10)
        self.executor_customer.test_customer_get_orders(
                                     customer_name="a",
                                     id=1,
                                     payment_method="cod",
                                     name_shipping="a",
                                     phone_shipping="1",
                                     address_shipping="a",
                                     province_code_shipping="01",
                                     ward_code_shipping="00001",
                                     district_code_shipping="0001",
                                     customer_username="a",
                                     from_price=Decimal(100000),
                                     to_price=Decimal(200000),
                                     page=1,
                                     size=10,
                                     sort_direction='asc')
        self.executor_customer.test_customer_get_orders(

        )

    def test_customer_place_order(self):
        self.executor_customer.test_customer_place_order(
            {
                "created_at": "2022-08-04T07:09:20.882Z",
                "created_by": "string",
                "updated_at": "2022-08-04T07:09:20.882Z",
                "updated_by": "string",
                "payment_method": "COD",
                "shipping_fee_discount": 0.3,
                "name_shipping": "string",
                "customer_username": "vietanh",
                "discount": 0.2
            }
        )
        self.executor_customer.test_customer_place_order_customer_username_not_found(
            {
                "created_at": "2022-08-04T07:09:20.882Z",
                "created_by": "string",
                "updated_at": "2022-08-04T07:09:20.882Z",
                "updated_by": "string",
                "payment_method": "COD",
                "shipping_fee_discount": 0.3,
                "name_shipping": "string",
                "customer_username": "XYZ",
                "discount": 0.2
            }
        )

    def test_customer_get_products(self):
        self.executor_customer.test_customer_get_products(
            brand="no",
            page=1,
            size=2,
            sort_direction="asc"
        )
        self.executor_customer.test_customer_get_products(
            from_price=Decimal(0),
            to_price=Decimal(200000),
            brand="no",
            page=1,
            size=2,
            sort_direction="asc"
        )
        self.executor_customer.test_customer_get_products(
            size=2,
            sort_direction="desc"
        )
        self.executor_customer.test_customer_get_products(
            brand="NO",
            page=1,
            size=2,
        )

    def test_customer_get_product_by_id(self):
        self.executor_customer.test_customer_get_product_by_id_successful(1)
        self.executor_customer.test_customer_get_product_not_found_id(100)
