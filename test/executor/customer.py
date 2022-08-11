from decimal import Decimal
from typing import Dict
from starlette import status
from test.client import client


class CustomerAPIExecutor():
    def test_customer_created_profile_successful(self, body: Dict):
        res = client.post("http://127.0.0.1:8000/customers/", json=body)
        assert res.status_code == status.HTTP_201_CREATED

    def test_customer_created_profile_values_error(self, body: Dict):
        res = client.post("http://127.0.0.1:8000/customers/", json=body)
        assert res.status_code == status.HTTP_400_BAD_REQUEST

    def test_customer_get_profile_by_username_successful(self, username):
        res = client.get(f"http://127.0.0.1:8000/customers/{username}")
        assert res.status_code == status.HTTP_200_OK

    def test_customer_get_profile_by_username_not_found(self, username):
        res = client.get(f"http://127.0.0.1:8000/customers/{username}")
        assert res.status_code == status.HTTP_404_NOT_FOUND

    def test_customer_update_profile_successful(self, body: Dict, username):
        res = client.put(f"http://127.0.0.1:8000/customers/{username}", json=body)
        assert res.status_code == status.HTTP_200_OK

    def test_customer_update_profile_not_found_username(self, body: Dict, username):
        res = client.put(f"http://127.0.0.1:8000/customers/{username}", json=body)
        assert res.status_code == status.HTTP_404_NOT_FOUND

    def test_customer_update_profile_value_error(self, body: Dict, username):
        res = client.put(f"http://127.0.0.1:8000/customers/{username}", json=body)
        assert res.status_code == status.HTTP_400_BAD_REQUEST

    def test_customer_get_cart_items_successful(self, username):
        res = client.get(f"http://127.0.0.1:8000/customers/carts/?username={username}")
        assert res.status_code == status.HTTP_200_OK

    def test_customer_get_cart_items_not_found_username(self, username):
        res = client.get(f"http://127.0.0.1:8000/customers/carts/?username={username}")
        assert res.status_code == status.HTTP_404_NOT_FOUND

    def test_customer_insert_cart_item_successful(self, body: Dict):
        res = client.post(f"http://127.0.0.1:8000/customers/carts/", json=body)
        assert res.status_code == status.HTTP_201_CREATED

    def test_customer_insert_cart_item_value_missing(self, body: Dict):
        res = client.post(f"http://127.0.0.1:8000/customers/carts/", json=body)
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_customer_get_cart_item_by_id_successful(self, id):
        res = client.get(f"http://127.0.0.1:8000/customers/carts/{id}")
        assert res.status_code == status.HTTP_200_OK

    def test_customer_get_cart_item_by_id_not_found(self, id):
        res = client.get(f"http://127.0.0.1:8000/customers/carts/{id}")
        assert res.status_code == status.HTTP_404_NOT_FOUND

    def test_customer_update_cart_item_successful(self, id, body: Dict):
        res = client.put(f"http://127.0.0.1:8000/customers/carts/{id}", json=body)
        assert res.status_code == status.HTTP_200_OK

    def test_customer_update_cart_item_not_found(self, id, body: Dict):
        res = client.put(f"http://127.0.0.1:8000/customers/carts/{id}", json=body)
        assert res.status_code == status.HTTP_404_NOT_FOUND

    def test_customer_update_cart_item_value_error(self, id, body: Dict):
        res = client.put(f"http://127.0.0.1:8000/customers/carts/{id}", json=body)
        assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_customer_delete_cart_item_successful(self, id):
        res = client.delete(f'http://127.0.0.1:8000/customers/carts/{id}')
        assert res.status_code == status.HTTP_204_NO_CONTENT

    def test_customer_delete_cart_item_not_found(self, id):
        res = client.delete(f'http://127.0.0.1:8000/customers/carts/{id}')
        assert res.status_code == status.HTTP_404_NOT_FOUND

    def test_customer_get_orders(self,
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

    def test_customer_place_order(self, body: Dict):
        res = client.post("http://127.0.0.1:8000/customers/orders/", json=body)
        assert res.status_code == status.HTTP_201_CREATED

    def test_customer_place_order_customer_username_not_found(self, body: Dict):
        res = client.post("http://127.0.0.1:8000/customers/orders/", json=body)
        assert res.status_code == status.HTTP_400_BAD_REQUEST

    def test_customer_get_products(self,
                                   name: str = None,
                                   category: str = None,
                                   color: str = None,
                                   from_price: Decimal = None,
                                   to_price: Decimal = None,
                                   brand: str = None,
                                   page: int = None,
                                   size: int = None,
                                   sort_direction: str = None):
        res = f'http://127.0.0.1:8000/customers/products/?'
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

    def test_customer_get_product_by_id_successful(self, id):
        res = client.get(f"http://127.0.0.1:8000/customers/products/{id}?product_id={id}")
        assert res.status_code == status.HTTP_200_OK

    def test_customer_get_product_not_found_id(self, id):
        res = client.get(f"http://127.0.0.1:8000/customers/products/{id}?product_id={id}")
        assert res.status_code == status.HTTP_404_NOT_FOUND
