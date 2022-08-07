import pandas as pd

from repo.cart import CartItemRepo
from repo.customer import CustomerRepo
from repo.sku import SkuRepo
from schema import CustomerReq


class CustomerService(CustomerRepo):
    def insert_customer_service(self, customer: CustomerReq):
        data_district = pd.read_excel(
            """/home/minerva-backend/Desktop/repos/ecommerce_oracle_database/service/shipping_code/district_29_07.xls""",
            dtype=str)['Mã']
        data_province = pd.read_excel(
            """/home/minerva-backend/Desktop/repos/ecommerce_oracle_database/service/shipping_code/province_29_07.xls""",
            dtype=str)['Mã']
        data_ward = pd.read_excel(
            """/home/minerva-backend/Desktop/repos/ecommerce_oracle_database/service/shipping_code/ward_29_07.xls""",
            dtype=str)['Mã']
        for item in data_ward:
            if customer.ward_code == item:
                customer.ward_code = item
        for item in data_district:
            if customer.district_code == item:
                customer.district_code = item
        for item in data_province:
            if customer.province_code == item:
                customer.province_code = item
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
        return customer
