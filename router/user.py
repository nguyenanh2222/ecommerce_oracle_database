from datetime import datetime

from fastapi import APIRouter, Body, Query
from starlette import status

from project.schemas import DataResponse
from repo.product import ProductRepo
from router.examples.user import user_op1
from schema import UserReq, UserRes, ProductReq, SkuReq, ProductRes
from service.user import UserService

router = APIRouter()


@router.post(path="/user",
             response_model=DataResponse,
             status_code=status.HTTP_201_CREATED)
def insert_user(user: UserReq):
    user = UserService().insert_user_service(UserReq(created_at=user.created_at,
                                                     created_by=user.created_by,
                                                     updated_at=user.updated_at,
                                                     updated_by=user.updated_by,
                                                     username=user.username,
                                                     password=user.password,
                                                     firstname=user.firstname,
                                                     lastname=user.lastname))
    return DataResponse(data=user)


@router.put(
    path="/user",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def update_user(username: str, user: UserReq = Body(..., examples=user_op1)):
    user = UserService().update_user_service(username=username, user=UserReq(
        created_at=user.created_at,
        created_by=user.created_by,
        updated_at=user.updated_at,
        updated_by=user.updated_by,
        password=user.password,
        firstname=user.password,
        lastname=user.lastname
    ))
    return DataResponse(data=user)


@router.get(path="/users",
            response_model=DataResponse,
            status_code=status.HTTP_200_OK)
def get_user_router():
    ...
#
#
# @router.get(path="/permissions")
# def get_permission_router(permission_name: str, role_name: str):
#     ...
#
#
# @router.get(path="/{username}")
# def delete_user_router(username: str):
#     ...
