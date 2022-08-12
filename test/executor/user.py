import base64
from decimal import Decimal
from typing import Dict
from starlette import status
from test.client import client
import requests


class UserAPIExecutor():
    def authentication(self, request):
        req = client.post(url="http://127.0.0.1:8000/users/token", headers=request.headers.get("Authorization"))
    def test_user_sign_up(self):
        ...

    def test_user_sign_in(self):
        ...

    def test_get_users(self):
        ...

    def test_put_user(self):
        ...

    def test_delete_user(self):
        ...

    def test_login_for_access_token(self):
        username = "ANH"
        password = "123456"
        self.authentication()
        res = self.te(username, password)
