from typing import List
from sqlalchemy import insert, update, select, delete
from sqlalchemy.engine import Row, CursorResult
from sqlalchemy.orm import Session
from datetime import date
from model import User, UserRole, RolePermission, Permission, Role
from database import SessionLocal
from schema import UserReq


class UserRepo:
    def insert_user_repo(self, user: UserReq) -> Row:
        session: Session = SessionLocal()
        session.add(User(created_at=user.created_at,
                         created_by=user.created_by,
                         updated_at=user.updated_at,
                         updated_by=user.updated_by,
                         username=user.username,
                         password=user.password,
                         firstname=user.firstname,
                         lastname=user.lastname
                         ))
        session.commit()
        user = session.get(User, user.username)
        return user

    def update_product_repo(self, username: str, user: UserReq) -> Row:
        session: Session = SessionLocal()
        query = update(User).where(username == id).values(created_at=user.created_at,
                                                                created_by=user.created_by,
                                                                update_at=user.updated_at,
                                                                update_by=user.updated_by,
                                                                password=user.password,
                                                                first_name=user.password,
                                                                last_name=user.lastname).returning(User)
        rs = session.execute(query).fetchall()
        session.commit()
        return rs

    def get_user_repo(self, created_at: date, created_by: str,
                      updated_at: date, updated_by: str,
                      first_name: str, last_name: str,
                      page: int, size: int) -> List[Row]:
        session: Session = SessionLocal()
        query = select(UserRole).join(User, User.username)
        if created_at:
            query += query.where(User.created_at == created_at)
        if updated_at:
            query += query.where(User.updated_at == updated_at)
        if created_by:
            query += query.where(User.created_by == created_by)
        if updated_by:
            query += query.where(User.updated_by == updated_by)
        if first_name:
            query += query.where(User.firstname == first_name)
        if last_name:
            query += query.where(User.lastname == last_name)
        if page and size:
            query += query.limit(size).offset((page - 1) * size)
        rs = session.execute(query).fetchall()
        return rs

    def get_permission_repo(self, permission_name: str, role_name: str):
        session: Session = SessionLocal()
        query = select(RolePermission).join(Permission, Permission.code).join(Role, Role.code)
        if permission_name:
            query += query.where(Permission.name == permission_name)
        if role_name:
            query += query.where(Role.name == role_name)
        rs = session.execute(query).fetchall()
        return rs

    def delete_user_repo(self, username: str):
        session: Session = SessionLocal()
        query = delete(User).where(User.username == username).returning(User)
        rs = session.execute(query).fetchone()
        return rs
