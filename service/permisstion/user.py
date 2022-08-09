import os
import uuid

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

    def authenticate_user(self,  username: str, password: str):
        user = UserRepo().get_user_by_username_repo(username)
        if not user:
        #     return False
        # user = get_user(fake_db, username)
        #
        # if not verify_password(password, user.hashed_password):
            return False
        return user

    def get_user_by_username_service(self, username: str):
        user = UserRepo().get_user_by_username_repo(username)
        return user

    def get_hashed_password(self, plain_text_password):
        return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt(rounds=12, prefix=b"2b"))

    def check_password(self, plain_text_password, hashed_password):
        return bcrypt.checkpw(password=plain_text_password, hashed_password=hashed_password)

    def sign_in_service(self, user: UserReq):
        password = self.get_hashed_password(user.password)        # confirm password
        user = UserReq(
            created_at=user.created_at,
            created_by=user.created_by,
            updated_at=user.updated_at,
            updated_by=user.updated_by,
            username=user.username,
            password=password,
            firstname=user.firstname,
            lastname=user.lastname, role=RoleReq(
                code=user.role.code,
                name=user.role.name
            ))
        role = UserRepo().insert_role(role=user.role)
        user = UserRepo().insert_user_repo(user=user)
        return user

    def sign_up_service(self, username: str, password: str):
        user_db = UserRepo().get_user_by_username_repo(username)
        if user_db != None:
            if self.check_password(password.encode('utf-8'), user_db['User'].password.encode('utf-8')):
                return {'username': username, 'password': password }
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)



    def get_roles(self):
        roles = UserRepo().get_roles()
        return roles

    def add_role(self, role: RoleReq):
        role = UserRepo().insert_role(role=role)
        return role
