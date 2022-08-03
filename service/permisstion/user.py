from starlette import status
from starlette.responses import Response

from repo.user import UserRepo
from schema import UserReq


class UserService(UserRepo):
    def insert_user_service(self, user: UserReq):
        user = UserRepo().insert_user_repo(UserReq(
            created_at=user.created_at,
            created_by=user.created_by,
            updated_at=user.updated_at,
            updated_by=user.updated_by,
            username=user.username,
            password=user.password,
            firstname=user.firstname,
            lastname=user.lastname))
        return user

    def update_user_service(self, username: str, user: UserReq):
        user = UserRepo().update_product_repo(username=username,
                                              user=UserReq(
                                                  created_at=user.created_at,
                                                  created_by=user.created_by,
                                                  updated_at=user.updated_at,
                                                  updated_by=user.updated_by,
                                                  username=user.username,
                                                  password=user.password,
                                                  firstname=user.firstname,
                                                  lastname=user.lastname))
        return user

    def get_users_service(self, role_name: str):
        users = UserRepo().get_users()
        list_user = []
        for user in users:
            username = user['User'].username
            role = UserRepo().get_role(username, role_name)
            permission = UserRepo().get_permisstion(role['Role'].code)
            list_user.append({'user': user['User'], 'role': role['Role'].name, 'permission': permission})
        return list_user

    def get_user_by_username_service(self, username: str):
        user = UserRepo().get_user_by_username_repo(username)
        return user

    def delete_user_service(self, username: str):
        user = UserRepo().delete_user_repo(username=username)


