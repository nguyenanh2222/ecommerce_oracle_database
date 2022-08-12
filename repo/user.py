from enum import Enum
from typing import List

from sqlalchemy import update, select, delete
from sqlalchemy.engine import Row
from sqlalchemy.orm import Session
from model import User, RolePermission, Permission, Role, UserRole
from database import SessionLocal
from schema import UserReq, RoleReq


class UserRepo:
    def insert_user_repo(self, user: UserReq, salt: bytes) -> Row:
        session = SessionLocal()
        user_db = User(
            created_at=user.created_at,
            created_by=user.created_by,
            updated_at=user.updated_at,
            updated_by=user.updated_by,
            username=user.username,
            password=user.password,
            firstname=user.firstname,
            lastname=user.lastname,
            salt=salt
        )
        session.add(user_db)
        session.commit()
        role = Role(
            code=user.role.code,
            name=user.role.name
        )
        session.add(role)
        session.commit()
        user_role = UserRole(
            username=user.username,
            role_code=user.role.code
        )
        session.add(user_role)
        session.commit()
        rs = session.get(User, user.username)
        return rs

    def update_product_repo(self, username: str, user: UserReq) -> Row:
        session = SessionLocal()
        query = update(User).values(
            created_at=user.created_at,
            created_by=user.created_by,
            updated_at=user.updated_at,
            updated_by=user.updated_by,
            password=user.password,
            firstname=user.firstname,
            lastname=user.lastname
        ).where(
            User.username == username)
        session.execute(query)
        session.commit()
        rs = session.get(User, username)
        return rs

    def get_users(self) -> List[Row]:
        session = SessionLocal()
        query = session.query(User)
        rs = session.execute(query).fetchall()
        return rs

    def get_role(self, username: str) -> Row:
        session = SessionLocal()
        query = session.query(Role).join(UserRole).filter(
            UserRole.username == username)
        rs = session.execute(query).fetchone()
        return rs

    def get_permisstion(self, role_code: str) -> List:
        session = SessionLocal()
        query = session.query(Permission).join(RolePermission).filter(RolePermission.role_code == role_code)
        rs = session.execute(query).fetchall()
        list_permission = [permission['Permission'].name for permission in rs]
        return list_permission

    def get_user_by_username_repo(self, username: str) -> User:
        session = SessionLocal()
        return session.query(User).filter(User.username == username).one()

    def delete_user_repo(self, username: str):
        session = SessionLocal()
        query = delete(UserRole).where(UserRole.username == username)
        rs = session.execute(query)
        query = delete(User).where(User.username == username)
        rs = session.execute(query)
        rs = session.get(User, username)
        return rs

    def authenticate_repo(self, username: str, password: str) -> Row:
        session = SessionLocal()
        query = session.query(User).get(username)
        rs = session.execute(query).fetchone()
        return rs

    def get_roles(self):
        session = SessionLocal()
        query = session.query(Role)
        rs = session.execute(query)
        return rs

    def insert_role(self, role: RoleReq):
        session = SessionLocal()
        role = Role(
            code=role.code,
            name=role.name
        )
        session.add(role)
        session.commit()
        return role
