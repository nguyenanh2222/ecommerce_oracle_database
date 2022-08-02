from fastapi import HTTPException
from starlette import status

from repo.customer import CustomerRepo
from schema import CustomerReq, UserReq


class CustomerService(CustomerRepo):
    def insert_customer_service(self, customer: CustomerReq):
        customer = CustomerRepo().insert_customer_repo(customer=CustomerReq(
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
            ward_code=customer.ward_code,
            user=UserReq(
                created_at=customer.created_at,
                created_by=customer.created_by,
                updated_at=customer.updated_at,
                updated_by=customer.updated_by,
                username=customer.user.username,
                password=customer.user.password,
                firstname=customer.user.firstname,
                lastname=customer.user.lastname
            )
        ))
        return customer

    def update_customer_service(self, customer: CustomerReq, username: str):
        customer = CustomerRepo().update_customer_repo(customer=CustomerReq(
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
            ward_code=customer.ward_code,
            user=UserReq(
                created_at=customer.created_at,
                created_by=customer.created_by,
                updated_at=customer.updated_at,
                updated_by=customer.updated_by,
                username=customer.user.username,
                password=customer.user.password,
                firstname=customer.user.firstname,
                lastname=customer.user.lastname
            )
        ), username=username)
        return customer

    def get_customer_by_username_service(self, username: str):
        customer = CustomerRepo().get_customer_by_username_repo(username=username)
        return customer
