from typing import List, Optional

from fastapi import APIRouter, Body, Query
from starlette import status
from starlette.responses import Response

from project.schemas import DataResponse
from router.examples.user import user_op1
from schema import UserReq
from service.permisstion.user import UserService
router = APIRouter()


@router.post(path="/",
             response_model=DataResponse,
             status_code=status.HTTP_201_CREATED)
def insert_user(user: UserReq):
    user = UserService().insert_user_service(UserReq(
        created_at=user.created_at,
        created_by=user.created_by,
        updated_at=user.updated_at,
        updated_by=user.updated_by,
        username=user.username,
        password=user.password,
        firstname=user.firstname,
        lastname=user.lastname))
    return DataResponse(data=user)


@router.put(
    path="/{id}",
    response_model=DataResponse,
    status_code=status.HTTP_200_OK
)
def update_user(username: str, user: UserReq = Body(..., examples=user_op1)):
    user = UserService().update_user_service(username=username, user=UserReq(
        created_at=user.created_at,
        created_by=user.created_by,
        updated_at=user.updated_at,
        updated_by=user.updated_by,
        username=user.username,
        password=user.password,
        firstname=user.firstname,
        lastname=user.lastname))
    return DataResponse(data=user)


@router.get(path="/",
            status_code=status.HTTP_200_OK,
            response_model=DataResponse)
def get_user(role_name: str = Query(None, example="ADMIN")):
    users = UserService().get_users_service(role_name)
    return DataResponse(data=users)

@router.get(
    path="/{id}",
    status_code=status.HTTP_200_OK,
    response_model=DataResponse
)
def get_user_by_id(username: str = Query(..., example="vietanh")):
    user = UserService().get_user_by_username_repo(username)
    return DataResponse(data=user)

@router.delete(
    path="/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(username: str):
    user = UserService().delete_user_service(username=username)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

