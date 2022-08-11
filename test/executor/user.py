from decimal import Decimal
from typing import Dict
from starlette import status
from test.client import client


class UserAPIExecutor():
    def test_user_sign_up(self):
        ...

    def test_user_sign_in(self):
        ...

    def test_get_user_by_username(self):
        ...

    def test_get_users(self):
        ...

    def test_put_user(self):
        ...

    def test_delete_user(self):
        ...

    def test_login_for_access_token(self, username, password):
        data = {"username": "ANH", "password": "" }
        res = client.post("http://127.0.0.1:8000/users/token", )