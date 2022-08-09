import os
from datetime import datetime
import datetime
import jwt
from fastapi import APIRouter, Body, Query, Security, Depends, HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBasic, HTTPAuthorizationCredentials, HTTPBearer
from starlette import status
from starlette.responses import Response
from project.schemas import DataResponse
from router.examples.user import user_op1
from schema import UserReq, Token, RoleReq
from service.permisstion.user import UserService

router = APIRouter()


# @router.post(path="/",
#              response_model=DataResponse,
#              status_code=status.HTTP_201_CREATED)
# def insert_user(user: UserReq):
#     user = UserService().insert_user_service(UserReq(
#         created_at=user.created_at,
#         created_by=user.created_by,
#         updated_at=user.updated_at,
#         updated_by=user.updated_by,
#         username=user.username,
#         password=user.password,
#         firstname=user.firstname,
#         lastname=user.lastname))
#     return DataResponse(data=user)

@router.post(path="/sign_in",
             response_model=DataResponse,
             status_code=status.HTTP_201_CREATED)
def sign_up(user: UserReq):
    user = UserService().sign_up_service(UserReq(
        created_at=user.created_at,
        created_by=user.created_by,
        updated_at=user.updated_at,
        updated_by=user.updated_by,
        username=user.username,
        password=user.password,
        firstname=user.firstname,
        lastname=user.lastname,
        role=RoleReq(
            code=user.role.code,
            name=user.role.name
        )))
    return DataResponse(data=user)


@router.post(path="/sign_up",
             status_code=status.HTTP_200_OK)
def sign_in(username: str, password: str,
            credentials: HTTPAuthorizationCredentials = Security(HTTPBearer())):
    user = UserService().sign_in_service(username, password)
    token = credentials.credentials
    token_content = jwt.decode(token,
                               key=os.getenv('SECRET_KEY'),
                               algorithms=os.getenv("ALGORITHM"))
    return token_content


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


@router.post(
    path="/token",
    status_code=status.HTTP_201_CREATED,
    response_model=Token
)
async def login_for_access_token(
        credentials: HTTPBasicCredentials = Security(HTTPBasic())) -> Token:
    user = UserService().authenticate_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = UserService().check_password(str(credentials.username).encode('utf-8'))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"})

    role = UserService().get_role(credentials.username)
    role_code = role['Role'].code
    permissions = UserService().get_permisstion(role_code)
    payload = {
        "sub": credentials.username,
        "iat": datetime.datetime.now(),
        "exp": datetime.datetime.now() + datetime.timedelta(hours=2, minutes=10),
        "role": role['Role'].name,
        "permission": permissions
    }
    token = jwt.encode(payload=payload,
                       key=os.getenv('SECRET_KEY'),
                       algorithm=os.getenv("ALGORITHM"))
    return Token(access_token=token,
                 token_type='Bearer')


@router.post(
    path="/sample-api"
)
async def required_token(credentials: HTTPAuthorizationCredentials = Security(HTTPBearer())):
    scheme = credentials.scheme
    token = credentials.credentials
    token_content = jwt.decode(token,
                               key=os.getenv('SECRET_KEY'),
                               algorithms=os.getenv("ALGORITHM"))
    return token_content
