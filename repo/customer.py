from typing import List

from sqlalchemy import select, insert, update, delete
from sqlalchemy.engine import Row
from sqlalchemy.orm import Session

from database import SessionLocal
from model import Customer, User
from schema import CustomerReq


class CustomerRepo():
    # def get_customers(self) -> List[Row]:
    #     session: Session = SessionLocal()
    #     stmt = select(Customer)
    #     rs = session.execute(stmt).fetchall()
    #     return rs

    def get_customer_by_username_repo(self, username: str) -> Row:
        session: Session = SessionLocal()
        stmt = select(Customer).where(Customer.username == username)
        rs = session.execute(stmt).fetchone()
        return rs

    def insert_customer(self, customer: CustomerReq):
        session: Session = SessionLocal()
        stmt = insert(Customer).values(
            created_at=customer.created_at,
            created_by=customer.created_by,
            updated_at=customer.updated_at,
            updated_by=customer.updated_by,
            username=customer.user.username,
            password=customer.user.password,
            firstname=customer.user.firstname,
            lastname=customer.user.lastname,
            phone=customer.phone,
            address=customer.address,
            province_code=customer.province_code,
            district_code=customer.district_code,
            ward_code=customer.ward_code
        )
        session.execute(stmt)
        session.commit()
        stmt = insert(User).values(created_at=customer.created_at,
                                   created_by=customer.created_by,
                                   updated_at=customer.updated_at,
                                   updated_by=customer.updated_by,
                                   username=customer.user.username,
                                   password=customer.user.password,
                                   firstname=customer.user.firstname,
                                   lastname=customer.user.lastname)
        session.execute(stmt)
        session.commit()
        rs = session.get(Customer, customer.user.username)
        return rs

    def update_customer_repo(self, customer: CustomerReq, username: str) -> Row:
        session: Session = SessionLocal()
        stmt = update(Customer).values(created_at=customer.created_at,
                                       created_by=customer.created_by,
                                       updated_at=customer.updated_at,
                                       updated_by=customer.updated_by,
                                       username=customer.user.username,
                                       password=customer.user.password,
                                       firstname=customer.user.firstname,
                                       lastname=customer.user.lastname,
                                       phone=customer.phone,
                                       address=customer.address,
                                       province_code=customer.province_code,
                                       district_code=customer.district_code,
                                       ward_code=customer.ward_code
                                       ).where(Customer.username == username)
        session.execute(stmt)
        session.commit()
        stmt = update(User).values(created_at=customer.created_at,
                                   created_by=customer.created_by,
                                   updated_at=customer.updated_at,
                                   updated_by=customer.updated_by,
                                   username=customer.user.username,
                                   password=customer.user.password,
                                   firstname=customer.user.firstname,
                                   lastname=customer.user.lastname).where(
            User.username == username)
        session.execute(stmt)
        session.commit()
        rs = session.get(Customer, username)
        return rs

    def delete_customer_repo(self, usermane: str):
        session: Session = SessionLocal()
        stmt = delete(Customer).where(Customer.username == usermane).returning(Customer)
        session.execute(stmt)
