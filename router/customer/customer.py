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
    customer = CustomerService().insert_customer_service(
        customer=CustomerReq(
            username=customer.username,
            created_at=customer.created_at,
            created_by=customer.created_by,
            updated_at=customer.updated_at,
            updated_by=customer.updated_by,
            phone=customer.phone,
            address=customer.address,
            province_code=customer.province_code,
            district_code=customer.district_code,
            ward_code=customer.ward_code
        ))
    return DataResponse(data=customer)


@router.put(
    path="/{id}",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def update_customer(username: str, customer: CustomerReq = Body(..., examples=customer_op1)):
    customer = CustomerService().update_customer_service(customer=CustomerReq(
        created_at=customer.created_at,
        created_by=customer.created_by,
        updated_at=customer.updated_at,
        updated_by=customer.updated_by,
        username=customer.username,
        phone=customer.phone,
        address=customer.address,
        province_code=customer.province_code,
        district_code=customer.district_code,
        ward_code=customer.ward_code)
        , username=username)
    return DataResponse(data=customer)


@router.get(
    path="/{id}",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def get_customer(username: str) -> DataResponse:
    customer = CustomerService().get_customer_by_username_service(username=username)
    return DataResponse(data=customer)
