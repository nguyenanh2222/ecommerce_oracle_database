import base64
from decimal import Decimal
from typing import Dict
from starlette import status
from test.client import client


class AdminAPIExecutor():
    def test_admin_get_products(self,
                                name: str = None,
                                category: str = None,
                                color: str = None,
                                from_price: Decimal = None,
                                to_price: Decimal = None,
                                brand: str = None,
                                page: int = None,
                                size: int = None,
                                sort_direction: str = None):
        res = f'http://127.0.0.1:8000/products/?'
        if name:
            res += f"name={name}&"
        if color:
            res += f"page={color}&"
        if brand:
            res += f"size={brand}&"
        if category:
            res += f"category={category}&"
        if from_price:
            res += f"from_price={from_price}&"
        if to_price:
            res += f"to_price={to_price}&"
        if sort_direction:
            res += f"sort_direction={sort_direction}&"
        if page:
            res += f"page={page}&"
        if size:
            res += f"size={size}&"
        res = client.get(res[:-1])
        assert res.status_code == status.HTTP_200_OK

    def test_admin_insert_product_successful(self, body: Dict):
        res = client.post("http://127.0.0.1:8000/products/", json=body)
        assert res.status_code == status.HTTP_201_CREATED

    def test_admin_insert_product_validation_error(self, body: Dict):
        res = client.post("http://127.0.0.1:8000/products/", json=body)
        assert res.status_code == status.HTTP_400_BAD_REQUEST

    def test_admin_insert_product_validation_missing(self, body: Dict):
        res = client.post("http://127.0.0.1:8000/products/", json=body)
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_admin_delete_product_successful(self, id):
        res = client.delete(f"http://127.0.0.1:8000/products/?product_id={id}")
        assert res.status_code == status.HTTP_204_NO_CONTENT

    def test_admin_delete_product_not_found_id(self, id):
        res = client.delete(f"http://127.0.0.1:8000/products/?product_id={id}")
        assert res.status_code == status.HTTP_404_NOT_FOUND

    def test_admin_get_product_by_id_successful(self, id):
        res = client.get(f"http://127.0.0.1:8000/products/?product_id={id}")
        assert res.status_code == status.HTTP_200_OK

    def test_admin_get_product_not_found_id(self, id):
        res = client.get(f"http://127.0.0.1:8000/products/{id}?product_id={id}")
        assert res.status_code == status.HTTP_404_NOT_FOUND

    def test_admin_update_product_by_id_successful(self, id, body: Dict):
        res = client.put(f"http://127.0.0.1:8000/products/{id}?product_id={id}", json=body)
        assert res.status_code == status.HTTP_200_OK

    def test_admin_update_product_not_found_id(self, id, body: Dict):
        res = client.put(f"http://127.0.0.1:8000/products/{id}?product_id={id}", json=body)
        assert res.status_code == status.HTTP_404_NOT_FOUND

    def test_admin_update_product_validation_missing(self, id, body: Dict):
        res = client.put(f"http://127.0.0.1:8000/products/{id}?product_id={id}", json=body)
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_admin_get_orders(self,
                              customer_name: str = None,
                              id: int = None,
                              payment_method: str = None,
                              name_shipping: str = None,
                              phone_shipping: str = None,
                              address_shipping: str = None,
                              province_code_shipping: str = None,
                              ward_code_shipping: str = None,
                              district_code_shipping: str = None,
                              customer_username: str = None,
                              from_price: Decimal = None,
                              to_price: Decimal = None,
                              page: int = None,
                              size: int = None,
                              sort_direction: str = None):
        res = f'http://127.0.0.1:8000/products/?'
        if id:
            res += f"id={id}&"
        if customer_name:
            res += f"customer_username={customer_name}&"
        if payment_method:
            res += f"payment_method={payment_method}&"
        if name_shipping:
            res += f"name_shipping={name_shipping}&"
        if phone_shipping:
            res += f"phong_shipping={phone_shipping}&"
        if address_shipping:
            res += f"address_shipping={address_shipping}&"
        if province_code_shipping:
            res += f"province_code_shipping={province_code_shipping}&"
        if ward_code_shipping:
            res += f"ward_code_shipping={ward_code_shipping}&"
        if district_code_shipping:
            res += f"district_code_shipping={district_code_shipping}&"
        if customer_username:
            res += f"customer_username={customer_username}"
        if from_price:
            res += f"from_price={from_price}&"
        if to_price:
            res += f"to_price={to_price}&"
        if sort_direction:
            res += f"sort_direction={sort_direction}&"
        if page:
            res += f"page={page}&"
        if size:
            res += f"size={size}&"
        res = client.get(res[:-1])
        assert res.status_code == status.HTTP_200_OK

    def test_admin_get_order_by_id_successful(self, id):
        res = client.get(f"http://127.0.0.1:8000/orders/{id}?order_id={id}")
        assert res.status_code == status.HTTP_200_OK

    def test_admin_get_order_not_found_id(self, id):
        res = client.get(f"http://127.0.0.1:8000/orders/{id}?order_id={id}")
        assert res.status_code == status.HTTP_404_NOT_FOUND

    def test_admin_put_change_status_successful(self, id, next_status):
        res = client.put(f'http://127.0.0.1:8000/orders/change_status?order_id={id}&next_status={next_status}')
        assert res.status_code == status.HTTP_200_OK

    def test_admin_put_change_status_not_found_id(self, id, next_status):
        res = client.put(f'http://127.0.0.1:8000/orders/change_status?order_id={id}&next_status={next_status}')
        assert res.status_code == status.HTTP_404_NOT_FOUND

    def test_admin_post_upload_file_successful(self):
        res = client.post('http://127.0.0.1:8000/files/',
                          files={"file": open(
                              '/home/minerva-backend/Desktop/repos/ecommerce_oracle_database/files/api.png', "rb")})
        assert res.status_code == status.HTTP_200_OK

    def test_admin_post_upload_file_value_error(self):
        res = client.post('http://127.0.0.1:8000/files/',
                          files={"file": open(
                              '/home/minerva-backend/Desktop/repos/ecommerce_oracle_database/files/Untitled-1.odt',
                              "rb")})
        assert res.status_code == status.HTTP_400_BAD_REQUEST

