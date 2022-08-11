from http.client import HTTPException

import pandas as pd
from fastapi import HTTPException
from starlette import status

from repo.cart import CartItemRepo
from repo.customer import CustomerRepo
from repo.sku import SkuRepo
from schema import CustomerReq


class CustomerService(CustomerRepo):
    def check_address_code(self, province_code, district_code, ward_code):
        data_province = pd.read_excel(
            """/home/minerva-backend/Desktop/repos/ecommerce_oracle_database/service/shipping_code/province_29_07.xls""",
            dtype=str)['Mã']
        point = True
        for item in [item for item in data_province]:
            if province_code == item:
                province_code = item
                point = False
        if point:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        data_district = pd.read_excel(
            """/home/minerva-backend/Desktop/repos/ecommerce_oracle_database/service/shipping_code/district_29_07.xls""",
            dtype=str)['Mã']
        point = True
        for item in [item for item in data_district]:
            if district_code == item:
                district_code = item
                point = False
        if point:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        data_ward = pd.read_excel(
            """/home/minerva-backend/Desktop/repos/ecommerce_oracle_database/service/shipping_code/ward_29_07.xls""",
            dtype=str)['Mã']
        point = True
        for item in [item for item in data_ward]:
            if ward_code == item:
                ward_code = item
                point = False
        if point:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    def insert_customer_service(self, customer: CustomerReq):
        self.check_address_code(district_code=customer.district_code,
                                province_code=customer.province_code,
                                ward_code=customer.ward_code)
        if self.get_customer_by_username_repo(customer.username) != None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        customer = CustomerRepo().insert_customer_repo(customer=CustomerReq(
            username=customer.username,
            created_at=customer.created_at,
            created_by=customer.created_by,
            updated_at=customer.updated_at,
            updated_by=customer.updated_by,
            phone=customer.phone,
            address=customer.address,
            province_code=customer.province_code,
            district_code=customer.district_code,
            ward_code=customer.ward_code,
            password=customer.password,
            firstname=customer.firstname,
            lastname=customer.lastname
        ))

        return customer

    def update_customer_service(self, customer: CustomerReq, username: str):
        self.check_address_code(district_code=customer.district_code,
                                province_code=customer.province_code,
                                ward_code=customer.ward_code)
        _customer = CustomerRepo().get_customer_by_username_repo(username)
        if _customer == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        customer = CustomerRepo().update_customer_repo(customer=CustomerReq(
            username=customer.username,
            created_at=customer.created_at,
            created_by=customer.created_by,
            updated_at=customer.updated_at,
            updated_by=customer.updated_by,
            phone=customer.phone,
            address=customer.address,
            province_code=customer.province_code,
            district_code=customer.district_code,
            ward_code=customer.ward_code,
            password=customer.password,
            firstname=customer.firstname,
            lastname=customer.lastname)
            , username=username)
        return customer

    def get_customer_by_username_service(self, username: str):
        customer = CustomerRepo().get_customer_by_username_repo(username=username)
        if customer == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return customer
