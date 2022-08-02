from fastapi import APIRouter, Body
from starlette import status

from project.schemas import DataResponse
from router.examples.customer import customer_op1
from schema import CustomerRes, CustomerReq, UserReq
from service.customer.customer import CustomerService

router = APIRouter()
@router.post(
    path="/",
    response_model=DataResponse,
    status_code=status.HTTP_201_CREATED
)
def insert_customer(customer: CustomerReq = Body(
    ..., examples=customer_op1)) -> DataResponse:
    customer = CustomerService().insert_customer_service(customer=CustomerReq(
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
    return DataResponse(data=customer)

@router.put(
    path="/",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def update_customer(username: str, customer: CustomerReq = Body(..., examples=customer_op1)):
        customer = CustomerService().update_customer_service(customer=CustomerReq(
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
        return DataResponse(data=customer)

@router.get(
    path="/{id}",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def get_customer(username: str) -> DataResponse:
    customer = CustomerService().get_customer_by_username_service(username=username)
    return DataResponse(data=customer)