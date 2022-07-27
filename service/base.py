from datetime import datetime
from repo.user import UserRepo
from schema import UserReq


class UserService(UserRepo):
    def insert_user_service(self, user: UserReq):
        user = UserRepo().insert_user_repo(UserReq(created_at=user.created_at,
                                                   created_by=user.created_by,
                                                   updated_at=user.updated_at,
                                                   updated_by=user.updated_by,
                                                   password=user.password,
                                                   firstname=user.firstname,
                                                   lastname=user.lastname))
        return user

    def update_user_service(self, username: str, user: UserReq):
        ...

    def get_user_service(self, created_at: datetime, created_by: str,
                         updated_at: datetime, updated_by: str,
                         first_name: str, last_name: str,
                         page: int, size: int):
        ...

    def get_permission_repo(self, permission_name: str, role_name: str):
        ...

    def delete_user_repo(self, username: str):
        ...
