from datetime import date
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