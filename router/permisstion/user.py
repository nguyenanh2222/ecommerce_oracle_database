import os
from datetime import datetime, date, timedelta
from typing import List, Optional
import datetime
import jwt
from fastapi import APIRouter, Body, Query, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials, HTTPAuthorizationCredentials, HTTPBearer
from starlette import status
from starlette.requests import Request
from starlette.responses import Response

from project.schemas import DataResponse
from router.examples.user import user_op1

from schema import UserReq
from service.permisstion.user import UserService
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

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
def get_user(role_name: str = Query(None, example="ADMIN"),
             credentials: HTTPAuthorizationCredentials = Security(HTTPBearer())):
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


@router.post(
    path="/login",
    status_code=status.HTTP_200_OK
)
async def login(credentials: HTTPBasicCredentials = Security(
    HTTPBasic())):
    payload = {
        "sub": credentials.username,
        "exp": datetime.datetime.now() + datetime.timedelta(hours=2, minutes=10)
    }
    token = jwt.encode(payload=payload,
                       key=os.getenv('SECRET_KEY'),
                       algorithms=os.getenv('ALGORITHM'))
    return token


@router.post(
    path="/sample-api"
)
async def required_token(credentials: HTTPAuthorizationCredentials = Security(HTTPBearer())):
    # request: Request)
    # print(type(request.user))
    # return request.user
    scheme = credentials.scheme
    token = credentials.credentials
    token_content = jwt.decode(token,
                               key=os.getenv('SECRET_KEY'),
                               algorithms=os.getenv('ALGORITHM'))
    return token_content
