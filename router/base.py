from fastapi import APIRouter
from starlette import status

from project.schemas import DataResponse
from repo.product import ProductRepo
from schema import UserReq, UserRes, ProductReq, SkuReq, ProductRes
from service.base import UserService

router = APIRouter()


@router.post(path="/user",
             response_model=DataResponse,
             status_code=status.HTTP_200_OK)
def insert_user_router(user: UserReq):
    user = UserService().insert_user_service(UserReq(created_at=user.created_at,
                                                     created_by=user.created_by,
                                                     updated_at=user.updated_at,
                                                     updated_by=user.updated_by,
                                                     username=user.username,
                                                     password=user.password,
                                                     firstname=user.firstname,
                                                     lastname=user.lastname))
    return DataResponse(data=user)


# @router.put(path="/user")
# def update_user_router(username: str, user: UserReq):
#     username = 'A'
#     return user
#
#
# @router.get(path="/users")
# def get_user_router(created_at: datetime, created_by: str,
#                     updated_at: datetime, updated_by: str,
#                     first_name: str, last_name: str,
#                     page: int, size: int):
#     ...
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





