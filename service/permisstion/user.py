import datetime
import hashlib
import math
import os
import uuid
import random

import bcrypt
import jwt
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from starlette import status
from starlette.exceptions import HTTPException
from repo.user import UserRepo
from schema import UserReq, RoleReq

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService(UserRepo):
    # def insert_user_service(self, user: UserReq):
    #     user = UserRepo().insert_user_repo(UserReq(
    #         created_at=user.created_at,
    #         created_by=user.created_by,
    #         updated_at=user.updated_at,
    #         updated_by=user.updated_by,
    #         username=user.username,
    #         password=user.password,
    #         firstname=user.firstname,
    #         lastname=user.lastname))
    #     return user

    def update_user_service(self, username: str, user: UserReq):
        user = UserRepo().update_product_repo(username=username,
                                              user=UserReq(
                                                  created_at=user.created_at,
                                                  created_by=user.created_by,
                                                  updated_at=user.updated_at,
                                                  updated_by=user.updated_by,
                                                  username=user.username,
                                                  password=user.password,
                                                  firstname=user.firstname,
                                                  lastname=user.lastname))
        return user

    def get_users_service(self, role_name: str):
        users = UserRepo().get_users()
        list_user = []
        for user in users:
            username = user['User'].username
            role = UserRepo().get_role(username)
            permission = UserRepo().get_permisstion(role['Role'].code)
            list_user.append({'user': user['User'], 'role': role['Role'].name, 'permission': permission})
        return list_user

    def delete_user_service(self, username: str):
        user = UserRepo().delete_user_repo(username=username)

    def authenticate_user(self, username: str, password: str):
        user = UserRepo().get_user_by_username_repo(username)
        if not user:
            return False
        if not self.check_password(username, password):
            return False
        return user

    def get_user_by_username_service(self, username: str):
        user = UserRepo().get_user_by_username_repo(username)
        return user

    def get_hashed_password(self, plain_text_password, salt: bytes):
        hashed_pass = hashlib.md5(plain_text_password.encode("utf8") + salt).hexdigest()
        return hashed_pass

    def check_password(self, plain_text_password, username):
        user = UserRepo().get_user_by_username_repo(username)
        hashed_password = self.get_hashed_password(plain_text_password, user.salt)
        if user.password == hashed_password:
            return True
        else:
            return False

    def sign_up_service(self, user: UserReq):
        # salt = str(random.randint(0, 99)).encode("utf8")
        # password = self.get_hashed_password(user.password, salt)
        user = UserReq(
            created_at=user.created_at,
            created_by=user.created_by,
            updated_at=user.updated_at,
            updated_by=user.updated_by,
            username=user.username,
            password=user.password,
            firstname=user.firstname,
            lastname=user.lastname,
        )
        user = UserRepo().insert_user_repo(user=user)
        return user

    def sign_in(self, username: str, password: str) -> str:
        user_db = UserRepo().get_user_by_username_repo(username)
        print(user_db)
        if user_db is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        if password != user_db.password:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        return self.generate_token(username)

    def generate_token(self, username) -> str:
        payload = {
            "sub": username,
            "iat": datetime.datetime.now(),
            "exp": datetime.datetime.now() + datetime.timedelta(hours=2, minutes=10),
        }
        return jwt.encode(payload=payload,
                          key=os.getenv('SECRET_KEY'),
                          algorithm=os.getenv("ALGORITHM"))

    def get_roles(self):
        roles = UserRepo().get_roles()
        return roles

    def add_role(self, role: RoleReq):
        role = UserRepo().insert_role(role=role)
        return role
