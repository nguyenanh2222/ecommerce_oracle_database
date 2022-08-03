from starlette.authentication import BaseUser


class UserAuth(BaseUser):

    def __init__(self, username: str):
        self.username = username

    @property
    def display_name(self) -> str:
        return self.username

    @property
    def identity(self) -> str:
        return self.username

    @property
    def is_authenticated(self) -> bool:
        return True
